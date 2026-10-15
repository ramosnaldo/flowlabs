# Identidade visual 2.0 · Villas Cavaliere

Fonte: `C:/Users/DELL/Downloads/Villas Cavaliere · Identidade 2.0.pdf` (9 páginas) e canvas https://claude.ai/artifact/CjNnzxUWSQb2PaxGCtuQGL. Prints em `../exemplos/`.

## Conceito
"Luz de alfaiataria": um terno sob a luz do provador. Fundo profundo, um ponto de luz azul vindo de um canto, grão fino por cima. Minimalista, masculino, silencioso.

## Assinatura (logo)
- **Símbolo:** o ornamento de quatro volutas. Vetor em `../assets/`:
  - `simbolo-claro.svg` (gradiente Linho → Azul Tiffany) para fundos escuros
  - `simbolo-escuro.svg` (gradiente Azul Cavaliere → Marinho) para fundos claros
  - `simbolo-linho.svg`, `simbolo-offwhite.svg`, `simbolo-noite.svg` chapados
  - `simbolo-path.txt` só o path, viewBox `0 0 302 324`
- **Lockup horizontal:** símbolo | fio vertical fino | "VILLAS" (pequeno, espaçado 0.6em, Azul Cavaliere ou Tiffany) sobre "CAVALIERE" (Yanone 200, protagonista).
- **Versões:** principal (fundo claro), negativa (fundo noite), símbolo isolado, assinatura reduzida (só tipografia).
- Não distorcer, não trocar cor fora da paleta, não aplicar sombra.

## Paleta

| Nome | HEX | Papel | Uso |
|---|---|---|---|
| Noite | `#0F1E25` | base | 40% |
| Linho | `#EFEBE5` | fundo claro e texto sobre escuro | 25% |
| Azul Marinho | `#1B2A4A` | base | 15% |
| Azul Cavaliere | `#5394A9` | cor da assinatura, brilho | 10% |
| Areia | `#D6D1CA` | neutro | ~5% |
| Black Tie | `#121417` | contraste, fundo de post | |
| Azul Tiffany | `#81D8D0` | acento (sobretítulo, detalhe) | pouco |
| Cinza | `#8E9196` | acento | pouco |
| Off-white | `#F7F5F0` | acento claro | pouco |

**Proibido:** tons terrosos, rosé, vinho, terracota (eram da versão antiga), branco puro chapado, preto puro chapado.

## Gradientes (sempre radiais, de um ponto de luz para a sombra)
- **Lapela** (principal): Azul Cavaliere → Marinho → Noite
- **Linho** (fundos claros): Linho → Areia → Azul Tiffany
- **Neblina** (campanhas e eventos): Off-white → Cinza → Marinho
- **Black Tie** (feed): `#1A1D21 → #121417 → #0B0C0E` com brilho Azul Cavaliere a 32% no canto superior direito

Regras: direção sempre radial, luz vindo de um canto. Nunca gradiente linear chapado. Texto em Linho sobre a área mais escura.

## Grão
Ruído monocromático, 4 a 8% de intensidade, modo sobrepor. Aplicar também nas fotos para unificar feed e peças. Nos templates, é o `<svg class="grain">` com `feTurbulence`.

## Padrão "tom sobre tom"
O símbolo repetido como textura, 8 a 15% de opacidade, na mesma família de cor do fundo. Aparece de perto, some de longe, como a trama de um tecido nobre. Usos: Linho + Areia (papelaria, embalagem), Cinza + Off-white (forro, convites), Marinho (etiqueta, verso).

## Tipografia
Google Fonts: `Yanone Kaffeesatz` (200, 300) e `Hanken Grotesk` (300, 400).

| Uso | Fonte | Detalhe |
|---|---|---|
| Títulos | Yanone Kaffeesatz ExtraLight 200 / Light 300 | sempre CAIXA ALTA, tracking +6% |
| Sobretítulos / categorias | Hanken Grotesk Regular 400 | 12 a 14 px no impresso (≈26 a 30 px no post 1080), caixa alta, tracking +32% |
| Corpo | Hanken Grotesk Light 300 | 15 a 17 px no impresso (≈34 a 40 px no post), entrelinha 1.6 |

Escala no post 1080x1350: título 120 a 150 px, sobretítulo 28 px, corpo 36 px, rodapé 26 px.

## Fundo de post (página 08 do manual)
- 1080 × 1350 (4:5)
- Fundo Black Tie com brilho Azul Cavaliere 32% no canto superior direito
- Símbolo gigante quase invisível no canto superior direito (opacidade ~6%)
- Margem de segurança: **96 px** em todos os lados
- Topo: `[CATEGORIA]` à esquerda, `01 / 06` à direita (Hanken, caixa alta, espaçado, Linho a 60%)
- Miolo: sobretítulo em Azul Tiffany, título grande em Yanone, fio curto Azul Cavaliere abaixo
- Rodapé: lockup (símbolo + VILLAS/CAVALIERE) à esquerda, `@villascavaliere` à direita

## Fotografia
- Homens de traje, luz baixa, fundo escuro ou desfocado, clima de fim de tarde ou noite.
- Tratamento: preto e branco frio ou duotone azul (Noite → Linho), com grão por cima.
- Capa com foto: foto ocupando a metade de baixo, degradê para o Black Tie no topo onde fica o título (ver `exemplos/capa-carrossel-erros-noivo.png`).
- Detalhes que vendem: lapela, abotoadura, mãos ajustando, giz e fita métrica.

## Aplicações aprovadas (página 07)
- **Feed:** gradiente Lapela, símbolo no topo, sobretítulo Tiffany ("COLEÇÃO 2027"), título "O AZUL QUE VESTE O SIM.", @ no rodapé.
- **Story:** gradiente Neblina, sobretítulo "AGENDA ABERTA", título "PROVA COM HORA MARCADA", botão contornado "AGENDAR".
- **Etiqueta e cartão:** Marinho com símbolo e padrão; cartão em Off-white com lockup.
