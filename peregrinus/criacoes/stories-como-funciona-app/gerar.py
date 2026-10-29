"""Gera os stories "Como funciona o app" (1080x1920) a partir do story.html do brand kit 2.0.

Uso: python gerar.py  ->  cria story-01.html ... story-10.html nesta pasta.
Fontes locais de ../../03-fontes (não depende do Google Fonts).
"""
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
DEFS = re.search(r"<defs>(.*?)</defs>", open(os.path.join(AQUI, "_defs.svg"), encoding="utf-8").read(), re.S).group(1)
TOTAL = 8

CSS = """
@font-face{font-family:"Anton";src:url(../../03-fontes/Anton-Regular.ttf)}
@font-face{font-family:"Inter";src:url(../../03-fontes/Inter-Variable.ttf);font-weight:100 900}
@font-face{font-family:"Instrument Serif";font-style:italic;src:url(../../03-fontes/InstrumentSerif-Italic.ttf)}
@font-face{font-family:"Space Mono";src:url(../../03-fontes/SpaceMono-Regular.ttf)}
@font-face{font-family:"Space Mono";font-weight:700;src:url(../../03-fontes/SpaceMono-Bold.ttf)}
:root{--blue:#36BFEC;--blue-d:#1A7FA6;--black:#000;--grey:#888888;--light:#D6D6D6;--white:#fff;--line:rgba(255,255,255,.16)}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
body{position:relative;font-family:"Inter",sans-serif;background:var(--black);color:var(--white)}
body.azul{background:var(--blue);color:var(--black)}
.safe{position:absolute;inset:250px 80px 250px 80px;display:flex;flex-direction:column;z-index:3}
.top{display:flex;justify-content:space-between;align-items:center}
.lockup{display:flex;align-items:center;gap:18px}
.lockup svg{height:66px;width:auto;fill:var(--blue)}
body.azul .lockup svg,.capa .lockup svg{fill:var(--black)}
.wm{font-family:"Anton",sans-serif;text-transform:uppercase;letter-spacing:.05em;line-height:1;font-size:40px;white-space:nowrap}
.wm .i{display:inline-block;clip-path:polygon(-10% -10%,110% -10%,110% 74%,-10% 92%)}
.tag{display:flex;align-items:center;gap:16px;font-family:"Space Mono",monospace;font-size:22px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey)}
body.azul .tag,.capa .tag,.capa .wm{color:var(--black)}
.capa-foto .tag{color:var(--white)}
.tag svg{width:34px;height:34px}
.mid{flex:1;display:flex;flex-direction:column;justify-content:center}
.step{display:flex;align-items:flex-end;gap:22px;margin-bottom:18px}
.step .n{font-family:"Anton",sans-serif;font-size:190px;line-height:.8;color:var(--blue)}
.step .l{font-family:"Space Mono",monospace;font-size:22px;letter-spacing:.16em;color:var(--grey);padding-bottom:8px}
.title{font-family:"Anton",sans-serif;text-transform:uppercase;font-size:132px;line-height:.88;letter-spacing:.005em}
.title em{font-style:normal;color:var(--blue)}
body.azul .title em{color:var(--white)}
.eyebrow{font-family:"Instrument Serif",serif;font-style:italic;font-size:56px;line-height:1.1;color:var(--blue);margin-bottom:22px}
.body{font-size:36px;line-height:1.42;max-width:900px;margin-top:40px;color:#d4d4d4}
.body b{color:var(--white);font-weight:600}
body.azul .body{color:#06212b}
body.azul .body b{color:var(--black)}
.foot{display:flex;justify-content:space-between;align-items:center;font-family:"Space Mono",monospace;font-size:22px;letter-spacing:.12em;text-transform:uppercase;padding-top:26px;border-top:1.5px solid var(--line)}
body.azul .foot{border-color:rgba(0,0,0,.2)}
.foot svg{width:96px;height:32px;color:var(--blue)}
body.azul .foot svg{color:var(--black)}
.mono{font-family:"Space Mono",monospace;text-transform:uppercase;letter-spacing:.14em}
/* "telas" do app desenhadas no manual: fio fino, fundo chapado, raio 2px */
.ui{margin-top:52px;border:1.5px solid var(--line);border-radius:2px;padding:36px 38px;background:#0d0d0d}
.ui .lab{font-family:"Space Mono",monospace;font-size:20px;letter-spacing:.16em;color:var(--grey);text-transform:uppercase;margin-bottom:14px}
.field{border:1.5px solid rgba(255,255,255,.28);border-radius:2px;padding:22px 26px;font-size:32px;color:#bdbdbd}
.code{display:flex;gap:14px}
.code span{flex:1;height:96px;border:1.5px solid rgba(255,255,255,.28);border-radius:2px;display:flex;align-items:center;justify-content:center;font-family:"Space Mono",monospace;font-size:44px;font-weight:700}
.code span.on{border-color:var(--blue);color:var(--blue)}
.bt{display:flex;align-items:center;justify-content:space-between;background:var(--blue);color:var(--black);font-family:"Space Mono",monospace;font-weight:700;font-size:26px;letter-spacing:.16em;padding:24px 30px;border-radius:2px;text-transform:uppercase}
.bt svg{width:72px;height:24px}
.row{display:flex;gap:22px}
.col{flex:1;border:1.5px solid var(--line);border-radius:2px;padding:30px 28px;background:#0d0d0d}
.col h4{font-family:"Anton",sans-serif;font-weight:400;font-size:58px;line-height:1;margin-bottom:24px}
.col ol{list-style:none;counter-reset:s}
.col li{counter-increment:s;font-size:29px;line-height:1.3;padding:16px 0 16px 50px;position:relative;border-top:1.5px solid var(--line)}
.col li::before{content:counter(s);position:absolute;left:0;top:14px;font-family:"Space Mono",monospace;font-weight:700;font-size:26px;color:var(--blue)}
.chips{display:flex;flex-wrap:wrap;gap:12px}
.chip{font-family:"Space Mono",monospace;font-size:21px;letter-spacing:.14em;padding:10px 16px;border:1.5px solid rgba(255,255,255,.28);border-radius:2px;color:#cfcfcf}
.chip.on{background:var(--blue);border-color:var(--blue);color:var(--black);font-weight:700}
.list{margin-top:48px;border-top:1.5px solid var(--line)}
.list div{display:flex;justify-content:space-between;align-items:baseline;padding:26px 0;border-bottom:1.5px solid var(--line)}
.list .k{font-family:"Anton",sans-serif;font-size:62px;line-height:1}
.list .v{font-family:"Space Mono",monospace;font-size:28px;letter-spacing:.12em;color:var(--blue);font-weight:700;text-align:right}
.deg{display:flex;flex-direction:column;gap:7px;width:34px;flex:none;margin-top:12px}
.deg i{display:block;height:9px;background:var(--blue);border-radius:1px}
.feat{margin-top:46px;display:flex;flex-direction:column;gap:30px}
.feat>div{display:flex;gap:26px}
.feat h5{font-family:"Anton",sans-serif;font-weight:400;font-size:54px;line-height:1;text-transform:uppercase}
.feat p{font-size:29px;line-height:1.35;color:#cfcfcf;margin-top:8px}
.photo{height:330px;border-radius:2px;background:#1c1c1c;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.photo img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.1)}
.stamp{position:absolute;left:22px;bottom:22px;background:var(--black);color:var(--white);font-family:"Space Mono",monospace;font-size:20px;letter-spacing:.14em;padding:8px 14px;font-weight:700}
.stamp em{font-style:normal;color:var(--blue)}
.ic{width:46px;height:46px;flex:none}
"""

