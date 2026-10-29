# Capas de destaque (Instagram)

Capas dos destaques com as logos da PEREGRINUS e da FLOW Labs.

| Arquivo | Logo usada |
|---|---|
| `destaque-peregrinus.png` | Falcão em P branco (`peregrinus/01-logos/png/peregrinus-falcao-p-branco.png`) |
| `destaque-flowlabs.png` | Símbolo FLOW Labs (`brand/flow-labs/logo-simbolo.png`) |
| `preview-destaques.png` | Simulação de como aparecem no perfil (círculos) |

## Padrão

- PNG 1080 × 1920. O Instagram recorta um círculo de 1080 px no centro; a logo fica centralizada nele, ocupando 55% a 67% da largura.
- Fundo: gradiente diagonal azul profundo `#06164A` → azul `#0E5CA8` → ciano `#3BE1F0`, com grão monocromático de 7%.
- Logo sempre em branco/clara, sem texto na capa. Nunca redesenhar a logo: usar os arquivos oficiais.
- Esse gradiente é uma exceção aprovada só para capas de destaque (pedido do Giovani em 29/10/2026). Nos posts e stories continua valendo a regra de fundo chapado dos manuais.

## Como gerar de novo

```bash
python3 destaques/gerar.py
```

Para um destaque novo, adicione uma linha em `CAPAS` no `gerar.py` (arquivo, logo, largura).

Pendência: o símbolo da FLOW Labs só existe em PNG de 305 px; quando sair o vetor, troque o caminho em `CAPAS` e gere de novo para ficar mais nítido.
