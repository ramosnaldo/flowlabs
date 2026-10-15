---
name: villas-cavaliere
description: "Brand kit completo da Villas Cavaliere (marca de trajes masculinos premium, @villascavaliere): identidade visual 2.0, paleta, fontes, símbolo, tom de voz, regras de copy e templates prontos para gerar post, carrossel, story, reel, legenda, anúncio e mensagem de WhatsApp no padrão da marca. Use SEMPRE que o pedido citar Villas Cavaliere, Cavaliere, @villascavaliere, traje, noivo, padrinho ou príncipe de debutante, ou pedir conteúdo para essa marca."
---

# Villas Cavaliere · Brand kit

Esta skill é a fonte única da marca. Antes de criar qualquer peça, leia só o que a tarefa pede:

| Vai fazer... | Leia |
|---|---|
| Qualquer texto (legenda, roteiro, anúncio, DM, WhatsApp) | `references/tom-de-voz.md` |
| Qualquer arte (post, carrossel, story, capa de reel, anúncio) | `references/identidade-visual.md` + `templates/` |
| Decidir pauta, ângulo ou público | `references/marca.md` |
| Especificação de cada formato (tamanhos, nº de slides, estrutura) | `references/formatos.md` |

Exemplos aprovados ficam em `exemplos/` (capa e legenda do carrossel "5 erros do noivo", páginas do manual). Use como régua de qualidade.

## A marca em 30 segundos

Marca de trajes masculinos premium em Curitiba. Nunca chamar de atelier ou ateliê (proibido desde 2026-10-13). **Não é loja, não é locadora.** Vende a experiência completa do traje: consultoria, escolha, prova e ajuste final, do agendamento ao grande dia. Fala com noivos, padrinhos, convidados de casamento de alto padrão e com o príncipe do baile de debutante.

Tom: confiante, sofisticado, emocional. Visual: noite, azul profundo, luz de alfaiataria, grão fino, tipografia fina em caixa alta.

## Regras inegociáveis (valem para tudo)

1. **Nunca travessão (—).** Use ponto, vírgula ou dois-pontos.
2. **Nunca abrir com o nome da marca.** Abre com gancho emocional.
3. **Palavras proibidas:** loja, locadora, aluguel, compre agora, promoção, desconto, oferta, empresa, talvez. (Só quebrar se o Patrick pedir explicitamente.)
4. **Emoji:** no máximo 1, só ✨, nunca no gancho. Nunca bullet point na peça final.
5. **Assinatura:** toda legenda termina com "Equipe Villas Cavaliere".
6. **CTA:** "Agendar horário exclusivo" ou "Falar com um consultor". Palavra-chave de comentário: **TRAJE**.
7. **Debutante:** o protagonista é o príncipe, nunca a debutante.
8. **Nunca inventar número, depoimento ou nome de cliente.** Se faltar prova, deixe `{{número}}` e avise.
9. **Visual:** só a paleta oficial, nada de tons terrosos, nada de gradiente linear chapado, nada de fonte fora de Yanone Kaffeesatz + Hanken Grotesk.
10. **Cada peça puxa um pilar** (Soluções, Conveniência, Experiência) e diz qual.

## Fluxo padrão

1. **Entender o pedido.** Se faltar o essencial (formato, público, tema), pergunte numa mensagem só. Se der para supor com segurança, suponha e diga o que supôs.
2. **Texto primeiro.** Para copy, entregue **3 versões + recomendação** de qual usar e por quê (1 a 2 frases). Para carrossel, entregue o roteiro slide a slide e espere o ok antes de renderizar, a não ser que o Patrick diga para ir direto.
3. **Arte.** Copie o template certo de `templates/` para a pasta do projeto em `C:/Users/DELL/Downloads/CLAUDE SKILLS/<nome-da-peça>/`, preencha e renderize com `scripts/render.py`. Olhe o PNG gerado antes de entregar (texto cortado, contraste, margem de 96 px).
4. **Checklist** (abaixo) antes de mostrar qualquer coisa.
5. **Entrega:** PNGs + `legenda.txt` na mesma pasta. Diga o pilar usado.

## Templates (`templates/`, prévia em `exemplos/templates-preview.png`)

| Arquivo | Uso |
|---|---|
| `post.html` | capa de carrossel ou post estático (fundo Black Tie) |
| `post-foto.html` | capa com foto (coloque `foto.jpg` na pasta; ajuste `object-position`) |
| `post-conteudo.html` | slide de miolo com número grande |
| `post-cta.html` | último slide, CTA "Comente TRAJE" (fundo Lapela) |
| `story.html` | story 1080x1920 (fundo Neblina, botão AGENDAR) |

Troque o fundo mudando a classe do `.bg` (`blacktie`, `lapela`, `neblina`, `linho`; em `linho` adicione `class="claro"` no body). Títulos longos: baixe o `font-size` do `.title` até caber em 2 ou 3 linhas. Se mudar o design base, edite `scripts/gerar_templates.py` e rode de novo.

## Renderizar artes

```bash
python ~/.claude/skills/villas-cavaliere/scripts/render.py caminho/do/slide.html [mais.html ...]
```
Gera um PNG ao lado de cada HTML, no tamanho certo (lê `data-size` do `<body>`: 1080x1350 post, 1080x1920 story, 1080x1080 quadrado). Usa o Chrome instalado, sem dependências extras. Para fotos, coloque o arquivo na mesma pasta do HTML.

## Integração com outras skills

As skills `ig-*` (ig-reel, ig-caption, ig-carousel, ig-story...) já usam `~/.claude/instagram/voice.md`, que espelha esta skill. Se houver divergência, **vale esta skill**. Em português, use os scripts `_pt` delas (hookscore_pt.py, caption_pt.py, beats_pt.py). Para revisar se o texto soa humano, `ig-human`.

## Checklist antes de entregar

1. Abre com gancho emocional, sem o nome da marca?
2. Nenhuma palavra proibida, nenhum "talvez", nenhum travessão?
3. No máximo 1 emoji (✨), fora do gancho, e sem bullet points?
4. CTA padrão e assinatura "Equipe Villas Cavaliere"?
5. Debutante: foco no príncipe?
6. Pilar declarado?
7. Arte: paleta oficial, fontes oficiais, margem 96 px, símbolo e assinatura no rodapé, @villascavaliere visível, grão aplicado?
8. Nenhum número ou depoimento inventado?

## Dados pendentes (pedir ao Patrick quando precisar)

Link do WhatsApp da Villas Cavaliere para CTA, anos de história, quantos noivos já vestidos, prazo médio do agendamento ao ajuste, depoimentos autorizados. Quando o Patrick informar, atualize `references/marca.md` (seção Provas) e `~/.claude/instagram/voice.md`.