ICONS = """
<symbol id="fire" viewBox="0 0 24 24"><path d="M12 2c1 3.5 5 6 5 11a5 5 0 0 1-10 0c0-2.4 1.2-4 2.6-5.3.2 1.6 1 2.8 2.2 3.3C11 8.6 11.3 5 12 2z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></symbol>
<symbol id="msg" viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></symbol>
"""


def top(rotulo, capa=False):
    return f"""<div class="top"><div class="lockup"><svg viewBox="0 0 690 548"><use href="#fal"/></svg><span class="wm">PEREGR<span class="i">I</span>NUS</span></div><div class="tag"><span>{rotulo}</span><svg><use href="#xh"/></svg></div></div>"""


FOOT = """<div class="foot"><span>@peregrinusclub</span><svg><use href="#chev"/></svg></div>"""


def page(conteudo, classe="preto", extra=""):
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head>
<body class="{classe}" data-size="1080x1920">
<svg width="0" height="0" style="position:absolute"><defs>{DEFS}{ICONS}</defs></svg>
{extra}
<div class="safe">{conteudo}</div>
</body></html>
"""


def passo(n, titulo, corpo, ui=""):
    return page(f"""{top(f"Como funciona · {n:02d}/{TOTAL:02d}")}
<div class="mid">
  <div class="step"><span class="n">{n:02d}</span><span class="l">PASSO</span></div>
  <div class="title">{titulo}</div>
  {ui}
  <div class="body">{corpo}</div>
