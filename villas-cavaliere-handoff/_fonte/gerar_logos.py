#!/usr/bin/env python3
"""Gera os SVGs dos logos da Villas Cavaliere com o texto convertido em curvas.

O simbolo vem do vetor original do manual (simbolo-original.d). VILLAS e
CAVALIERE sao desenhados a partir das fontes em 03-fontes, com kerning via
HarfBuzz, e saem como <path>: os arquivos abrem iguais sem a fonte instalada.

Uso:  pip install fonttools uharfbuzz
      python3 _fonte/gerar_logos.py
Depois rode _fonte/exportar.mjs para gerar os PNG e PDF.
"""
import re
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

RAIZ = Path(__file__).resolve().parent.parent
FONTES = RAIZ / "03-fontes"
SAIDA = RAIZ / "01-logos" / "svg"

COR = {
    "noite": "#0F1E25",
    "marinho": "#1B2A4A",
    "cavaliere": "#5394A9",
    "blacktie": "#121417",
    "linho": "#EFEBE5",
    "areia": "#D6D1CA",
    "tiffany": "#81D8D0",
    "cinza": "#8E9196",
    "offwhite": "#F7F5F0",
}

# Paletas de cada versao. "grad" e o gradiente do simbolo (de -> para).
VERSOES = {
    "principal": dict(grad=(COR["cavaliere"], COR["marinho"]), fio=COR["cavaliere"],
                      villas=COR["cavaliere"], cavaliere=COR["noite"]),
    "negativa": dict(grad=(COR["offwhite"], COR["tiffany"]), fio=COR["cinza"],
                     villas=COR["tiffany"], cavaliere=COR["offwhite"]),
    "mono-blacktie": dict(grad=None, cor=COR["blacktie"]),
    "mono-offwhite": dict(grad=None, cor=COR["offwhite"]),
}

# ---------------------------------------------------------------- simbolo
# Unidade de medida: altura do simbolo = 100.
ALTURA_SIMBOLO = 100.0


def _num(s):
    return f"{s:.2f}".rstrip("0").rstrip(".")


def carregar_simbolo():
    d = (Path(__file__).parent / "simbolo-original.d").read_text().strip()
    nums = [float(n) for n in re.findall(r"-?\d+\.?\d*", d)]
    xs, ys = nums[0::2], nums[1::2]
    x0, y0, y1 = min(xs), min(ys), max(ys)
    k = ALTURA_SIMBOLO / (y1 - y0)
    largura = (max(xs) - x0) * k

    it = iter(nums)
    def par(_m):
        x, y = next(it), next(it)
        return f"{_num((x - x0) * k)} {_num((y - y0) * k)}"
    d = re.sub(r"-?\d+\.?\d*\s+-?\d+\.?\d*", par, d)
    d = re.sub(r"\s+", " ", d).replace(" Z M", "ZM").strip()
    return d, largura


SIMBOLO_D, LARGURA_SIMBOLO = carregar_simbolo()

# ---------------------------------------------------------------- texto
class Fonte:
    def __init__(self, arquivo):
        self.tt = TTFont(FONTES / arquivo)
        self.glyphs = self.tt.getGlyphSet()
        self.upm = self.tt["head"].unitsPerEm
        self.cap = self.tt["OS/2"].sCapHeight
        blob = hb.Blob.from_file_path(str(FONTES / arquivo))
        self.hb = hb.Font(hb.Face(blob))

    def texto(self, s, altura_cap, x, baseline, tracking_em=0.0):
        """Devolve (d, largura) com o texto em curvas. tracking em em."""
        buf = hb.Buffer()
        buf.add_str(s)
        buf.guess_segment_properties()
        hb.shape(self.hb, buf, {"kern": True})
        k = altura_cap / self.cap
        nomes = self.tt.getGlyphOrder()
        pen = SVGPathPen(self.glyphs, ntos=lambda v: _num(v))
        cx = 0.0
        n = len(buf.glyph_infos)
        for i, (info, pos) in enumerate(zip(buf.glyph_infos, buf.glyph_positions)):
            t = TransformPen(pen, (k, 0, 0, -k, x + cx * k, baseline))
            self.glyphs[nomes[info.codepoint]].draw(t)
            cx += pos.x_advance
            if i < n - 1:
                cx += tracking_em * self.upm
        return pen.getCommands(), cx * k

    def largura(self, s, altura_cap, tracking_em=0.0):
        return self.texto(s, altura_cap, 0, 0, tracking_em)[1]

    def tracking_para(self, s, altura_cap, largura_alvo):
        """Tracking (em) que faz o texto ocupar largura_alvo."""
        base = self.largura(s, altura_cap)
        k = altura_cap / self.cap
        return (largura_alvo - base) / ((len(s) - 1) * self.upm * k)


FINA = Fonte("YanoneKaffeesatz-ExtraLight.ttf")   # CAVALIERE, peso 200
LEVE = Fonte("YanoneKaffeesatz-Light.ttf")        # VILLAS, peso 300

# ---------------------------------------------------------------- lockups
# Proporcoes medidas no manual, em unidades da altura do simbolo.
H = dict(fio_x=139, fio_y0=-12.6, fio_y1=111.1, fio_w=2.6,
         texto_x=187, villas_base=7.4, villas_cap=22.2, villas_larg=153,
         cav_base=92.6, cav_cap=71.9, cav_larg=373)
V = dict(villas_base=149, villas_cap=17.2, villas_larg=130,
         cav_base=215.8, cav_cap=53.3, cav_larg=273)

