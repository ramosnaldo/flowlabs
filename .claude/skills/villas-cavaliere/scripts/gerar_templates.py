import sys
SK = sys.argv[1]
d = open(f'{SK}/assets/simbolo-path.txt').read()

CSS = """:root{--noite:#0F1E25;--marinho:#1B2A4A;--azul:#5394A9;--blacktie:#121417;--linho:#EFEBE5;--areia:#D6D1CA;--tiffany:#81D8D0;--cinza:#8E9196;--off:#F7F5F0;--m:96px}
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:__W__px;height:__H__px;overflow:hidden}
body{position:relative;font-family:"Hanken Grotesk",sans-serif;color:var(--linho);background:var(--blacktie)}
/* FUNDOS: troque a classe do .bg */
.bg{position:absolute;inset:0}
.bg.blacktie{background:radial-gradient(120% 90% at 100% 0%,rgba(83,148,169,.32) 0%,rgba(83,148,169,0) 55%),radial-gradient(140% 120% at 80% 10%,#1A1D21 0%,#121417 55%,#0B0C0E 100%)}
.bg.lapela{background:radial-gradient(110% 90% at 15% 8%,#5394A9 0%,#1B2A4A 45%,#0F1E25 100%)}
.bg.neblina{background:radial-gradient(110% 80% at 85% 95%,#F7F5F0 0%,#8E9196 40%,#1B2A4A 85%)}
.bg.linho{background:radial-gradient(120% 100% at 70% 0%,#EFEBE5 0%,#D6D1CA 55%,#81D8D0 120%)}
body.claro{color:var(--noite)}
.grain{position:absolute;inset:0;width:100%;height:100%;opacity:.07;mix-blend-mode:overlay;pointer-events:none}
.ghost{position:absolute;right:-140px;top:-120px;width:640px;opacity:.045}
.sym{display:block}
.safe{position:absolute;inset:var(--m);display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;font-size:26px;letter-spacing:.32em;text-transform:uppercase;opacity:.6}
.mid{flex:1;display:flex;flex-direction:column;justify-content:center}
.eyebrow{font-size:28px;letter-spacing:.32em;text-transform:uppercase;color:var(--tiffany);margin-bottom:28px}
body.claro .eyebrow{color:var(--azul)}
.title{font-family:"Yanone Kaffeesatz",sans-serif;font-weight:200;text-transform:uppercase;letter-spacing:.06em;font-size:136px;line-height:.98}
.num{font-family:"Yanone Kaffeesatz",sans-serif;font-weight:200;font-size:220px;line-height:.9;color:var(--tiffany);opacity:.9;margin-bottom:24px}
.rule{width:72px;height:2px;background:var(--azul);margin:44px 0 40px}
.body{font-size:36px;line-height:1.6;font-weight:300;max-width:820px;opacity:.88}
.foot{display:flex;justify-content:space-between;align-items:flex-end}
.lockup{display:flex;align-items:center;gap:22px}
.lockup .bar{width:1.5px;height:68px;background:rgba(239,235,229,.35)}
body.claro .lockup .bar{background:rgba(15,30,37,.3)}
.lockup .v{font-size:17px;letter-spacing:.62em;color:var(--azul);margin-bottom:2px}
.lockup .c{font-family:"Yanone Kaffeesatz",sans-serif;font-weight:200;font-size:52px;letter-spacing:.06em;line-height:1}
.handle{font-size:26px;letter-spacing:.04em;opacity:.8}
.btn{display:inline-block;border:1.5px solid currentColor;border-radius:999px;padding:22px 56px;font-size:26px;letter-spacing:.32em;text-transform:uppercase}"""

DEFS = f"""<svg width="0" height="0" style="position:absolute"><defs>
<path id="symp" fill-rule="evenodd" d="{d}"/>
<linearGradient id="g-light" x1="0.3" y1="0" x2="0.7" y2="1"><stop offset="0" stop-color="#EFEBE5"/><stop offset="1" stop-color="#81D8D0"/></linearGradient>
<linearGradient id="g-dark" x1="0.3" y1="0" x2="0.7" y2="1"><stop offset="0" stop-color="#5394A9"/><stop offset="1" stop-color="#1B2A4A"/></linearGradient>
<filter id="noise"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
</defs></svg>"""
GRAIN = '<svg class="grain"><rect width="100%" height="100%" filter="url(#noise)"/></svg>'
GHOST = '<svg class="ghost" viewBox="0 0 302 324"><use href="#symp" fill="#EFEBE5"/></svg>'
LOCKUP = ('<div class="lockup"><svg class="sym" viewBox="0 0 302 324" style="width:62px;height:66px">'
          '<use href="#symp" fill="url(#g-light)"/></svg><div class="bar"></div>'
          '<div><div class="v">VILLAS</div><div class="c">CAVALIERE</div></div></div>')
FOOT = f'<div class="foot">{LOCKUP}<div class="handle">@villascavaliere</div></div>'


def top(n):
    return f'<div class="top"><span>TRAJE DE NOIVO</span><span>{n}</span></div>'