</div>
{FOOT}""")


DEG = '<span class="deg"><i></i><i></i><i></i></span>'

STORIES = []

# 01 · capa
# Celular desenhado sobre bloco azul. Se existir print-app.png (print real do app) nesta pasta,
# ele aparece na tela; senão entra a tela desenhada no padrão da marca.
PW, PH, PB = 360, 740, 12  # largura, altura e borda do celular
if os.path.exists(os.path.join(AQUI, "print-app.png")):
    TELA_APP = '<img src="print-app.png" alt="" style="width:100%;height:100%;object-fit:cover;object-position:top">'
else:
    k = (PW - 2 * PB) / 210
    TELA_APP = f"""<div style="width:210px;height:{(PH - 2 * PB) / k:.0f}px;transform:scale({k:.3f});transform-origin:0 0;font-family:Inter;color:#fff;padding:30px 14px">
  <div style="display:flex;align-items:center;gap:6px"><svg viewBox="0 0 690 548" style="height:16px;width:auto;fill:#36BFEC"><use href="#fal"/></svg><span class="wm" style="font-size:11px">PEREGR<span class="i">I</span>NUS</span></div>
  <div style="font-family:Anton;font-size:30px;line-height:.9;margin-top:24px">TREINOU?<br><span style="color:#36BFEC">POSTA.</span></div>
  <div style="margin-top:14px;height:110px;background:#222;border-radius:2px;position:relative;overflow:hidden"><img src="falcao-voo.jpg" style="width:100%;height:100%;object-fit:cover;filter:grayscale(1)"><span style="position:absolute;left:5px;bottom:5px;background:#000;font-family:'Space Mono';font-size:7px;letter-spacing:.1em;padding:2px 4px;font-weight:700">JORNADA <b style="color:#36BFEC">047</b></span></div>
  <div style="display:flex;gap:4px;margin-top:12px;font-family:'Space Mono';font-size:6.5px;letter-spacing:.08em"><span style="background:#36BFEC;color:#000;padding:3px 5px;font-weight:700">CORRIDA</span><span style="border:1px solid #555;padding:2px 5px">PEDAL</span><span style="border:1px solid #555;padding:2px 5px">ACADEMIA</span></div>
  <div style="margin-top:12px;border-top:1px solid #333;padding-top:10px;display:flex;justify-content:space-between;font-family:'Space Mono';font-size:6.5px;letter-spacing:.1em;color:#888"><span>DURAÇÃO</span><span style="color:#fff">1H 05MIN</span></div>
  <div style="margin-top:6px;display:flex;justify-content:space-between;font-family:'Space Mono';font-size:6.5px;letter-spacing:.1em;color:#888"><span>DISTÂNCIA</span><span style="color:#fff">10,2 KM</span></div>
  <div style="margin-top:14px;background:#36BFEC;color:#000;font-family:'Space Mono';font-weight:700;font-size:8px;letter-spacing:.12em;padding:8px 9px">REGISTRAR TREINO &gt;&gt;&gt;</div>
</div>"""
CELULAR = f"""<div style="position:absolute;left:{(1080 - PW) / 2 + 60:.0f}px;top:330px;width:{PW}px;height:{PH}px;background:#000;border-radius:54px;padding:{PB}px;transform:rotate(-7deg);box-shadow:0 0 0 2px #888">
  <div style="width:100%;height:100%;border-radius:42px;overflow:hidden;background:#000;position:relative">{TELA_APP}
    <div style="position:absolute;left:50%;top:12px;width:90px;height:26px;margin-left:-45px;background:#000;border-radius:14px"></div></div>
