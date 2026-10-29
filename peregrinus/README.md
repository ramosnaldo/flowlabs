# PEREGRINUS Club Esportivo · Brand kit 2.0

Pasta de criação da PEREGRINUS. O app do clube fica em outro repositório (`ramosnaldo/pgrns`).
Este README resume as regras do manual (`Manual-Handoff-Peregrinus.pdf` / `guia-handoff.html`). Na dúvida, o manual manda.

Versão: brand kit 2.0, aprovado em 11/10/2026 (ver `02-tokens/tokens.json`).

## O que tem aqui

| Pasta | Conteúdo |
|---|---|
| `00-prancha-logos.png` | Visão geral de todas as versões da logo |
| `guia-handoff.html` / `Manual-Handoff-Peregrinus.pdf` | Manual completo (10 páginas) |
| `01-logos/` | `svg/` (texto em curvas), `pdf-vetor/` (gráfica), `png/` (transparente, 2400 px), `3d/` (qb 3D + original do cliente) |
| `02-tokens/` | `tokens.css` e `tokens.json`: cores, fontes, escala e grade |
| `03-fontes/` | Anton, Inter, Instrument Serif, Space Mono + licenças OFL |
| `04-templates-instagram/` | post, post-foto, post-conteudo, post-cta, treino, story (HTML → exportar PNG) |
| `05-imagens/` | Fotos P&B do falcão (retrato, voo, recorte) |
| `06-elementos-graficos/` | degraus, globo, setas, mira, rota, topografia, velocidade + `icones/` |

## Logo

### Versões e quando usar

Escolha a versão pela cor do fundo, não pelo gosto. Os arquivos têm o mesmo nome em `svg/`, `pdf-vetor/` e `png/`.

| Versão | Arquivo | Onde usar |
|---|---|---|
| Horizontal principal | `peregrinus-horizontal-principal` | Fundo claro |
| Horizontal negativa | `peregrinus-horizontal-negativa` | Fundo escuro |
| Mono preto | `peregrinus-horizontal-mono-preto`, `peregrinus-vertical-mono-preto` | Sobre azul ou impressão em 1 cor |
| Mono branco | `peregrinus-horizontal-mono-branco`, `peregrinus-vertical-mono-branco` | Sobre foto ou cinza |
| Vertical | `peregrinus-vertical-principal`, `peregrinus-vertical-negativa` | Peito de camiseta, selos, boné |
| Lettering | `peregrinus-lettering-azul`, `-preto`, `-branco` | Costas, mangas, faixas |
| Símbolo qb | `peregrinus-simbolo-qb-azul`, `-preto`, `-branco` | Símbolo principal |
| Falcão em P | `peregrinus-falcao-p-azul`, `-preto`, `-branco` | Favicon, ícone de app, crachá, chaveiro, medalha, patch |
| Avatar | `peregrinus-avatar-instagram` | Foto de perfil do Instagram |

Formatos: `svg/` para tela, Figma, Illustrator e Corel; `pdf-vetor/` para gráfica; `png/` (fundo transparente, lado maior com 2400 px) para quem não abre vetor. O qb 3D (`3d/`) é peça especial, não substitui o símbolo chapado.

### Símbolos

- **qb (principal):** desenho do cliente. Um P em pé e um P girado, hastes lado a lado, três degraus em cada haste. É igual de cabeça para baixo (180°). Mínimo **32 px** na tela e **15 mm** em bordado. Abaixo disso, use o falcão em P.
- **Falcão em P (secundário):** desenho do cliente. As três asas repetem os três degraus do qb; a cabeça é vazada, então no fundo preto aparece como no original.
- Os dois são desenhos do cliente: **nunca redesenhar**, sempre usar os arquivos de `01-logos/`.

### Assinatura

- PEREGRINUS em Anton, espaçamento +50, com o **I cortado na diagonal**. CLUB ESPORTIVO em Space Mono espaçado, embaixo.
- Nos arquivos o texto já está em curvas. Para compor em HTML, use a classe `.pg-wm` de `tokens.css`:

```html
<span class="pg-wm">PEREGR<span class="i">I</span>NUS</span>
```

### Proibido

Distorcer, girar o qb a 90°, aplicar neon ou brilho, sair da paleta, reordenar símbolo e nome.

## Cores

Uma cor de assinatura e três neutros.

| Papel | Nome | HEX | RGB | CMYK | Pantone (ref.) | Proporção |
|---|---|---|---|---|---|---|
| Principal | Azul Peregrino | `#36BFEC` | 54 191 236 | 77 19 0 7 | 298 C | 20% |
| Base | Preto | `#000000` | 0 0 0 | 60 40 40 100 | Black 6 C | 45% |
| Apoio | Cinza | `#888888` | 136 136 136 | 0 0 0 47 | Cool Gray 8 C | 10% |
| Respiro | Cinza claro | `#D6D6D6` | 214 214 214 | 0 0 0 16 | Cool Gray 1 C | 25% |
| Texto sobre preto | Branco | `#FFFFFF` | 255 255 255 | | | |
| Texto azul sobre claro | Azul de apoio | `#1A7FA6` | | | | só texto |

