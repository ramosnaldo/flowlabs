"""Re-edit of reels_momentos_profissional.mp4.

- Removes the polaroid dog photo (source 16.0s-18.0s, exactly 4 beats at 120 BPM,
  so the music stays on the grid).
- In-place transitions on every cut (whip pans, zoom blur, glitch, flash, spin,
  punch-ins) so the baked-in titles keep their original timing.
- Animated overlay graphics: progress bar, viewfinder brackets, chapter tags,
  audio-reactive HUD, GPS-style route, yellow stripe wipes, light leaks, grain.
- Synthesized whoosh / impact SFX under the transitions.

Usage: python3 edit.py SRC.mp4 OUT.mp4 [WORKDIR]
"""
import math
import subprocess
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy.signal import butter, sosfilt

SRC, OUT = sys.argv[1], sys.argv[2]
WORK = sys.argv[3] if len(sys.argv) > 3 else "."
W, H, FPS = 1080, 1920, 30
CUT_A, CUT_B = 16.0, 18.0  # removed span (polaroid dog photo), source seconds
SRC_FRAMES = 990
SKIP = range(int(CUT_A * FPS), int(CUT_B * FPS))
N = SRC_FRAMES - len(SKIP)  # output frames
DUR = N / FPS
YEL = (244, 196, 48)
FONT_B = "/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf"
FONT_M = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
rng = np.random.default_rng(7)

# ---------------------------------------------------------------- timeline
# (output seconds, transition kind, extras)
TRANS = [
    (0.0, "intro", {"flash", "sfx_hit"}),
    (4.0, "punch", {"sfx_whoosh"}),
    (6.5, "zoom", {"leak", "stripe", "sfx_whoosh"}),
    (8.0, "whipL", {"sfx_whoosh"}),
    (9.5, "whipU", {"sfx_whoosh"}),
    (10.5, "glitch", {"sfx_glitch"}),
    (11.5, "whipR", {"sfx_whoosh"}),
    (12.5, "zoom", {"flash", "stripe", "sfx_hit"}),
    (14.5, "whipL", {"sfx_whoosh"}),
    (16.0, "zoom", {"flash", "leak", "stripe", "sfx_hit"}),  # join where the photo was
    (18.0, "spin", {"sfx_whoosh"}),
    (20.0, "punch", {"flash", "shake", "stripe", "sfx_hit"}),
    (21.0, "punch", {"shake"}),
    (21.7, "punch", {"shake"}),
    (22.233, "whipL", {"stripe", "sfx_whoosh"}),
    (22.567, "punch", set()),
    (22.9, "punch", set()),
    (23.233, "glitch", {"sfx_glitch"}),
    (23.567, "punch", set()),
    (23.9, "punch", set()),
    (24.0, "zoom", {"leak", "stripe", "sfx_whoosh"}),
    (26.0, "none", {"leak"}),
]
CHAPTERS = [
    (0.0, "01", "CORRER"),
    (6.5, "02", "MOMENTOS"),
    (12.5, "03", "AMIGOS"),
    (16.0, "04", "SOL & CHUVA"),
    (20.0, "05", "CONSTÂNCIA"),
    (22.233, "06", "UM PASSO"),
    (26.0, "07", "O CAMINHO"),
]
SEG_STARTS = [t for t, k, _ in TRANS if k not in ("punch", "none")] + [DUR]


def ease_out(x):
    return 1 - (1 - x) ** 3


def ease_in(x):
    return x ** 3


def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


# ---------------------------------------------------------------- audio
def load_audio():
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", SRC, "-f", "f32le", "-ac", "2", "-ar", "48000", "-"],
        capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def cut_audio(a, sr=48000):
    i0, i1, xf = int(CUT_A * sr), int(CUT_B * sr), int(0.04 * sr)
    ramp = np.linspace(0, 1, xf)[:, None]
    mid = a[i0 - xf:i0] * (1 - ramp) + a[i1 - xf:i1] * ramp
    out = np.concatenate([a[:i0 - xf], mid, a[i1:]])
    return out[: int(DUR * sr)]