</div>"""
STORIES.append(page(f"""<div class="capa">{top("App do club")}</div>
<div class="mid" style="justify-content:flex-end;padding-bottom:40px">
  <div class="eyebrow">Passo a passo, em oito telas.</div>
  <div class="title" style="font-size:150px">O club no seu <em>celular.</em></div>
  <div class="body">Treino, ranking, comunidade e encontros num lugar só. Segue as próximas telas.</div>
</div>
{FOOT}""", extra=f'<div style="position:absolute;left:0;top:0;width:1080px;height:1060px;background:#36BFEC;z-index:0"></div><div style="position:absolute;inset:0;z-index:1">{CELULAR}</div>'))

# 02 · entrar
STORIES.append(passo(1, "Entre pelo <em style=\"white-space:nowrap\">e-mail.</em>",
    "Abra <b>pgrns.vercel.app</b>, digite seu e-mail e use o código de 6 números que chega na caixa de entrada. No primeiro acesso, coloque o código de convite do grupo e seu nome.",
    """<div class="ui">
  <div class="lab">E-mail</div><div class="field">voce@email.com</div>
  <div class="lab" style="margin-top:30px">Código de 6 números</div>
  <div class="code"><span class="on">4</span><span class="on">8</span><span class="on">2</span><span></span><span></span><span></span></div>
</div>"""))

# 03 · instalar
STORIES.append(passo(2, "Instale <em>sem loja.</em>",
    "Depois é só abrir pelo ícone do falcão, em tela cheia, como qualquer app.",
    """<div class="row" style="margin-top:52px">
  <div class="col"><div class="lab mono" style="font-size:20px;color:var(--grey);margin-bottom:10px">Safari</div><h4>IPHONE</h4><ol><li>Toque em Compartilhar</li><li>Adicionar à Tela de Início</li></ol></div>
  <div class="col"><div class="lab mono" style="font-size:20px;color:var(--grey);margin-bottom:10px">Chrome</div><h4>ANDROID</h4><ol><li>Toque no menu ⋮</li><li>Instalar app</li></ol></div>
</div>"""))

# 04 · check-in
STORIES.append(passo(3, "Treinou? <em>Posta.</em>",
    "Na aba <b>TREINO</b>: foto, modalidade e tempo. Só vale foto tirada nas últimas 18 horas. Cada treino vira uma <b>JORNADA</b> com número.",
    """<div class="ui" style="padding:26px">
  <div class="photo"><img src="falcao-voo.jpg" alt=""><span class="stamp">JORNADA <em>047</em></span></div>
  <div class="chips" style="margin-top:24px"><span class="chip on">CORRIDA</span><span class="chip">PEDAL</span><span class="chip">ACADEMIA</span><span class="chip">VÔLEI</span><span class="chip">TRILHA</span><span class="chip">+5</span></div>
  <div class="bt" style="margin-top:24px"><span>Registrar treino</span><svg><use href="#chev"/></svg></div>
</div>"""))

# 05 · mínimos
STORIES.append(passo(4, "O mínimo <em>que vale.</em>",
    "Abaixo disso o treino não entra. As outras modalidades valem a partir de 20 minutos.",
    """<div class="list">
  <div><span class="k">CORRIDA</span><span class="v">3 KM OU 30 MIN</span></div>
  <div><span class="k">PEDAL</span><span class="v">5 KM</span></div>
  <div><span class="k">CAMINHADA</span><span class="v">8 KM</span></div>
  <div><span class="k">ACADEMIA</span><span class="v">30 MIN</span></div>
</div>"""))

# 06 · pontos
STORIES.append(passo(5, "Cada treino, <em>1 ponto.</em>",
    "Até 3 pontos por dia. O ranking da semana zera toda segunda. A temporada dura 45 dias e vale medalha.",
    """<div class="row" style="margin-top:52px">
  <div class="col" style="text-align:left"><div class="lab mono" style="font-size:20px;color:var(--grey)">Por dia</div><div style="font-family:Anton;font-size:150px;line-height:1;color:var(--blue)">3</div><div class="mono" style="font-size:20px;color:#cfcfcf">pontos no máximo</div></div>
  <div class="col"><div class="lab mono" style="font-size:20px;color:var(--grey)">Semana</div><div style="font-family:Anton;font-size:150px;line-height:1">SEG</div><div class="mono" style="font-size:20px;color:#cfcfcf">ranking zera</div></div>
  <div class="col"><div class="lab mono" style="font-size:20px;color:var(--grey)">Temporada</div><div style="font-family:Anton;font-size:150px;line-height:1">45</div><div class="mono" style="font-size:20px;color:#cfcfcf">dias</div></div>
