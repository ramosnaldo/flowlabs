# Manual de marca · Villas Cavaliere · Identidade Visual 2.0

Versão 2.0, outubro 2026. Responsável: FLOW Labs. Este arquivo transcreve o
manual de handoff completo.

## Logo

O símbolo de quatro volutas faz referência à lapela do noivo. Na assinatura,
CAVALIERE é o protagonista em peso fino (Yanone 200) e VILLAS fica pequeno, bem
espaçado (Yanone 300) e colorido.

| Versão | Fundo | Cores |
| --- | --- | --- |
| Horizontal principal | Linho, Off-white, Areia | Símbolo em gradiente Azul Cavaliere → Marinho, fio e VILLAS em Azul Cavaliere, CAVALIERE em Noite |
| Horizontal negativa | Noite, Black Tie, Marinho | Símbolo em gradiente Off-white → Tiffany, fio em Cinza, VILLAS em Tiffany, CAVALIERE em Off-white |
| Vertical | Espaços estreitos, etiquetas, capas | Símbolo em cima, VILLAS e CAVALIERE centralizados embaixo |
| Símbolo isolado | Avatar, favicon, selo, carimbo | Qualquer versão |

- **Área de proteção:** em volta da assinatura, no mínimo metade da altura do
  símbolo. Nada de texto, borda ou foto dentro dessa margem.
- **Tamanho mínimo:** horizontal 120 px de largura na tela, 30 mm no impresso;
  vertical 80 px, 20 mm; símbolo 16 px, 5 mm. Abaixo disso, versão chapada sem
  gradiente.
- **Uma cor só:** bordado, carimbo, hot stamping e serigrafia de uma cor usam
  as versões monocromáticas em Black Tie ou Off-white. O gradiente do símbolo
  é só para tela e impressão em 4 cores.
- **Não fazer:** distorcer ou achatar; cores fora da paleta, como os terrosos
  da versão antiga; sombra, brilho ou contorno; fundo sem contraste.

## Cores

Bases profundas, um azul de assinatura e acentos frios. Nenhum tom terroso. Os
valores CMYK são referência para a gráfica: peça prova de cor antes de imprimir
tiragem.

| Nome | Papel | HEX | RGB | CMYK |
| --- | --- | --- | --- | --- |
| Noite | Base escura · 40% | #0F1E25 | 15 30 37 | 80 55 50 70 |
| Azul Marinho | Base · 15% | #1B2A4A | 27 42 74 | 100 85 35 35 |
| Azul Cavaliere | Assinatura e luz · 10% | #5394A9 | 83 148 169 | 68 25 22 2 |
| Black Tie | Contraste, fundo de post | #121417 | 18 20 23 | 70 60 55 85 |
| Linho | Fundo claro · 25% | #EFEBE5 | 239 235 229 | 5 5 8 0 |
| Areia | Neutro · 6% | #D6D1CA | 214 209 202 | 15 13 17 0 |
| Azul Tiffany | Acento | #81D8D0 | 129 216 208 | 47 0 24 0 |
| Cinza | Acento | #8E9196 | 142 145 150 | 45 35 30 5 |
| Off-white | Acento claro | #F7F5F0 | 247 245 240 | 2 2 5 0 |

Proporção de uso: Noite 40%, Linho 25%, Marinho 15%, Azul Cavaliere 10%,
Areia 6%, acentos 4%.

| Combinação | Contraste | Uso |
| --- | --- | --- |
| Linho sobre Black Tie | 15.5 : 1 | Títulos e corpo em fundo escuro |
| Tiffany sobre Black Tie | 11.1 : 1 | Sobretítulo, botão, detalhes |
| Noite sobre Linho | 14.3 : 1 | Texto em fundo claro |
| Azul Cavaliere sobre Linho | 2.9 : 1 | Só elementos grandes e decorativos (VILLAS na assinatura, fios). Nunca texto de leitura |
| Azul Cavaliere sobre Noite | 5.0 : 1 | Fios, ícones, texto de apoio |

## Gradientes e grão

Sempre radiais, com a luz vindo de um canto e indo para a sombra, como um terno
sob a luz do provador. Nunca gradiente linear chapado. O grão fino vai por cima
de tudo, inclusive das fotos.

| Nome | Uso | Token |
| --- | --- | --- |
| Lapela | Principal. Azul Cavaliere, Marinho, Noite | `--vc-grad-lapela` |
| Black Tie | Feed e posts. Brilho azul a 32% no canto | `--vc-grad-black-tie` |
| Neblina | Campanhas, eventos, stories | `--vc-grad-neblina` |
| Linho | Fundos claros, papelaria | `--vc-grad-linho` |

Grão em HTML (último filho de um container com `position: relative`):

