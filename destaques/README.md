# Capas de destaque (Instagram)

Capas dos destaques com as logos da PEREGRINUS e da FLOW Labs.

| Arquivo | Logo usada |
|---|---|
| `destaque-peregrinus.png` | Falcão em P branco (`peregrinus/01-logos/png/peregrinus-falcao-p-branco.png`) |
| `destaque-flowlabs.png` | Símbolo FLOW Labs (`brand/flow-labs/logo-simbolo.png`) |
| `destaque-medalha.png`, `-bota-trilha`, `-cerebro`, `-jejum`, `-halter`, `-skate`, `-voltar`, `-livro`, `-cachorro`, `-festa` | Ícones em branco (`icones/`) |
| `destaque-70km.png`, `destaque-50km.png` | Número em letra de picho (Sedgwick Ave Display) + KM em letra gordinha de grafite (Rubik Bubbles) |
| `preview-destaques.png` | Simulação de como aparecem no perfil (círculos) |

## Padrão

- PNG 1080 × 1920. O Instagram recorta um círculo de 1080 px no centro; a logo fica centralizada nele, ocupando 55% a 67% da largura.
- Fundo: gradiente diagonal azul profundo `#06164A` → azul `#0E5CA8` → ciano `#3BE1F0`, com grão monocromático de 7%.
- Ícones: 540 px (50% do círculo), sempre branco chapado, estilo preenchido. Medalha, cérebro, voltar, cachorro e festa são do Phosphor Icons (MIT, `icones/LICENSE-phosphor.txt`); bota de trilha, jejum (prato-relógio entre garfo e faca), livro (páginas com linhas), halter e skate foram desenhados aqui no mesmo estilo.
- Distâncias: número em Sedgwick Ave Display esticado na vertical e inclinado (picho) e KM em Rubik Bubbles (grafite). Fontes OFL em `fontes/`.
- Logo sempre em branco/clara, sem texto na capa. Nunca redesenhar a logo: usar os arquivos oficiais.
- Esse gradiente é uma exceção aprovada só para capas de destaque (pedido do Giovani em 29/10/2026). Nos posts e stories continua valendo a regra de fundo chapado dos manuais.

## Como gerar de novo

```bash
python3 destaques/gerar.py
```

O `gerar.py` faz as capas de logo e chama o `render-icones.mjs` (Node + Playwright/Chromium) para as de ícone e texto, sobre o mesmo fundo.

Destaque novo: logo → linha em `CAPAS` no `gerar.py`; ícone → SVG em `icones/` com `fill="currentColor"`, linha em `CAPAS` do `render-icones.mjs` e nome em `ICONES` do `gerar.py`.

Pendência: o símbolo da FLOW Labs só existe em PNG de 305 px; quando sair o vetor, troque o caminho em `CAPAS` e gere de novo para ficar mais nítido.
