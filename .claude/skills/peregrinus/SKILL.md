---
name: peregrinus
description: "Brand kit oficial da PEREGRINUS Club Esportivo (@peregrinusclub, club de corrida, ciclismo, academia, futebol, vôlei e trilha): brand kit 2.0 com paleta azul #36BFEC e preto, símbolo qb, falcão em P, tipografia, elementos gráficos, fotografia P&B, tom de voz e templates prontos para gerar post, carrossel, story, convocação de treino, cartaz de evento, legenda e estampa no padrão da marca. Use SEMPRE que o pedido citar Peregrinus, PEREGRINUS Club, @peregrinusclub, Peregrinus Run/Ride/Train/Play, o símbolo qb ou o falcão peregrino da marca, ou pedir conteúdo, arte ou produto para esse club."
---

# PEREGRINUS Club Esportivo · Brand kit 2.0

Esta skill é a fonte única da marca. A versão oficial foi aprovada pelo Patrick em 11/10/2026. Antes de criar qualquer peça, leia só o que a tarefa pede:

| Vai fazer... | Leia |
|---|---|
| Qualquer texto (legenda, roteiro, anúncio, DM, convite de treino) | `references/tom-de-voz.md` |
| Qualquer arte (post, carrossel, story, cartaz, estampa, produto) | `references/identidade-visual.md` + `templates/` |
| Decidir pauta, ângulo, modalidade ou público | `references/marca.md` |
| Tamanhos e estrutura de cada formato | `references/formatos.md` |

Manual completo publicado: https://claude.ai/artifact/4tc98UKrts58TgyWxjJBw9 (arquivo local em `D:/Claude/CLAUDE SKILLS/peregrinus-brand/peregrinus-brand-board.html`). Prévia dos templates em `exemplos/templates-preview.png`.

## A marca em 30 segundos

Club esportivo que reúne quem vive em movimento: corrida, ciclismo, academia, futebol, vôlei e trilha, com eventos e comunidade. Não é só um grupo de corrida. Conceito: **Viver em movimento.** Lema: **A jornada é mais importante que a linha de chegada.** Arquétipo: o Explorador. Mascote: o falcão peregrino (visão, liberdade, direção e controle, sem agressividade).

Visual: azul #36BFEC sobre preto, cinzas de apoio, fundos chapados, fotos em preto e branco de alto contraste, Anton em caixa alta.

## Regras inegociáveis

1. **Nunca travessão (—).** Use ponto, vírgula ou dois-pontos.
2. **Paleta fechada:** azul #36BFEC, preto #000000, cinza #888888, cinza claro #D6D6D6, branco. Azul de apoio #1A7FA6 só para texto azul sobre fundo claro. Nada de turquesa (#65CFC4 é da versão antiga), neon, brilho, gradiente colorido.
3. **Símbolo principal é o qb** (desenho do cliente: um P em pé e um P girado). Nunca redesenhar, girar a 90°, distorcer ou reordenar a assinatura. Mínimo 32 px; abaixo disso, use o falcão em P.
4. **Falcão em P** (desenho do cliente) é o símbolo secundário: favicon, ícone, crachá, chaveiro, medalha, patch, assinatura de comunidade. Nunca redesenhar.
5. **Fotos sempre P&B.** O azul entra como bloco, faixa, tipografia ou multiplicação sobre fundo azul. Nunca colorir a foto.
6. **Não usar a foto do rapaz do mockup da camiseta** em peças de marca (o Patrick pediu para tirar de tudo).
7. **Linguagem sem clichê:** nada de "no pain, no gain", "foco, força e fé", "disciplina hoje, liberdade sempre", nem linguagem de guerra (atacar, destruir, esmagar).
8. **Nunca inventar** ano de fundação (não use "EST."), número de membros, resultado, depoimento, local ou horário real. Deixe `{{local}}`, `{{data}}`, `{{horário}}` e avise.
9. **Uma serifada itálica por peça, no máximo** (Instrument Serif), só como destaque editorial.
10. **Artes do cliente são intocáveis:** a estampa do globo (`assets/estampa-globo-camiseta.svg`), o qb e o falcão em P só podem ser vetorizados ou recoloridos se o Patrick pedir.

