# Formatos · Villas Cavaliere

## Carrossel (feed)
- 1080 × 1350, 6 a 9 slides. Template: `templates/post.html` (capa e slides de conteúdo) e `templates/post-foto.html` (capa com foto).
- **Slide 1 (capa):** categoria + contador, sobretítulo Tiffany, título em Yanone que promete algo concreto, linha de apoio curta. Pode ter foto.
- **Miolo:** um ponto por slide. Número grande em Yanone ("01"), título curto, 2 a 3 linhas de corpo. Sem bullet.
- **Penúltimo:** síntese ou virada emocional.
- **Último (CTA):** "Comente TRAJE" ou "Agende seu horário exclusivo", com o lockup em destaque.
- Legenda: `ig-caption` com as regras de `tom-de-voz.md`. Salvar em `legenda.txt`.
- Referência: `Downloads/CLAUDE SKILLS/carrossel-erros-noivo/` (9 slides aprovados).

## Post estático
- 1080 × 1350, `templates/post.html` com uma frase forte só. Ex.: "O AZUL QUE VESTE O SIM."

## Story
- 1080 × 1920, `templates/story.html`. Zona segura: deixar 250 px livres em cima e embaixo.
- Gradiente Neblina ou Lapela. Uma ideia por tela. Botão contornado para CTA.
- Sequência típica de venda: bastidor (foto/vídeo) → enquete ou caixa de pergunta → prova social → "Agenda aberta" com link ou palavra-chave.

## Reel
- Roteiro com `ig-reel` (usar hookscore_pt.py). Gancho nos 2 primeiros segundos, sem nome da marca.
- Texto na tela: Yanone caixa alta, Linho, curto. Legenda queimada em Hanken.
- Capa do reel: `templates/post.html` em 1080 × 1920 (`data-size="1080x1920"`), título centralizado na faixa 4:5 do meio para não cortar no grid.
- Trilha: elegante, instrumental, sem tendência barulhenta.

## Anúncio (Meta Ads)
- Artes: 1080 × 1350 (feed) e 1080 × 1920 (stories/reels). Mesmo sistema visual.
- Copy: texto principal curto com a estrutura gancho → problema → solução → CTA. Título até 40 caracteres. Sem palavras proibidas mesmo em anúncio.
- CTA do botão: "Enviar mensagem" ou "Saiba mais", apontando para o WhatsApp da Villas Cavaliere.

## WhatsApp
Mensagem curta, nome da pessoa, uma pergunta, puxa para data de prova. Exemplo de abertura:
"Oi, {{nome}}! Aqui é {{consultor}}, da Villas Cavaliere. Vi que você comentou TRAJE. Seu casamento já tem data? Assim eu vejo os melhores horários de prova para você."

## Onde salvar
Cada peça numa pasta própria em `C:/Users/DELL/Downloads/CLAUDE SKILLS/<nome-da-peça>/`: os HTMLs, os PNGs (`slide-01.png`...), a foto original e `legenda.txt`.