TRACK_CAV_H = FINA.tracking_para("CAVALIERE", H["cav_cap"], H["cav_larg"])
TRACK_VIL_H = LEVE.tracking_para("VILLAS", H["villas_cap"], H["villas_larg"])
TRACK_CAV_V = FINA.tracking_para("CAVALIERE", V["cav_cap"], V["cav_larg"])
TRACK_VIL_V = LEVE.tracking_para("VILLAS", V["villas_cap"], V["villas_larg"])


def defs_gradiente(v, gid):
    if not v["grad"]:
        return ""
    a, b = v["grad"]
    # principal: luz no canto superior esquerdo; negativa: de cima para baixo
    x2, y2 = ("1", "1") if v is VERSOES["principal"] else ("0.35", "1")
    return (f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/>'
            f"</linearGradient></defs>")


def cores(v, gid):
    if v["grad"]:
        return f"url(#{gid})", v["fio"], v["villas"], v["cavaliere"]
    c = v["cor"]
    return c, c, c, c


def svg(w, h, corpo, titulo, x0=0.0, y0=0.0):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{_num(x0)} {_num(y0)} {_num(w)} {_num(h)}" '
            f'width="{_num(w * 4)}" height="{_num(h * 4)}" role="img" aria-label="{titulo}">'
            f"<title>{titulo}</title>{corpo}</svg>\n")


def simbolo(nome, v):
    gid = f"vc-grad-simbolo-{nome}"
    s, *_ = cores(v, gid)
    corpo = defs_gradiente(v, gid) + f'<path fill="{s}" fill-rule="evenodd" d="{SIMBOLO_D}"/>'
    return svg(LARGURA_SIMBOLO, ALTURA_SIMBOLO, corpo, "Villas Cavaliere")


def horizontal(nome, v):
    gid = f"vc-grad-horizontal-{nome}"
    s, f, cv, cc = cores(v, gid)
    d_vil, w_vil = LEVE.texto("VILLAS", H["villas_cap"], H["texto_x"], H["villas_base"], TRACK_VIL_H)
    d_cav, w_cav = FINA.texto("CAVALIERE", H["cav_cap"], H["texto_x"], H["cav_base"], TRACK_CAV_H)
    fio_x = H["fio_x"] - H["fio_w"] / 2
    corpo = (defs_gradiente(v, gid)
             + f'<path fill="{s}" fill-rule="evenodd" d="{SIMBOLO_D}"/>'
             + f'<rect fill="{f}" x="{_num(fio_x)}" y="{_num(H["fio_y0"])}" width="{_num(H["fio_w"])}" '
               f'height="{_num(H["fio_y1"] - H["fio_y0"])}"/>'
             + f'<path fill="{cv}" d="{d_vil}"/><path fill="{cc}" d="{d_cav}"/>')
    y0 = min(H["fio_y0"], H["villas_base"] - H["villas_cap"]) - 2
    y1 = max(H["fio_y1"], ALTURA_SIMBOLO) + 2
    largura = H["texto_x"] + max(w_vil, w_cav) + 2
    return svg(largura, y1 - y0, corpo, "Villas Cavaliere", 0, y0)


def _pilha(v, gid, com_simbolo):
    s, _, cv, cc = cores(v, gid)
    w_vil = LEVE.largura("VILLAS", V["villas_cap"], TRACK_VIL_V)
    w_cav = FINA.largura("CAVALIERE", V["cav_cap"], TRACK_CAV_V)
    largura = max(w_cav, w_vil, LARGURA_SIMBOLO)
    meio = largura / 2
    deslocar = 0 if com_simbolo else -(V["villas_base"] - V["villas_cap"])
    d_vil, _ = LEVE.texto("VILLAS", V["villas_cap"], meio - w_vil / 2,
                          V["villas_base"] + deslocar, TRACK_VIL_V)
    d_cav, _ = FINA.texto("CAVALIERE", V["cav_cap"], meio - w_cav / 2,
                          V["cav_base"] + deslocar, TRACK_CAV_V)
    corpo = defs_gradiente(v, gid) if com_simbolo else ""
    if com_simbolo:
        corpo += (f'<path fill="{s}" fill-rule="evenodd" transform="translate({_num(meio - LARGURA_SIMBOLO / 2)} 0)" '
                  f'd="{SIMBOLO_D}"/>')
    corpo += f'<path fill="{cv}" d="{d_vil}"/><path fill="{cc}" d="{d_cav}"/>'
    altura = V["cav_base"] + deslocar + 1
    return largura, altura, corpo


def vertical(nome, v):
    w, h, corpo = _pilha(v, f"vc-grad-vertical-{nome}", True)
    return svg(w + 4, h + 2, corpo, "Villas Cavaliere", -2, -1)


def assinatura(nome, v):
    w, h, corpo = _pilha(v, f"vc-grad-assinatura-{nome}", False)
    return svg(w + 4, h + 2, corpo, "Villas Cavaliere", -2, -1)


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    for f in SAIDA.glob("*.svg"):
        f.unlink()
    for forma, fn in [("horizontal", horizontal), ("vertical", vertical),
                      ("assinatura", assinatura), ("simbolo", simbolo)]:
        for nome, v in VERSOES.items():
            (SAIDA / f"vc-{forma}-{nome}.svg").write_text(fn(nome, v))
    print(f"tracking CAVALIERE horizontal {TRACK_CAV_H:+.3f} em, vertical {TRACK_CAV_V:+.3f} em")
    print(f"tracking VILLAS    horizontal {TRACK_VIL_H:+.3f} em, vertical {TRACK_VIL_V:+.3f} em")
    print(f"{len(list(SAIDA.glob('*.svg')))} SVGs em {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