def sfx_track(n, sr=48000):
    out = np.zeros(n, np.float32)
    for t, _, ex in TRANS:
        c = int(t * sr)
        if "sfx_whoosh" in ex:
            L = int(0.42 * sr)
            noise = rng.standard_normal(L).astype(np.float32)
            # sweep a band-pass upwards by filtering in chunks
            seg = np.zeros(L, np.float32)
            chunks = 12
            for k in range(chunks):
                lo = 300 + 2600 * k / chunks
                sos = butter(2, [lo, lo * 2.2], "bandpass", fs=sr, output="sos")
                s = slice(k * L // chunks, (k + 1) * L // chunks)
                seg[s] = sosfilt(sos, noise)[s]
            env = np.sin(np.linspace(0, math.pi, L)) ** 2
            seg *= env * 0.22
            st = c - int(0.3 * sr)
        elif "sfx_hit" in ex:
            L = int(0.5 * sr)
            tt = np.arange(L) / sr
            boom = np.sin(2 * math.pi * (55 + 60 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9)
            sos = butter(2, 4000, "highpass", fs=sr, output="sos")
            air = sosfilt(sos, rng.standard_normal(L)) * np.exp(-tt * 25)
            seg = (boom * 0.45 + air * 0.12).astype(np.float32)
            st = c
        elif "sfx_glitch" in ex:
            L = int(0.18 * sr)
            tt = np.arange(L) / sr
            seg = (np.sign(np.sin(2 * math.pi * 900 * tt)) * (rng.random(L) > 0.5)
                   * np.exp(-tt * 18) * 0.08).astype(np.float32)
            st = c - int(0.05 * sr)
        else:
            continue
        st = max(0, st)
        e = min(n, st + len(seg))
        out[st:e] += seg[: e - st]
    return out


def band_levels(mono, sr=48000, bands=6):
    """Per-output-frame levels in log-spaced bands, for the HUD meter."""
    hop = sr // FPS
    edges = np.geomspace(60, 8000, bands + 1)
    freqs = np.fft.rfftfreq(2048, 1 / sr)
    lv = np.zeros((N, bands))
    win = np.hanning(2048)
    for i in range(N):
        s = i * hop
        fr = mono[s:s + 2048]
        if len(fr) < 2048:
            fr = np.pad(fr, (0, 2048 - len(fr)))
        sp = np.abs(np.fft.rfft(fr * win))
        for b in range(bands):
            m = (freqs >= edges[b]) & (freqs < edges[b + 1])
            lv[i, b] = np.log1p(sp[m].mean())
    lv = (lv - lv.min(0)) / (np.ptp(lv, 0) + 1e-6)
    sm = np.copy(lv)  # fast attack, slow release
    for i in range(1, N):
        sm[i] = np.maximum(lv[i], sm[i - 1] * 0.82)
    return sm


# ---------------------------------------------------------------- image fx
def affine(img, scale=1.0, dx=0.0, dy=0.0, rot=0.0, border=cv2.BORDER_REFLECT):
    if scale == 1.0 and dx == 0 and dy == 0 and rot == 0:
        return img
    M = cv2.getRotationMatrix2D((W / 2, H / 2), rot, scale)
    M[0, 2] += dx
    M[1, 2] += dy
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=border)


def motion_blur(img, k, vertical=False):
    k = int(k)
    if k < 3:
        return img
    return cv2.blur(img, (1, k) if vertical else (k, 1))


def zoom_blur(img, scale, amount):
    if amount < 0.004:
        return affine(img, scale)
    acc = np.zeros(img.shape, np.float32)
    steps = 6
    for s in np.linspace(scale, scale * (1 + amount), steps):
        acc += affine(img, s)
    return (acc / steps).astype(np.uint8)


def rgb_split(img, off):
    off = int(off)
    if off == 0:
        return img
    out = img.copy()
    out[:, :, 2] = np.roll(img[:, :, 2], off, axis=1)
    out[:, :, 0] = np.roll(img[:, :, 0], -off, axis=1)
    return out


def slice_glitch(img, strength):
    out = img.copy()
    for _ in range(int(6 * strength) + 1):
        y = int(rng.integers(0, H - 80))
        h = int(rng.integers(20, 140))
        out[y:y + h] = np.roll(out[y:y + h], int(rng.integers(-90, 90) * strength), axis=1)
    return out


def make_leak():
    yy, xx = np.mgrid[0:H // 4, 0:W // 4].astype(np.float32)
    leak = np.zeros((H // 4, W // 4, 3), np.float32)
    for cx, cy, r, col in [(0.1, 0.25, 0.55, (40, 120, 255)), (0.8, 0.65, 0.5, (60, 170, 255)),
                           (0.4, 0.95, 0.4, (90, 60, 255))]:  # BGR warm
        d = np.sqrt((xx / (W / 4) - cx) ** 2 + (yy / (H / 4) - cy) ** 2)
        leak += np.exp(-(d / r) ** 2)[:, :, None] * np.array(col, np.float32)
    leak = np.clip(leak, 0, 255)
    return cv2.resize(leak, (W * 2, H), interpolation=cv2.INTER_CUBIC)


LEAK = make_leak()
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
VIGNETTE = (1 - 0.32 * (((xx / W - 0.5) ** 2 + (yy / H - 0.5) ** 2) / 0.5) ** 1.3)[:, :, None]
GRAIN = [(rng.standard_normal((H // 2, W // 2, 1)) * 4).astype(np.float32) for _ in range(6)]


def screen(img, layer, a):
    f = img.astype(np.float32)
    l = layer * a
    return (255 - (255 - f) * (255 - l) / 255).astype(np.uint8)


# ---------------------------------------------------------------- overlay
fB = lambda s: ImageFont.truetype(FONT_B, s)
fM = lambda s: ImageFont.truetype(FONT_M, s)


def chapter_tag(num, name):
    font, font2 = fB(30), fM(26)
    txt = name
    tw = int(font2.getlength(txt) + 3 * len(txt))
    im = Image.new("RGBA", (tw + 150, 60), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.text((0, 12), num, font=font, fill=YEL + (255,))
    d.line([(52, 30), (92, 30)], fill=(255, 255, 255, 200), width=3)
    x = 108
    for ch in txt:  # tracked caps
        d.text((x, 14), ch, font=font2, fill=(255, 255, 255, 235))
        x += font2.getlength(ch) + 3
    return im.rotate(90, expand=True)


TAGS = [chapter_tag(n, s) for _, n, s in CHAPTERS]
ROUTE = []
for i in range(400):
    u = i / 399
    ROUTE.append((
        40 + 200 * u + 26 * math.sin(u * 9.0),
        150 - 95 * math.sin(u * math.pi * 1.25) + 18 * math.sin(u * 17),
    ))


def overlay(i, t, levels, kick):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    intro = ease_out(clamp(t / 0.6))
    outro = 1 - clamp((t - (DUR - 0.6)) / 0.5)
    vis = intro * outro
    a = lambda v: int(v * vis)

    # progress bar
    d.rectangle([0, 0, W, 7], fill=(255, 255, 255, a(55)))
    d.rectangle([0, 0, int(W * t / DUR), 7], fill=YEL + (a(255),))

    # viewfinder brackets (fly in, breathe on transitions)
    inset = 46 + (1 - intro) * 160 - kick * 18
    L, sw = 74, 5
    for cx, cy, sx, sy in [(inset, inset + 10, 1, 1), (W - inset, inset + 10, -1, 1),
                           (inset, H - inset, 1, -1), (W - inset, H - inset, -1, -1)]:
        d.line([(cx, cy), (cx + sx * L, cy)], fill=(255, 255, 255, a(210)), width=sw)
        d.line([(cx, cy), (cx, cy + sy * L)], fill=(255, 255, 255, a(210)), width=sw)

    # chapter tag, right edge
    ci = max(k for k, c in enumerate(CHAPTERS) if c[0] <= t + 1e-6)
    c0 = CHAPTERS[ci][0]
    c1 = CHAPTERS[ci + 1][0] if ci + 1 < len(CHAPTERS) else DUR
    pin = ease_out(clamp((t - c0 - 0.1) / 0.4))
    pout = clamp((c1 - t) / 0.25)
    tag = TAGS[ci]
    if pin * pout > 0:
        x = int(W - 58 - tag.width + (1 - pin) * 120)
        y = int(H * 0.5 - tag.height / 2)
        t_alpha = tag.copy()
        t_alpha.putalpha(t_alpha.getchannel("A").point(lambda v: int(v * pin * pout * vis)))
        im.alpha_composite(t_alpha, (x, y))

    # HUD chip: timecode + audio-reactive meter
    hx, hy = 64, H - 210
    d.rounded_rectangle([hx, hy, hx + 312, hy + 78], radius=39, fill=(10, 10, 10, a(120)))
    blink = 1.0 if (t % 1.0) < 0.6 else 0.25
    d.ellipse([hx + 26, hy + 30, hx + 44, hy + 48], fill=YEL + (a(255 * blink),))
    d.text((hx + 58, hy + 18), f"00:{int(t):02d}", font=fB(36), fill=(255, 255, 255, a(240)))
    for b in range(6):
        h = 8 + levels[i, b] * 40
        bx = hx + 180 + b * 19
        d.rounded_rectangle([bx, hy + 39 - h / 2, bx + 9, hy + 39 + h / 2], radius=4,
                            fill=(255, 255, 255, a(225)) if b % 2 else YEL + (a(255),))

    # GPS-style route, draws over the whole video
    rx, ry = W - 330, H - 300
    pts = [(rx + px, ry + py) for px, py in ROUTE]
    d.line(pts, fill=(255, 255, 255, a(70)), width=5, joint="curve")
    k = max(2, int(len(pts) * clamp(t / (DUR - 0.8))))
    d.line(pts[:k], fill=YEL + (a(255),), width=7, joint="curve")
    hx2, hy2 = pts[k - 1]
    pr = (t * 1.6) % 1.0
    r = 10 + pr * 26
    d.ellipse([hx2 - r, hy2 - r, hx2 + r, hy2 + r], outline=YEL + (a(200 * (1 - pr)),), width=3)
    d.ellipse([hx2 - 10, hy2 - 10, hx2 + 10, hy2 + 10], fill=(255, 255, 255, a(255)))
    d.text((rx + 40, ry - 26), "ROTA", font=fM(22), fill=(255, 255, 255, a(170)))

    # yellow stripe wipes across stripe cuts
    for tc, _, ex in TRANS:
        if "stripe" not in ex:
            continue
        p = (t - tc) / 0.3 + 0.5  # 0..1 over 0.3s centred on the cut
        if 0 <= p <= 1:
            p = ease_in(p) * 0.5 + ease_out(p) * 0.5
            x0 = -900 + p * (W + 1500)
            sk = 420
            d.polygon([(x0, H), (x0 + 380, H), (x0 + 380 + sk * 4.6, 0), (x0 + sk * 4.6, 0)],
                      fill=YEL + (235,))
            x1 = x0 - 120
            d.polygon([(x1, H), (x1 + 40, H), (x1 + 40 + sk * 4.6, 0), (x1 + sk * 4.6, 0)],
                      fill=(255, 255, 255, 220))
    return np.array(im)


def alpha_over(bgr, rgba):
    a = rgba[:, :, 3:4].astype(np.float32) / 255
    if not a.any():
        return bgr
    fg = rgba[:, :, 2::-1].astype(np.float32)
    return (bgr.astype(np.float32) * (1 - a) + fg * a).astype(np.uint8)


# ---------------------------------------------------------------- per-frame
def transform(img, t):
    """Apply camera-move style transitions around each cut. Returns (img, kick, flash, leak)."""
    f = t * FPS
    # slow push-in / pull-out per segment so nothing sits static
    seg = max(k for k, s in enumerate(SEG_STARTS) if s <= t + 1e-6)
    s0, s1 = SEG_STARTS[seg], SEG_STARTS[min(seg + 1, len(SEG_STARTS) - 1)]
    u = clamp((t - s0) / max(0.01, s1 - s0))
    base = 1.0 + (0.05 * u if seg % 2 == 0 else 0.05 * (1 - u))
    # beat pulse (once per second, on the kick at x.34s)
    ph = (t - 0.34) % 1.0
    pulse = 0.018 * math.exp(-ph * 9) if ph < 0.25 and t > 0.5 else 0.0
    scale, dx, dy, rot = base + pulse, 0.0, 0.0, 0.0
    blur_h = blur_v = zb = 0.0
    split = 0.0
    glitch = 0.0
    border = cv2.BORDER_REFLECT
    kick = flash = leak = 0.0
    for tc, kind, ex in TRANS:
        d = f - tc * FPS  # frames from cut, negative = outgoing
        if abs(d) > 14:
            continue
        if kind in ("whipL", "whipR", "whipU") and -5 <= d < 5:
            sgn = -1 if kind == "whipL" else 1
            if d < 0:
                p = ease_in((d + 5) / 5)
                off = sgn * p * 0.55
            else:
                p = ease_out(1 - d / 5) if d > 0 else 1.0
                off = -sgn * p * 0.55
            amt = abs(off)
            border = cv2.BORDER_WRAP  # continuous pan, no mirrored edges
            if kind == "whipU":
                dy += off * H
                blur_v = max(blur_v, amt * 260)
            else:
                dx += off * W
                blur_h = max(blur_h, amt * 260)
            scale += amt * 0.15
            kick = max(kick, amt * 2)
        elif kind == "zoom" and -6 <= d < 7:
            if d < 0:
                p = ease_in((d + 6) / 6)
                scale *= 1 + 0.6 * p
            else:
                p = 1 - ease_out(d / 7)
                scale *= 1 + 0.35 * p
            zb = max(zb, 0.12 * p)
            kick = max(kick, p)
        elif kind == "spin" and -6 <= d < 7:
            if d < 0:
                p = ease_in((d + 6) / 6)
                rot += 14 * p
            else:
                p = 1 - ease_out(d / 7)
                rot -= 14 * p
            scale *= 1 + 0.3 * p
            zb = max(zb, 0.06 * p)
            blur_h = max(blur_h, 40 * p)
            kick = max(kick, p)
        elif kind == "glitch" and -3 <= d < 4:
            p = 1 - abs(d) / 4
            split = max(split, 34 * p)
            glitch = max(glitch, p)
            kick = max(kick, p * 0.6)
        elif kind in ("punch", "intro") and 0 <= d < 9:
            p = 1 - ease_out(d / 9)
            scale *= 1 + (0.35 if kind == "intro" else 0.09) * p
            zb = max(zb, (0.05 if kind == "intro" else 0.02) * p)
            kick = max(kick, p)
            if kind == "punch" and d < 3:
                split = max(split, 10 * (1 - d / 3))
        if "flash" in ex and -2 <= d < 8:
            flash = max(flash, (d + 3) / 3 if d < 0 else math.exp(-d / 1.4))
        if "shake" in ex and 0 <= d < 10:
            amp = 22 * (1 - d / 10)
            dx += rng.uniform(-amp, amp)
            dy += rng.uniform(-amp, amp)
        if "leak" in ex and -12 <= d <= 14:
            leak = max(leak, 1 - abs(d) / 14)

    out = zoom_blur(img, scale, zb) if zb > 0 else img
    if zb > 0 and (dx or dy or rot):
        out = affine(out, 1.0, dx, dy, rot, border)
    elif zb == 0:
        out = affine(out, scale, dx, dy, rot, border)
    out = motion_blur(out, blur_h)
    out = motion_blur(out, blur_v, vertical=True)
    if glitch:
        out = slice_glitch(out, glitch)
    out = rgb_split(out, split)
    return out, kick, flash, leak


def main():
    audio = load_audio()
    cut = cut_audio(audio)
    sfx = sfx_track(len(cut))
    mix = cut + sfx[:, None]
    peak = np.abs(mix).max()
    if peak > 0.98:
        mix *= 0.98 / peak
    wav = f"{WORK}/mix.f32"
    mix.astype(np.float32).tofile(wav)
    levels = band_levels(cut.mean(1))

    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", SRC, "-f", "rawvideo", "-pix_fmt", "bgr24", "-"],
                           stdout=subprocess.PIPE)
    enc = subprocess.Popen(
        ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{W}x{H}",
         "-r", str(FPS), "-i", "-", "-f", "f32le", "-ar", "48000", "-ac", "2", "-i", wav,
         "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "slow", "-crf", "21", "-maxrate", "12M", "-bufsize", "24M",
         "-pix_fmt", "yuv420p", "-profile:v", "high", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", "-shortest", OUT],
        stdin=subprocess.PIPE)
    fs = W * H * 3
    i = 0
    for src_idx in range(SRC_FRAMES):
        buf = dec.stdout.read(fs)
        if len(buf) < fs:
            break
        if src_idx in SKIP:
            continue
        t = i / FPS
        img = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
        img, kick, flash, leak = transform(img, t)
        if leak > 0:
            off = int((t * 400) % W)
            img = screen(img, LEAK[:, off:off + W], 0.45 * leak)
        f = img.astype(np.float32) * VIGNETTE
        f += cv2.resize(GRAIN[i % 6], (W, H), interpolation=cv2.INTER_NEAREST)[:, :, None]
        if flash > 0:
            f = f + (255 - f) * min(1.0, flash) * 0.7
        img = np.clip(f, 0, 255).astype(np.uint8)
        img = alpha_over(img, overlay(i, t, levels, kick))
        if t > DUR - 0.5:  # final fade
            img = (img * clamp((DUR - t) / 0.5)).astype(np.uint8)
        enc.stdin.write(img.tobytes())
        i += 1
        if i % 60 == 0:
            print(f"{i}/{N}", flush=True)
    enc.stdin.close()
    enc.wait()
    dec.wait()


if __name__ == "__main__":
    main()
