# PEREGRINUS Club Esportivo · Brand kit 2.0

Pasta de criação da PEREGRINUS. O app do clube fica em outro repositório (`ramosnaldo/pgrns`).
Este README resume as regras do manual (`Manual-Handoff-Peregrinus.pdf` / `guia-handoff.html`). Na dúvida, o manual manda.

## O que tem aqui

| Pasta | Conteúdo |
|---|---|
| `00-prancha-logos.png` | Visão geral de todas as versões da logo |
| `01-logos/` | `svg/` (texto em curvas), `pdf-vetor/` (gráfica), `png/` (transparente, 2400 px), `3d/` (qb 3D + original do cliente) |
| `02-tokens/` | `tokens.css` e `tokens.json`: cores, fontes, escala e grade |
| `03-fontes/` | Anton, Inter, Instrument Serif, Space Mono + licenças OFL |
| `04-templates-instagram/` | post, post-foto, post-conteudo, post-cta, treino, story (HTML → exportar PNG) |
| `05-imagens/` | Fotos P&B do falcão (voo, recorte) |
| `06-elementos-graficos/` | degraus, globo, setas, mira, rota, topografia, velocidade + `icones/` |

## Logo

- Escolha a versão pela cor do fundo: principal (fundo claro), negativa (fundo escuro), mono preto (sobre azul ou 1 cor), mono branco (sobre foto ou cinza), vertical (peito, selos, boné), lettering (costas, mangas, faixas).
- Símbolo principal **qb**: mínimo 32 px / 15 mm bordado. Abaixo disso, use o **falcão em P**.
- qb e falcão são desenhos do cliente: nunca redesenhar.
- Proibido: distorcer, girar o qb a 90°, neon ou brilho, sair da paleta, reordenar símbolo e nome.

## Cores

| Papel | Nome | HEX | Proporção |
|---|---|---|---|
| Principal | Azul Peregrino | `#36BFEC` | 20% |
| Base | Preto | `#000000` | 45% |
| Apoio | Cinza | `#888888` | 10% |
| Respiro | Cinza claro | `#D6D6D6` | 25% |
| Texto azul sobre claro | Azul de apoio | `#1A7FA6` | só texto |

- Fundos chapados. Sem gradiente colorido, sem neon, sem brilho.
- Sem turquesa `#65CFC4` (versão antiga) e sem ciano `#00F9E7` (primeira camiseta, anterior ao kit 2.0).

## Tipografia

- **Anton**: títulos, caixa alta, entrelinha 0,86 a 0,95.
- **Instrument Serif itálico**: uma frase editorial por peça, no máximo.
- **Inter**: texto corrido (400, 500, 600, 700).
- **Space Mono**: dados, rótulos, horários, distâncias. Caixa alta, espaçamento +100 a +140.
- PEREGRINUS em Anton +50 com o I cortado na diagonal (classe `.pg-wm` em `tokens.css`).

## Fotografia

Preto e branco de alto contraste, documental, luz natural. O azul nunca colore a foto: entra como bloco, faixa, tipografia ou mesclagem (multiplicação sobre azul).

## Linguagem

- Lema: **A JORNADA É MAIS IMPORTANTE QUE A LINHA DE CHEGADA.**
- Conceito: **VIVER EM MOVIMENTO.**
- Convite: **SEU ESPORTE. SEU RITMO. SUA JORNADA.**
- Assinatura: **MOVE. CONNECT. EVOLVE.**
- Fala como quem treina junto: frases curtas, verbos de ação, dados reais do treino.
- Evitar: travessão (—), clichês ("no pain, no gain", "foco, força e fé"), linguagem de guerra, inventar números, datas, locais ou depoimentos.

## Instagram

- Post 1080 × 1350, margem 80 px. Story 1080 × 1920, 250 px livres em cima e embaixo.
- Grade fixa: símbolo no canto superior esquerdo, rótulo em Space Mono à direita, mensagem no terço inferior, `@peregrinusclub` no rodapé.
- Fundo pela classe do `<body>`: preto (padrão), `azul` ou `claro`.
- Troque os textos no HTML e exporte em PNG pelo Chrome. O story precisa do `falcao-voo.jpg` na mesma pasta.

## Pendências (não inventar)

- Pantone e CMYK são referência: validar em prova de cor com a gráfica.
- Ainda não definidos: locais e horários fixos de treino, link de contato/inscrição, palavra-chave de CTA, cidade-sede, ano de fundação e número de membros. Não usar "EST." até confirmar o ano.