def page(W, H, inner, bg='blacktie', ghost=True):
    head = ('<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8">\n'
            '<link href="https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz:wght@200;300;400'
            '&family=Hanken+Grotesk:wght@300;400;500&display=swap" rel="stylesheet">\n<style>\n'
            + CSS.replace('__W__', str(W)).replace('__H__', str(H)) + '\n</style></head>\n')
    return (head + f'<body data-size="{W}x{H}">\n'
            '<!-- Fundos: blacktie (feed padrão) | lapela | neblina | linho (em linho, use class="claro" no body) -->\n'
            + DEFS + f'\n<div class="bg {bg}"></div>\n' + (GHOST + '\n' if ghost else '')
            + GRAIN + '\n' + inner + '\n</body></html>\n')


T = {}
T['post.html'] = page(1080, 1350, f"""<!-- CAPA ou POST ESTÁTICO. Troque os textos. -->
<div class="safe">
  {top('01 / 06')}
  <div class="mid">
    <div class="eyebrow">COLEÇÃO 2027</div>
    <div class="title">O AZUL QUE<br>VESTE O SIM.</div>
    <div class="rule"></div>
    <div class="body">Cada traje começa numa conversa.</div>
  </div>
  {FOOT}
</div>""")
T['post-conteudo.html'] = page(1080, 1350, f"""<!-- SLIDE DE CONTEÚDO de carrossel: um ponto por slide. -->
<div class="safe">
  {top('02 / 06')}
  <div class="mid">
    <div class="num">01</div>
    <div class="title" style="font-size:112px">ESCOLHER PELA<br>FOTO DO PINTEREST.</div>
    <div class="rule"></div>
    <div class="body">O traje da foto foi feito para outro corpo, outra luz e outro casamento. O seu precisa vestir você.</div>
  </div>
  {FOOT}
</div>""")
T['post-cta.html'] = page(1080, 1350, f"""<!-- ÚLTIMO SLIDE (CTA). -->
<div class="safe">
  {top('06 / 06')}
  <div class="mid" style="align-items:center;text-align:center">
    <svg class="sym" viewBox="0 0 302 324" style="width:150px;height:161px;margin-bottom:56px"><use href="#symp" fill="url(#g-light)"/></svg>
    <div class="eyebrow">AGENDA ABERTA</div>
    <div class="title" style="font-size:120px">COMENTE<br>TRAJE.</div>
    <div class="rule" style="margin:44px auto 40px"></div>
    <div class="body">A gente te chama para agendar um horário exclusivo com um consultor.</div>
  </div>
  <div class="foot" style="justify-content:center"><div class="handle">@villascavaliere</div></div>
</div>""", bg='lapela', ghost=False)
T['post-foto.html'] = page(1080, 1350, f"""<!-- CAPA COM FOTO. Coloque a foto na mesma pasta como foto.jpg. P&B frio com toque azul; ajuste object-position para enquadrar. -->
<img src="foto.jpg" onerror="this.style.display='none'" style="position:absolute;left:0;right:0;bottom:0;top:30%;width:100%;height:70%;object-fit:cover;object-position:center 15%;filter:grayscale(1) contrast(1.08) brightness(.82);-webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 35%);mask-image:linear-gradient(180deg,transparent 0%,#000 35%)">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,#0B0C0E 0%,rgba(11,12,14,.92) 30%,rgba(11,12,14,.15) 58%,rgba(11,12,14,.25) 82%,rgba(11,12,14,.85) 100%)"></div>
<div style="position:absolute;inset:0;background:#5394A9;mix-blend-mode:color;opacity:.18"></div>
{GRAIN}
<div class="safe">
  {top('01 / 09')}
  <div style="margin-top:72px">
    <div class="eyebrow">ANTES DO GRANDE DIA</div>
    <div class="title" style="font-size:116px">5 ERROS DO NOIVO<br>NO TRAJE.</div>
    <div class="rule"></div>
    <div class="body">Antes de escolher o seu, passa por aqui.</div>
  </div>
  <div style="flex:1"></div>
  {FOOT}
</div>""", ghost=False)
T['story.html'] = page(1080, 1920, """<!-- STORY 1080x1920. Zona segura: 250px livres em cima e embaixo. -->
<div class="safe" style="inset:250px var(--m)">
  <div class="mid" style="align-items:center;text-align:center">
    <svg class="sym" viewBox="0 0 302 324" style="width:110px;height:118px;margin-bottom:72px"><use href="#symp" fill="url(#g-light)"/></svg>
    <div class="eyebrow">AGENDA ABERTA</div>
    <div class="title" style="font-size:150px">PROVA COM<br>HORA MARCADA</div>
    <div class="rule" style="margin:56px auto"></div>
    <div class="body" style="margin-bottom:72px">Seu traje escolhido com calma, ao lado de um consultor.</div>
    <div class="btn">AGENDAR</div>
  </div>
  <div class="foot" style="justify-content:center"><div class="handle">@villascavaliere</div></div>
</div>""", bg='neblina', ghost=False)

for k, v in T.items():
    open(f'{SK}/templates/{k}', 'w', encoding='utf-8').write(v)
print(list(T))