```html
<svg style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;
            opacity:.30;mix-blend-mode:overlay">  <!-- fundo claro: opacity .45, multiply -->
  <filter id="vcg">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
  </filter>
  <rect width="100%" height="100%" filter="url(#vcg)"/>
</svg>
```

Com `tokens.css`, basta a classe `.vc-grao` (e `.vc-grao--claro` no claro).

- **Grão no Photoshop:** Adicionar Ruído 4 a 8%, Gaussiano, monocromático, em
  camada cinza 50% no modo Sobrepor. Em fundo claro, Multiplicar.
- **Padrão tom sobre tom:** o símbolo repetido como textura, 8 a 15% de
  opacidade, na mesma família de cor do fundo. Etiqueta, forro, convite, verso
  de cartão.

## Tipografia

Duas famílias gratuitas do Google Fonts, licença OFL, uso comercial liberado.

- **Yanone Kaffeesatz 200 e 300:** títulos, sempre em caixa alta, espaçamento
  +6%. Peso 200 em tamanhos grandes, 300 abaixo de 40 px.
- **Hanken Grotesk 300 e 400:** corpo em 300, entrelinha 1.6. Sobretítulos em
  400, caixa alta, espaçamento +32%.

| Estilo | Fonte | Post 1080 | Web | Impresso |
| --- | --- | --- | --- | --- |
| Título | Yanone 200, caixa alta, +6%, entrelinha 0.95 | 120–150 px | 48–84 px | 40 pt ou mais |
| Subtítulo | Yanone 300, caixa alta, +6% | 64–76 px | 26–34 px | 18–24 pt |
| Sobretítulo | Hanken 400, caixa alta, +32% | 22–28 px | 12–13 px | 8–9 pt |
| Corpo | Hanken 300, entrelinha 1.6 | 32–36 px | 16–17 px | 10–12 pt |
| Rodapé e legenda | Hanken 300 ou 400 | 20–26 px | 12–13 px | 7–8 pt |

```html
<link href="https://fonts.googleapis.com/css2?family=Yanone+Kaffeesatz:wght@200;300&family=Hanken+Grotesk:wght@300;400&display=swap" rel="stylesheet">
```

```css
--vc-font-display: 'Yanone Kaffeesatz', 'Arial Narrow', sans-serif;
--vc-font-texto:   'Hanken Grotesk', 'Helvetica Neue', Arial, sans-serif;
```

## Componentes

O mesmo conjunto aparece no site, no link da bio e nos posts.

**Botão contornado** (`.vc-botao`, variantes `--tiffany` e `--claro`)
- Altura mínima 44 px, raio total, borda 1 px
- Hover: preenche com a cor da borda, texto vira Noite, 200 ms ease-out
- Foco do teclado: contorno Tiffany de 2 px, afastado 3 px
- Desativado: 40% de opacidade, sem hover
- Texto do CTA: "Agendar horário exclusivo" ou "Falar com um consultor"

**Bloco de título**
- Sobretítulo Tiffany no escuro. No claro, Azul Cavaliere só a partir de
  24 px; abaixo disso, Marinho
- Título em até 3 linhas. Se passar, reduza a fonte, não corte o texto
- Fio de 56 a 80 px abaixo, 1 px (`.vc-fio`)

**Rodapé de peça**
- Assinatura à esquerda, @villascavaliere à direita, alinhados pelo centro
- Topo da peça: categoria à esquerda, contagem 01 / 06 à direita

## Formatos de Instagram

Margem de segurança de 96 px em todos os formatos.

| Formato | Tamanho | Observação |
| --- | --- | --- |
| Post e carrossel | 1080 × 1350 px · 4:5 | Margem 96 |
| Story e Reels | 1080 × 1920 px | Livre 250 px no topo e 340 px embaixo (interface do app) |
| Quadrado | 1080 × 1080 px | Anúncios e grade antiga |
| Foto de perfil | 1080 × 1080 px | Símbolo centralizado com 40% da altura |

## Fotografia

- **Cena:** homens de traje, luz baixa, fim de tarde ou noite, fundo escuro ou
  desfocado. Uma pessoa por imagem. Detalhes que vendem: lapela, abotoadura,
  mãos ajustando o paletó, giz e fita métrica.
- **Tratamento:** preto e branco frio ou duotone de Noite para Linho, sempre
  com o grão por cima. Nas capas, a foto ocupa a metade de baixo e escurece até
  o Black Tie onde fica o título.
- **Evitar:** luz chapada de estúdio, fundo branco, filtros quentes, tons de
  pele alaranjados, sorriso posado para a câmera, montagem com várias pessoas.

## Ainda falta

- Referência Pantone das cores: pedir à gráfica a partir da prova de cor CMYK
- Telefone e link de WhatsApp oficiais para cartão e contracapa
- Banco de fotos aprovado seguindo a direção de imagem
