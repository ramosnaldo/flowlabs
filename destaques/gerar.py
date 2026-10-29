"""Gera as capas de destaque (Instagram highlights) com as logos.

Fundo: gradiente diagonal de azul profundo para ciano + grão monocromático.
Formato 1080x1920; a logo fica centralizada no círculo seguro (o Instagram
recorta um círculo no centro da imagem).

Uso (na raiz do repo):  python3 destaques/gerar.py
"""
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = Path(__file__).resolve().parent

W, H = 1080, 1920
CIRCULO = 1080            # diâmetro do recorte do Instagram, centrado na imagem
AZUL_PROFUNDO = (6, 22, 74)    # #06164A
AZUL_MEIO = (14, 92, 168)      # #0E5CA8
CIANO = (59, 225, 240)         # #3BE1F0 (ciano FLOW Labs)
GRAO = 0.07                    # 7% (manual FLOW Labs: grão 4–8%)
SEED = 360

CAPAS = [
    # (arquivo, logo, largura da logo em px)
    ("destaque-peregrinus.png",
     RAIZ / "peregrinus/01-logos/png/peregrinus-falcao-p-branco.png", 600),
    ("destaque-flowlabs.png",
     RAIZ / "brand/flow-labs/logo-simbolo.png", 720),
]

# Mesma ordem do render-icones.mjs (só para montar o preview).
ICONES = ["medalha", "bota-trilha", "cerebro", "jejum", "70km", "50km", "ultramaratona",
          "halter", "skate", "voltar", "livro", "cachorro", "festa"]


def fundo() -> Image.Image:
    y, x = np.mgrid[0:H, 0:W].astype(np.float32)
    # Diagonal (topo-esquerda → base-direita), comprimida no quadrado central
    # para o círculo visível mostrar a transição inteira.
    cy0, cy1 = (H - CIRCULO) / 2, (H + CIRCULO) / 2
    t = ((y - cy0) / (cy1 - cy0)) * 0.75 + (x / W) * 0.25
    t = np.clip(t, 0, 1)[..., None]
    a, m, c = (np.array(v, np.float32) for v in (AZUL_PROFUNDO, AZUL_MEIO, CIANO))
    cor = np.where(t < 0.5, a + (m - a) * (t / 0.5), m + (c - m) * ((t - 0.5) / 0.5))
    ruido = np.random.default_rng(SEED).normal(0, 255 * GRAO, (H, W, 1))
    return Image.fromarray(np.clip(cor + ruido, 0, 255).astype(np.uint8), "RGB")


def capa(logo_path: Path, largura: int) -> Image.Image:
    img = fundo()
    logo = Image.open(logo_path).convert("RGBA")
    bbox = logo.getbbox()
    logo = logo.crop(bbox)
    alt = round(logo.height * largura / logo.width)
    logo = logo.resize((largura, alt), Image.LANCZOS)
    img.paste(logo, ((W - largura) // 2, (H - alt) // 2), logo)
    return img


def preview(capas: list[Image.Image], colunas: int = 5) -> Image.Image:
    """Simula os destaques do perfil (círculos com borda), em grade."""
    d, gap, pad = 300, 100, 90
    linhas = -(-len(capas) // colunas)
    larg = pad * 2 + d * colunas + gap * (colunas - 1)
    alt = pad * 2 + d * linhas + gap * (linhas - 1)
    pv = Image.new("RGB", (larg, alt), (10, 10, 11))
    mask = Image.new("L", (d, d), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, d - 1, d - 1), fill=255)
    draw = ImageDraw.Draw(pv)
    top = (H - CIRCULO) // 2
    for i, c in enumerate(capas):
        quad = c.crop((0, top, W, top + CIRCULO)).resize((d, d), Image.LANCZOS)
        x = pad + (i % colunas) * (d + gap)
        y = pad + (i // colunas) * (d + gap)
        pv.paste(quad, (x, y), mask)
        draw.ellipse((x - 10, y - 10, x + d + 10, y + d + 10), outline=(58, 59, 64), width=4)
    return pv


if __name__ == "__main__":
    feitas = []
    for nome, logo, largura in CAPAS:
        c = capa(logo, largura)
        c.save(SAIDA / nome, optimize=True)
        feitas.append(c)
        print("ok", nome)
    # Capas de ícone e texto: renderizadas no Chromium sobre o mesmo fundo.
    fundo().save(SAIDA / ".fundo.png")
    subprocess.run(["node", str(SAIDA / "render-icones.mjs")], check=True)
    (SAIDA / ".fundo.png").unlink()
    for nome in ICONES:
        feitas.append(Image.open(SAIDA / f"destaque-{nome}.png").convert("RGB"))
    preview(feitas).save(SAIDA / "preview-destaques.png", optimize=True)
    print("ok preview-destaques.png")