## Fluxo padrão

1. **Entender o pedido.** Se faltar o essencial (formato, modalidade, data, local), pergunte numa mensagem só. Se der para supor com segurança, suponha e diga o que supôs.
2. **Texto primeiro.** Para copy, entregue 3 versões e recomende uma (1 a 2 frases do porquê). Para carrossel, entregue o roteiro slide a slide e espere o ok antes de renderizar, a não ser que o Patrick diga para ir direto.
3. **Arte.** Copie o template de `templates/` para `D:/Claude/CLAUDE SKILLS/peregrinus-<nome-da-peça>/`, troque os textos e renderize com `scripts/render.py`. Olhe o PNG antes de entregar (texto cortado, contraste, margem de 80 px).
4. **Checklist** abaixo.
5. **Entrega:** PNGs + `legenda.txt` na pasta da peça. Diga a modalidade e o formato usados.

## Templates (`templates/`)

| Arquivo | Uso |
|---|---|
| `post.html` | capa de carrossel ou post estático, fundo preto |
| `post-foto.html` | capa com foto P&B (coloque `foto.jpg` na pasta) e bloco azul |
| `post-conteudo.html` | slide de miolo com número grande |
| `post-cta.html` | último slide, fundo azul |
| `treino.html` | convocação de treino ou evento (dia, hora, local, distância) |
| `story.html` | story 1080x1920 com o falcão em voo |

Troque o fundo pela classe do `<body>`: `preto` (padrão), `azul` ou `claro`. Títulos longos: baixe o `font-size` do `.title`. As fotos do falcão para usar estão em `assets/` (`falcao-retrato.jpg` fundo preto, `falcao-voo.jpg` fundo branco, ótimo em multiplicação sobre azul). Para mudar o design base, edite `scripts/gerar_templates.py` e rode de novo.

## Renderizar

```bash
python ~/.claude/skills/peregrinus/scripts/render.py caminho/da/peça.html [mais.html ...]
```
Gera o PNG ao lado de cada HTML, no tamanho de `data-size` do `<body>` (1080x1350 post, 1080x1920 story, 1080x1080 quadrado). Usa o Chrome instalado. Fontes vêm do Google Fonts, então precisa de internet.

## Integração com outras skills

As skills `ig-*` usam `~/.claude/instagram/voice.md`, que hoje é da Villas Cavaliere. **Para Peregrinus, vale esta skill**: passe as regras de `references/tom-de-voz.md` para elas e ignore o voice.md. Para revisar se soa humano, `ig-human`. Para vídeo, o projeto Remotion fica em `D:/Claude/CLAUDE SKILLS/videos/peregrinus-remotion` (composições `Peregrinus` e `CamisetaRun`). Imagens e vídeos por IA: Higgsfield, conta no plano grátis (usar `nano_banana_2_1`; `gpt_image_2_5` é bloqueado).

## Checklist antes de entregar

1. Nenhum travessão, nenhum clichê, nenhuma linguagem de guerra?
2. Só cores da paleta oficial? Texto azul sobre claro usa #1A7FA6?
3. qb ou falcão em P presentes, sem distorção, no tamanho mínimo?
4. Fotos em P&B, azul só como bloco ou tipografia?
5. No máximo uma frase em serifada itálica?
6. Nenhum dado inventado (data, local, número, ano)? Pendências marcadas com `{{}}`?
7. Margem de 80 px, rótulo técnico em Space Mono, @peregrinusclub visível em peça de feed?

## Dados pendentes (pedir ao Patrick quando precisar)

Locais e horários fixos de treino de cada modalidade, link de WhatsApp ou inscrição, palavra-chave de CTA para comentários, ano de fundação, número de membros, cidade-sede oficial. Quando ele informar, atualize `references/marca.md`.
