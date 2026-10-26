---
name: villas-cavaliere-brand
description: >-
  Aplica a identidade visual 2.0 da Villas Cavaliere (alfaiataria e trajes de
  noivo) em qualquer peça: posts, carrosséis e stories de Instagram, páginas
  web, link da bio, convites, cartões e papelaria. Traz logos em SVG, tokens de
  cor e tipografia, fontes e templates HTML prontos. Use sempre que o pedido
  envolver a Villas Cavaliere, @villascavaliere, "VC", ou quando o usuário pedir
  algo "na marca", "no padrão da Villas" ou "com a identidade da Cavaliere".
---

# Villas Cavaliere · marca

Tudo o que for feito para a Villas Cavaliere sai desta skill: os arquivos em
`assets/` são a fonte da verdade, e as regras completas estão em
`references/manual.md`. Leia o manual antes da primeira peça da conversa.

A marca é sóbria e fria: bases profundas, um azul de assinatura, luz radial
vinda de um canto, grão fino por cima de tudo, títulos finos em caixa alta.
Se a peça parecer quente, colorida, chapada ou "animada", está fora da marca.

## Arquivos

| Caminho | O que é |
| --- | --- |
| `assets/01-logos/svg/vc-{forma}-{versao}.svg` | Logos com texto em curvas. Formas: `horizontal`, `vertical`, `assinatura` (só texto), `simbolo`. Versões: `principal` (fundo claro), `negativa` (fundo escuro), `mono-blacktie`, `mono-offwhite` |
| `assets/01-logos/vc-avatar-instagram-1080.png` | Foto de perfil pronta |
| `assets/02-tokens/tokens.css` | Variáveis `--vc-*`, gradientes, grão (`.vc-grao`) e classes `.vc-titulo`, `.vc-subtitulo`, `.vc-sobretitulo`, `.vc-corpo`, `.vc-botao`, `.vc-fio` |
| `assets/02-tokens/tokens.json` | Os mesmos valores, com RGB e CMYK |
| `assets/03-fontes/` | Yanone Kaffeesatz 200/300, Hanken Grotesk 300/400 (OFL) e `fontes.css` |
| `assets/04-templates-instagram/` | `post.html`, `carrossel.html`, `story.html` com `templates.css` e `templates.js` |
| `scripts/exportar-templates.mjs` | Exporta cada `.peca` dos templates como PNG em tamanho real |

## Como fazer cada tipo de peça

**Instagram (post, carrossel, story).** Copie o template mais próximo para a
pasta de trabalho junto com `01-logos`, `02-tokens`, `03-fontes` (os caminhos
são relativos: `../01-logos/...`), troque os textos e, se houver foto, use
`style="--foto:url(foto.jpg)"` no `.foto`. Monte cada lâmina como um
`<article class="peca" style="--w:1080;--h:1350">`. Exporte com
`node scripts/exportar-templates.mjs <saida>` (Playwright) e confira os PNGs
antes de entregar. Para a escrita (gancho, legenda, sequência), as skills
`ig-*` cuidam do texto; esta cuida do visual.

**Página web ou link da bio.** Carregue as fontes (Google Fonts ou
`fontes.css`) e `tokens.css`, e use as variáveis e classes dele em vez de
valores soltos. Fundo escuro em `--vc-grad-black-tie` ou `--vc-grad-lapela`
com `.vc-grao`; CTA com `.vc-botao`; logo com a versão `negativa`.

**Impresso e papelaria.** Use os valores CMYK de `tokens.json` e avise que a
gráfica precisa de prova de cor (ainda não há Pantone). Para uma cor só
(bordado, hot stamping, carimbo), só as versões `mono-*`.

## Regras que não podem falhar

1. **Só a paleta.** Noite `#0F1E25`, Marinho `#1B2A4A`, Azul Cavaliere
   `#5394A9`, Black Tie `#121417`, Linho `#EFEBE5`, Areia `#D6D1CA`, Tiffany
   `#81D8D0`, Cinza `#8E9196`, Off-white `#F7F5F0`. Nenhum tom terroso.
2. **Logo certo para o fundo.** `principal` em Linho/Off-white/Areia,
   `negativa` em Noite/Black Tie/Marinho. Área livre em volta: metade da
   altura do símbolo. Mínimos: horizontal 120 px / 30 mm, vertical 80 px /
   20 mm, símbolo 16 px / 5 mm. Nunca distorcer, recolorir, pôr sombra ou
   contorno, nem usar sobre fundo sem contraste. Nunca redesenhar o logo em
   texto: use o SVG.
3. **Gradientes sempre radiais**, luz de um canto para a sombra. Nunca
   linear chapado. Grão por cima de tudo, inclusive das fotos (escuro: 30%
   overlay; claro: 45% multiply).
4. **Tipografia.** Títulos em Yanone Kaffeesatz 200 (300 abaixo de 40 px),
   caixa alta, +6%, entrelinha 0.95, no máximo 3 linhas: se passar, reduza a
   fonte, não corte o texto. Corpo em Hanken Grotesk 300, entrelinha 1.6.
   Sobretítulo em Hanken 400, caixa alta, +32%.
5. **Contraste.** Azul Cavaliere sobre Linho (2.9:1) só em elementos grandes
   e decorativos, nunca em texto de leitura. Sobretítulo no claro: Azul
   Cavaliere a partir de 24 px, Marinho abaixo disso. No escuro: Tiffany.
6. **Instagram.** Margem de 96 px em tudo. Story: nada importante nos 250 px
   do topo nem nos 340 px de baixo. Topo da peça: categoria à esquerda,
   contagem `01 / 06` à direita. Rodapé: assinatura à esquerda, `@villascavaliere`
   à direita.
7. **CTA** só "Agendar horário exclusivo" ou "Falar com um consultor".
8. **Foto.** Homens de traje, luz baixa, fundo escuro, uma pessoa por imagem,
   P&B frio ou duotone Noite→Linho. Nas capas, a foto ocupa a metade de baixo
   e escurece até o Black Tie onde fica o título. Evite estúdio chapado,
   fundo branco, filtros quentes, sorriso posado, várias pessoas.

## Antes de entregar

Renderize a peça (Playwright) e olhe a imagem. Confira: cores só da paleta,
versão do logo certa para o fundo, títulos em até 3 linhas e dentro da margem,
nada nas faixas do story, grão aplicado, CTA com um dos dois textos. Se faltar
um dado que a marca ainda não tem (Pantone, WhatsApp oficial, fotos
aprovadas), deixe um marcador visível e diga ao usuário.

O guia completo publicado fica em `/villas-cavaliere/` no site do projeto, e
o pacote de origem em `villas-cavaliere-handoff/` no repositório flowlabs.
Depois de mudar o pacote, rode `villas-cavaliere-handoff/_fonte/sincronizar-skill.sh`.
