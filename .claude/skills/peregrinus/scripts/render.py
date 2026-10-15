"""Renderiza artes HTML da Peregrinus em PNG usando o Chrome (ou Edge) instalado.

Uso: python render.py slide-01.html [slide-02.html ...]
O tamanho vem de data-size="LARGURAxALTURA" no <body> (padrão 1080x1350).
O PNG sai ao lado do HTML, com o mesmo nome.
"""
import os
import re
import subprocess
import sys
import tempfile

BROWSERS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def browser():
    for b in BROWSERS:
        if os.path.exists(b):
            return b
    sys.exit("Chrome ou Edge não encontrado.")


def render(path):
    path = os.path.abspath(path)
    html = open(path, encoding="utf-8").read()
    m = re.search(r'data-size="(\d+)x(\d+)"', html)
    w, h = (int(m.group(1)), int(m.group(2))) if m else (1080, 1350)
    out = os.path.splitext(path)[0] + ".png"
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run([
            browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--force-device-scale-factor=1", f"--user-data-dir={profile}",
            f"--window-size={w},{h}", "--virtual-time-budget=8000",
            f"--screenshot={out}", "file:///" + path.replace("\\", "/"),
        ], check=True, capture_output=True, timeout=90)
    print(f"{out}  ({w}x{h})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        render(p)