### Combinações aprovadas

| Fundo | Texto | Destaque |
|---|---|---|
| Preto (padrão) | Branco | Azul `#36BFEC` |
| Azul `#36BFEC` | Preto | Branco |
| Cinza claro `#D6D6D6` | Preto | Azul de apoio `#1A7FA6` |

- Texto azul sobre fundo claro usa sempre o azul de apoio `#1A7FA6`: o `#36BFEC` não tem contraste para leitura.
- Fundos chapados. Sem gradiente colorido, sem neon, sem brilho.
- Sem turquesa `#65CFC4` (versão antiga) e sem ciano `#00F9E7` (primeira camiseta, anterior ao kit 2.0). Novas peças de vestuário seguem o azul `#36BFEC`.

## Tipografia

Quatro fontes, todas do Google Fonts com licença OFL (arquivos em `03-fontes/`). Elas substituem Druk, DIN Condensed e PP Editorial das referências antigas.

| Papel | Fonte | Regra |
|---|---|---|
| Títulos | **Anton** | Caixa alta, entrelinha 0,86 a 0,95. Chamadas, números de evento, lettering |
| Destaque editorial | **Instrument Serif itálico** | Uma frase por peça, no máximo |
| Texto e interface | **Inter** 400, 500, 600, 700 | Legendas, site, app. Entrelinha 1,5 |
| Dados e rótulos | **Space Mono** | Caixa alta, espaçamento +100 a +140. Horários, distâncias, coordenadas, numeração |

Escala de referência no post (1080 px de largura): título 150 px (título longo 110 px), número de destaque 300 px, frase editorial 54 px, corpo 34 px, rótulo 22 px.

Para usar na web:

```html
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link href="02-tokens/tokens.css" rel="stylesheet">
```

Use as variáveis `--pg-*` (cores, fontes, escala, grade) em vez de repetir valores soltos.

## Elementos gráficos

Formas tiradas do símbolo e do mundo do esporte. Elas apoiam a marca, nunca competem com ela. **Uma ou duas por peça**, em azul, preto ou branco.

- **Degraus:** as barras do qb como faixas e marcadores.
- **Globo:** exploração e alcance.
- **Linhas de velocidade:** horizontais ou a 30°.
- **Setas:** direção e chamada para ação.
- **Mira:** nos cantos das peças.
- **Topografia:** trilha e outdoor.
- **Rota:** percurso com início e chegada.
- **Coordenadas:** LAT/LON em Space Mono, só com local real.
- **Ícones** (`icones/`): corrida, ciclismo, academia, futebol, vôlei, trilha, eventos, comunidade, explorar, falcão.

## Fotografia

- Preto e branco de alto contraste, documental, luz natural.
- Temas: falcão peregrino (mascote), pessoas reais treinando, cidade, montanha.
- O azul nunca colore a foto: entra como bloco, faixa, tipografia ou mesclagem (foto com fundo branco em multiplicação sobre azul).
- Fotos prontas em `05-imagens/`: `falcao-retrato.jpg` (fundo preto), `falcao-voo.jpg` (fundo branco, mescla em qualquer cor), `falcao-recorte.png`.

## Linguagem

- Lema: **A JORNADA É MAIS IMPORTANTE QUE A LINHA DE CHEGADA.**
- Conceito: **VIVER EM MOVIMENTO.**
- Convite: **SEU ESPORTE. SEU RITMO. SUA JORNADA.**
- Assinatura: **MOVE. CONNECT. EVOLVE.**
- Fala como quem treina junto: frases curtas, verbos de ação, dados reais do treino.
- Evitar: travessão (—), clichês ("no pain, no gain", "foco, força e fé"), linguagem de guerra, inventar números, datas, locais ou depoimentos.

## Instagram

- Post 1080 × 1350 (quadrado 1080 × 1080), margem 80 px. Story 1080 × 1920, 250 px livres em cima e embaixo.
- Capas de destaque: ver `destaques/` na raiz (logo ou ícone em branco sobre gradiente azul profundo → ciano com grão; exceção aprovada só para destaques).
- Grade fixa: símbolo no canto superior esquerdo, rótulo em Space Mono à direita, mensagem no terço inferior, `@peregrinusclub` no rodapé.
- Fundo pela classe do `<body>`: preto (padrão), `azul` ou `claro`.
- Troque os textos no HTML e exporte em PNG pelo Chrome. O story precisa do `falcao-voo.jpg` na mesma pasta.

## Pendências (não inventar)

- Pantone e CMYK são referência: validar em prova de cor com a gráfica.
- Ainda não definidos: locais e horários fixos de treino, link de contato/inscrição, palavra-chave de CTA, cidade-sede, ano de fundação e número de membros. Não usar "EST." até confirmar o ano.
