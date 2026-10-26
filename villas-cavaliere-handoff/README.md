# Villas Cavaliere · Handoff de marca

Identidade Visual 2.0 (outubro 2026), FLOW Labs. Abra `guia-handoff.html` no navegador: é o manual em formato web, com os arquivos para baixar.

| Pasta | Conteúdo |
| --- | --- |
| `01-logos/svg` | Vetor para web, Figma, Illustrator. Texto já em curvas |
| `01-logos/pdf-vetor` | Vetor para gráfica e bordado |
| `01-logos/png` | Fundo transparente, 2000 px no lado maior, e `vc-avatar-instagram-1080.png` |
| `02-tokens` | `tokens.css` (variáveis e classes prontas) e `tokens.json` |
| `03-fontes` | Yanone Kaffeesatz 200/300 e Hanken Grotesk 300/400, licença OFL, e `fontes.css` |
| `04-templates-instagram` | Post, carrossel (6 lâminas) e story em HTML editável |
| `_fonte` | Scripts que geram os logos e os PNGs |

Os logos saem em 4 formas (`horizontal`, `vertical`, `assinatura` com só o texto, `simbolo`) × 4 versões (`principal`, `negativa`, `mono-blacktie`, `mono-offwhite`).

## Usar os templates

1. Abra `04-templates-instagram/post.html`, `carrossel.html` ou `story.html`.
2. Clique nos textos para editar. Para pôr uma foto, defina `--foto: url(minha-foto.jpg)` no `style` do elemento `.foto`.
3. Exporte com `node _fonte/exportar-templates.mjs` (gera PNG em tamanho real em `04-templates-instagram/exportados`) ou abra com `?exportar` na URL e capture cada peça.

## Gerar os arquivos de novo

```sh
pip install fonttools uharfbuzz
python3 _fonte/gerar_logos.py      # SVGs, a partir do símbolo original e das fontes
node _fonte/exportar.mjs           # PNG, PDF vetorial e avatar (precisa do playwright)
node _fonte/exportar-templates.mjs # PNGs dos templates
```

O símbolo vem do vetor do manual (`_fonte/simbolo-original.d`). Mude cores e proporções no topo de `gerar_logos.py`.

## Ainda falta

- Referência Pantone das cores: pedir à gráfica a partir da prova de cor CMYK
- Telefone e link de WhatsApp oficiais para cartão e contracapa
- Banco de fotos aprovado seguindo a direção de imagem
