# Formatos · PEREGRINUS

## Carrossel (feed)
- 1080 × 1350, 5 a 8 slides.
- **Capa:** `templates/post.html` ou `post-foto.html`. Rótulo da modalidade + contador no topo, título em Anton que promete algo concreto.
- **Miolo:** `post-conteudo.html`, um ponto por slide, número grande em azul, 2 a 3 linhas de corpo.
- **Último:** `post-cta.html`, convite claro (aparecer no treino, salvar, chamar no direct).
- Legenda em `legenda.txt`, regras de `tom-de-voz.md`.

## Post estático
1080 × 1350, `post.html` com uma frase forte, ou `treino.html` para convocação.

## Convocação de treino / evento
`treino.html`, 1080 × 1350 (ou 1080 × 1920 trocando `data-size`). Campos: modalidade, nome do treino, dia, horário, local, distância ou nível. Nunca inventar local ou horário: use `{{}}` se não souber.

## Story
1080 × 1920, `story.html`. Deixar 250 px livres em cima e embaixo. Uma ideia por tela. Sequência típica: convocação → enquete (quem vem?) → bastidor do treino → resultado da comunidade.

## Reel
- Gancho nos 2 primeiros segundos, sem nome da marca.
- Texto na tela em Anton caixa alta branco, destaque em azul.
- Capa: `post.html` com `data-size="1080x1920"`, título na faixa central 4:5.
- Projeto de vídeo: `D:/Claude/CLAUDE SKILLS/videos/peregrinus-remotion`.

## Cartaz de evento (impresso)
A3 (297 × 420 mm) ou 3:4. Número grande (distância), rota, ficha técnica em Space Mono (data, largada, elevação). Fundo azul, preto ou cinza claro.

## Estampa de camiseta
- PNG 300 dpi com fundo transparente. Frente até 26 cm de largura; costas até 28 × 36 cm.
- Renderizar com Chrome headless (`--default-background-color=00000000`) a partir de SVG/HTML.
- Cores de silk dentro da paleta 2.0. A camiseta 1 (globo ciano) é anterior ao 2.0.

## Onde salvar
Cada peça numa pasta própria: `D:/Claude/CLAUDE SKILLS/peregrinus-<nome-da-peça>/` com HTMLs, PNGs, fotos e `legenda.txt`. Brand kit e arquivos-mestre: `D:/Claude/CLAUDE SKILLS/peregrinus-brand/`.