</div>"""))

# 07 · comunidade
STORIES.append(passo(6, "O grupo <em>vê tudo.</em>",
    "Em <b>COMUNIDADE</b>, o mural mostra o treino de todo mundo na hora. Dá para reagir, comentar e seguir quem treina com você.",
    """<div class="ui">
  <div class="chips"><span class="chip on">TODOS</span><span class="chip">SEGUINDO</span></div>
  <div style="display:flex;align-items:center;gap:20px;margin-top:30px">
    <svg viewBox="0 0 690 548" style="width:74px;height:74px;fill:var(--blue);background:#1c1c1c;border-radius:50%;padding:14px"><use href="#fal"/></svg>
    <div><div style="font-weight:600;font-size:32px">Nome do membro</div><div class="mono" style="font-size:20px;color:var(--grey)">CORRIDA · JORNADA 012</div></div>
  </div>
  <div style="display:flex;gap:40px;margin-top:30px;padding-top:24px;border-top:1.5px solid var(--line)">
    <span style="display:flex;align-items:center;gap:12px;color:var(--blue)" class="mono"><svg class="ic"><use href="#fire"/></svg><b style="font-size:24px">REAGIR</b></span>
    <span style="display:flex;align-items:center;gap:12px;color:#cfcfcf" class="mono"><svg class="ic"><use href="#msg"/></svg><b style="font-size:24px">COMENTAR</b></span>
  </div>
</div>"""))

# 08 · encontros
STORIES.append(passo(7, "Marque <em>presença.</em>",
    "No <b>CALENDÁRIO</b> estão os encontros do club. Toque em <b>VOU</b> e seu nome entra na lista. Qualquer membro pode criar um encontro.",
    """<div class="ui">
  <div class="lab">Encontro</div>
  <div style="font-family:Anton;font-size:64px;line-height:1">TREINO EM GRUPO</div>
  <div class="mono" style="font-size:22px;color:#cfcfcf;margin-top:16px">DIA · HORÁRIO · LOCAL</div>
  <div class="bt" style="margin-top:30px"><span>VOU</span><svg><use href="#chev"/></svg></div>
</div>"""))

# 09 · e mais
STORIES.append(passo(8, "E tem <em>mais.</em>",
    "Tudo dentro do mesmo app.",
    f"""<div class="feat">
  <div>{DEG}<div><h5>Hábitos</h5><p>Sono, água, leitura e outros, marcados no PERFIL.</p></div></div>
  <div>{DEG}<div><h5>Plano de treino</h5><p>Envie o plano do treinador e compare o feito com o planejado.</p></div></div>
  <div>{DEG}<div><h5>Story do treino</h5><p>Seu check-in vira story pronto para o Instagram.</p></div></div>
  <div>{DEG}<div><h5>Loja</h5><p>Peças do club na sacola do topo, pedido pelo WhatsApp.</p></div></div>
</div>"""))

# 10 · convite final (azul)
STORIES.append(page(f"""{top("Bora junto")}
<div class="mid" style="justify-content:flex-end;padding-bottom:40px">
  <div class="title" style="font-size:150px">Seu esporte.<br>Seu ritmo.<br>Sua <em>jornada.</em></div>
  <div class="body">Ainda não entrou? Peça o código de convite no direct e comece hoje.</div>
  <div style="display:inline-flex;align-self:flex-start;align-items:center;gap:22px;margin-top:48px;background:#000;color:var(--blue);font-family:'Space Mono',monospace;font-weight:700;font-size:30px;letter-spacing:.16em;padding:26px 36px;text-transform:uppercase">pgrns.vercel.app <svg style="width:84px;height:28px"><use href="#chev"/></svg></div>
</div>
{FOOT}""", classe="azul"))

for i, html in enumerate(STORIES, 1):
    with open(os.path.join(AQUI, f"story-{i:02d}.html"), "w", encoding="utf-8") as f:
        f.write(html)
print(len(STORIES), "stories")
