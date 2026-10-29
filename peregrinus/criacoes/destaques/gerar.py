"""Capas de destaque do Instagram (1080x1920), ícones do brand kit 2.0 em preto sobre azul
mais escuro (#2FA8D0) com granulação fina.

Uso: python gerar.py  ->  cria destaque-<nome>.html nesta pasta.
O ícone fica no centro: o Instagram recorta um círculo no meio da imagem.
"""
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
ICONES = os.path.join(AQUI, "..", "..", "06-elementos-graficos", "icones")
STROKE = 'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="square" stroke-linejoin="miter"'


def icone_kit(nome):
    # Reaproveita o desenho do kit, trocando o preto fixo por currentColor e afinando o traço.
    svg = open(os.path.join(ICONES, f"icone-{nome}.svg"), encoding="utf-8").read()
    return svg.replace('stroke="#000000"', 'stroke="currentColor"').replace('stroke-width="1.7"', 'stroke-width="1.5"')


# APP: celular com o falcão em P (desenho do cliente) na tela; TIME: escudo de time com o falcão em P. Desenhados no mesmo traço dos ícones do kit.
DEFS = open(os.path.join(AQUI, "..", "stories-como-funciona-app", "_defs.svg"), encoding="utf-8").read()
FALCAO = re.search(r'<symbol id="fal"[^>]*>(.*?)</symbol>', DEFS, re.S).group(1).replace("<path ", '<path fill="currentColor" ')
APP = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" {STROKE}><rect x="6.5" y="1.5" width="11" height="21" rx="1.5"/><path d="M10.5 19.5 H13.5"/><svg x="8.3" y="7.6" width="7.4" height="5.9" viewBox="20 23 690 548">{FALCAO}</svg></svg>'
TIME = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" {STROKE}><path d="M12 1.8 L20.5 4.8 V11 C20.5 16.6 16.8 20.4 12 22.2 C7.2 20.4 3.5 16.6 3.5 11 V4.8 Z"/><svg x="7.2" y="7.2" width="9.6" height="7.6" viewBox="20 23 690 548">{FALCAO}</svg></svg>'

DESTAQUES = [
    ("app", APP),
    ("encontros", icone_kit("eventos")),
    ("time", TIME),
    ("grupo", icone_kit("comunidade")),
]

PAGINA = """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden}}
body{{background:#2FA8D0;color:#000;display:flex;align-items:center;justify-content:center}}
.grao{{position:absolute;inset:0;width:100%;height:100%;mix-blend-mode:overlay;opacity:1}}
.ic{{position:relative;width:440px;height:440px}}
.ic svg{{width:100%;height:100%}}
</style></head>
<body data-size="1080x1920"><img class="grao" src="grao.png" alt=""><div class="ic">{svg}</div></body></html>
"""

# Textura de grão: ruído cinza centrado em 50%, então o overlay não muda o tom do azul.
if not os.path.exists(os.path.join(AQUI, "grao.png")):
    from PIL import Image, ImageFilter
    import random
    random.seed(7)
    g = Image.effect_noise((1080, 1920), 38).filter(ImageFilter.GaussianBlur(0.6))
    g.save(os.path.join(AQUI, "grao.png"))

for nome, svg in DESTAQUES:
    with open(os.path.join(AQUI, f"destaque-{nome}.html"), "w", encoding="utf-8") as f:
        f.write(PAGINA.format(svg=svg))
print(len(DESTAQUES), "destaques")
