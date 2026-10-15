# Identidade visual · PEREGRINUS (brand kit 2.0)

## Símbolos
**Principal: qb** (`assets/qb.svg`, viewBox 0 0 107 100). Desenho do cliente: um P em pé e um P girado, hastes lado a lado separadas por um respiro de 3u, três degraus em cada haste (passos, faixas de pista, evolução). É igual de cabeça para baixo (rotação de 180°). Módulo de 16u para hastes, degraus e espessura dos bojos. Mínimo 32 px na tela, 15 mm em bordado. Original 3D do cliente em `assets/qb-original-cliente.webp`.

SVG inline para templates:
```html
<symbol id="pp" viewBox="0 0 107 100"><g id="pp-half"><path fill-rule="evenodd" d="M52 0V65H36V51H22C8 51 0 41 0 25.5C0 10 8 0 22 0Z M36 13H27C21 13 18 18 18 25.5C18 33 21 38 27 38H36Z"/><rect x="36" y="68.5" width="16" height="8" rx="1"/><rect x="36" y="80.25" width="16" height="8" rx="1"/><rect x="36" y="92" width="16" height="8" rx="1"/></g><use href="#pp-half" transform="rotate(180 53.5 50)"/></symbol>
```

**Secundário: falcão em P** (`assets/falcao-p.svg`, viewBox 20 23 690 548). Desenho do cliente: P azul com três asas escalonadas à esquerda e a cabeça do falcão recortada no bojo, olho azul. As três asas repetem os três degraus do qb. Uso em tamanho pequeno (favicon, notificação, ícone do app), crachá, chaveiro, medalha, patch e assinatura de comunidade.
```html
<symbol id="fal" viewBox="20 23 690 548"><path fill-rule="evenodd" d="M305 25 H560 C650 25 707 105 707 218 C707 335 622 428 498 428 L430 568 H305 V362 H218 L172 295 H305 V265 H146 L98 195 H305 V165 H70 L22 100 H305 Z M367.7 484.6C366.9 483.7 367.9 480.5 369.7 478.4C370.5 477.5 371.1 476.2 371.7 473.8C372.6 470.1 373.4 468.1 375.0 466.1C375.6 465.4 376.8 463.3 377.6 461.4C378.4 459.5 379.8 456.9 380.7 455.6C381.6 454.3 382.8 452.0 383.4 450.6C384.0 449.1 385.3 446.8 386.2 445.3C387.1 443.9 388.9 440.5 390.2 437.8C393.0 432.2 398.6 421.6 399.7 420.1C400.1 419.5 401.1 417.7 401.9 416.0C402.8 414.3 404.4 411.5 405.5 409.8C406.6 408.1 408.0 405.7 408.5 404.6C409.0 403.4 410.3 401.2 411.3 399.7C412.4 398.1 413.8 395.6 414.5 394.1C415.2 392.6 416.5 390.2 417.4 388.9C418.3 387.5 419.7 384.8 420.6 382.9C421.6 380.9 422.9 378.6 423.6 377.6C424.3 376.6 425.6 374.2 426.5 372.3C427.4 370.3 428.8 367.9 429.5 366.8C430.3 365.8 431.4 363.8 432.0 362.4C432.7 361.0 434.1 358.6 435.1 357.0C436.2 355.5 437.5 352.9 438.2 351.3C438.9 349.8 440.2 347.4 441.1 346.0C442.1 344.7 443.6 342.2 444.4 340.5C445.3 338.7 446.6 336.5 447.3 335.5C448.0 334.4 449.4 331.8 450.4 329.7C451.4 327.5 452.7 325.2 453.3 324.4C453.9 323.7 455.2 321.5 456.2 319.5C457.2 317.5 458.7 314.9 459.6 313.7C460.4 312.5 461.7 310.3 462.3 308.9C462.9 307.5 464.2 305.3 465.2 303.9C466.2 302.6 467.5 300.1 468.2 298.5C468.9 296.8 470.2 294.4 471.1 293.1C472.1 291.9 473.5 289.4 474.3 287.6C475.2 285.9 476.4 283.6 477.2 282.7C477.9 281.7 479.3 279.3 480.2 277.3C481.1 275.4 482.6 272.7 483.5 271.4C484.5 270.0 485.7 268.0 486.2 266.8C486.7 265.7 488.0 263.4 489.1 261.9C490.1 260.3 491.5 257.9 492.1 256.5C492.7 255.2 494.0 253.0 494.9 251.7C495.8 250.4 497.3 247.7 498.2 245.8C499.1 243.8 500.6 241.2 501.5 239.9C502.4 238.6 503.7 236.3 504.5 234.7C505.2 233.1 506.6 230.7 507.5 229.4C508.4 228.1 509.8 225.8 510.5 224.3C511.3 222.7 512.3 220.9 512.8 220.2C514.2 218.5 519.4 208.1 519.4 207.1C519.4 205.6 518.7 204.5 516.7 202.5C514.5 200.4 512.7 199.3 508.2 197.6C506.7 197.0 503.9 195.7 502.2 194.7C500.4 193.7 497.6 192.3 496.0 191.7C494.3 191.0 491.9 189.7 490.5 188.8C489.2 187.9 486.4 186.5 484.3 185.8C482.2 185.0 479.6 183.8 478.5 183.1C477.4 182.3 474.7 180.9 472.6 180.0C470.5 179.0 467.9 177.6 466.8 176.8C465.7 176.1 463.1 174.7 461.0 173.9C459.0 173.0 456.3 171.6 455.0 170.7C453.8 169.9 451.2 168.7 449.4 168.0C447.6 167.3 444.7 166.0 443.1 165.0C441.4 164.0 438.5 162.6 436.6 161.9C434.7 161.1 432.0 159.9 430.8 159.1C429.5 158.2 427.4 157.1 426.2 156.6C422.4 154.9 421.3 153.2 423.0 151.7C423.8 150.9 426.1 150.9 492.0 150.7C520.4 150.6 521.6 150.7 530.2 153.0C533.2 153.8 537.5 154.8 539.8 155.3C545.8 156.4 549.1 157.4 552.9 159.2C554.8 160.1 558.0 161.3 560.0 162.0C562.6 162.8 564.6 163.8 566.6 165.2C568.2 166.3 570.3 167.6 571.4 168.1C573.9 169.4 580.4 175.4 582.1 177.9C583.6 180.1 588.2 183.8 590.5 184.6C591.3 184.9 593.6 185.4 595.5 185.6C600.0 186.2 604.2 187.5 606.6 189.1C607.6 189.8 609.5 190.9 610.8 191.6C614.1 193.4 616.1 195.2 619.3 199.7C622.7 204.4 622.9 204.9 624.1 208.9C626.5 216.5 626.7 222.3 625.1 230.2C623.9 236.1 623.0 238.6 621.0 241.7C620.0 243.2 618.5 245.7 617.8 247.1C616.3 250.0 615.4 250.9 613.5 250.9C611.7 250.9 610.1 249.5 608.0 246.1C605.5 242.0 604.9 241.4 599.8 238.6C591.6 234.0 591.1 233.9 577.5 233.9C566.2 233.9 560.3 234.5 555.1 236.4C543.3 240.6 542.7 240.9 539.4 243.2C538.2 244.1 536.2 245.3 534.9 245.9C533.7 246.6 531.6 247.9 530.4 248.9C529.2 249.9 527.3 251.3 526.3 252.0C522.1 254.8 512.4 264.3 510.1 267.8C509.4 268.9 508.1 270.6 507.2 271.5C506.3 272.4 505.0 274.4 504.2 275.8C503.4 277.3 501.9 279.6 500.8 281.1C499.7 282.5 498.3 284.7 497.7 285.9C497.1 287.2 495.8 289.2 494.9 290.4C494.0 291.7 492.6 293.9 491.8 295.3C491.0 296.8 489.6 298.9 488.7 300.0C487.8 301.1 486.6 303.0 486.0 304.1C485.4 305.3 484.0 307.5 482.9 309.0C481.7 310.5 480.4 312.7 479.8 313.8C479.3 314.8 478.1 316.8 477.1 318.1C476.1 319.4 474.5 321.8 473.6 323.4C472.7 325.1 471.3 327.4 470.4 328.5C469.5 329.6 468.3 331.7 467.6 333.0C466.9 334.3 465.7 336.3 464.8 337.4C463.9 338.5 462.5 340.7 461.6 342.3C460.8 343.9 459.4 346.1 458.4 347.2C457.5 348.4 456.1 350.5 455.4 351.9C454.6 353.4 453.4 355.4 452.6 356.4C451.8 357.5 450.6 359.5 449.9 360.9C449.2 362.4 447.8 364.6 446.8 365.8C445.9 367.0 444.5 369.2 443.7 370.7C443.0 372.1 441.5 374.5 440.4 375.9C439.4 377.4 438.1 379.3 437.6 380.2C437.2 381.2 435.9 383.1 434.8 384.6C433.7 386.0 432.1 388.5 431.3 390.0C430.4 391.5 429.1 393.5 428.4 394.4C427.7 395.2 426.3 397.3 425.2 399.0C424.2 400.7 422.9 402.6 422.4 403.3C421.9 403.9 420.9 405.6 420.1 407.0C419.4 408.5 417.8 411.0 416.6 412.7C415.5 414.3 413.9 416.8 413.1 418.1C412.3 419.5 410.8 421.9 409.8 423.5C408.7 425.0 406.3 428.7 404.4 431.5C402.6 434.4 400.4 437.6 399.5 438.8C398.6 439.9 397.1 442.2 396.2 444.0C395.2 445.7 393.8 448.0 393.0 449.0C392.2 450.1 391.1 452.0 390.4 453.2C389.8 454.4 388.5 456.4 387.6 457.5C385.9 459.6 385.6 460.0 383.9 463.9C383.4 465.0 382.3 466.8 381.4 467.8C380.5 468.7 379.0 471.0 378.0 472.8C376.7 475.3 375.9 476.4 374.4 477.5C373.0 478.5 372.3 479.5 371.4 481.4C370.7 482.7 369.9 484.1 369.7 484.4C369.3 484.9 368.2 485.0 367.7 484.6Z M562.0 197.1C563.7 196.2 568.8 191.6 569.4 190.5C570.2 188.9 570.1 185.9 569.2 184.1C567.9 181.5 564.9 180.0 559.0 179.2C557.3 179.0 555.0 178.5 553.9 178.1C549.4 176.4 547.5 176.4 545.8 178.0C544.2 179.5 544.8 184.9 547.0 188.5C548.3 190.5 553.1 195.9 554.3 196.6C556.7 198.1 559.8 198.3 562.0 197.1Z"/></symbol>
```
Ao usar `<use>` de um symbol, o `<svg>` de fora precisa de `viewBox="0 0 107 100"` (qb) ou `viewBox="0 0 690 548"` (falcão), sem deslocamento, senão corta.

**Assinatura:** qb + PEREGRINUS em Anton, espaçamento +50, com o I cortado na diagonal (clip-path), e CLUB ESPORTIVO em Space Mono espaçado embaixo. Versões: horizontal, vertical (selos, peito, boné), lettering sozinho (costas, mangas), assinatura de comunidade (falcão + PEREGRINUS + "Run · Ride · Train · Play").
```css
.wm .i{display:inline-block;clip-path:polygon(-10% -10%,110% -10%,110% 74%,-10% 92%)}
```
```html
<span class="wm">PEREGR<span class="i">I</span>NUS</span>
```

**Usos incorretos:** distorcer, girar o qb a 90°, aplicar neon ou brilho, sair da paleta, reordenar símbolo e nome.

## Cores
| Nome | HEX | RGB | CMYK | Pantone (validar em prova) | Papel |
|---|---|---|---|---|---|
| Azul Peregrino | #36BFEC | 54 191 236 | 77 19 0 7 | ref. 298 C | assinatura |
| Preto | #000000 | 0 0 0 | 60 40 40 100 | Black 6 C | base |
| Cinza | #888888 | 136 136 136 | 0 0 0 47 | Cool Gray 8 C | apoio |
| Cinza claro | #D6D6D6 | 214 214 214 | 0 0 0 16 | Cool Gray 1 C | respiro |
| Branco | #FFFFFF | | | | texto sobre preto |
| Azul de apoio | #1A7FA6 | | | | só texto azul sobre fundo claro |

Proporção por peça: preto 45, cinza claro 25, azul 20, cinza 10.
Combinações: preto + branco + azul (padrão) · azul + preto (destaque em branco) · cinza claro + preto + azul de apoio.
Fundos **chapados**. Nada de gradiente colorido, granulação pesada, neon ou brilho.

## Tipografia (Google Fonts)
| Papel | Fonte | Regra |
|---|---|---|
| Títulos | **Anton** | caixa alta, entrelinha 0,86 a 0,95 (substitui Druk/DIN Condensed) |
| Destaque editorial | **Instrument Serif itálico** | uma frase por peça, no máximo |
| Texto e interface | **Inter** 400/500/600/700 | legendas, site, app |
| Dados e rótulos | **Space Mono** | caixa alta, espaçamento +100 a +140: horários, km, coordenadas, numeração |

```html
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```

## Elementos gráficos
Uma ou duas por peça, em azul, preto ou branco, sem competir com o símbolo.
- **Degraus:** as barras do qb como faixas, listas, marcadores de progresso.
- **Globo:** wireframe, exploração e alcance (é o mesmo globo da estampa da camiseta).
- **Linhas de velocidade:** horizontais ou a 30°.
- **Setas:** três chevrons `>>>` para direção e CTA.
- **Mira (crosshair):** nos cantos das peças, foco e precisão.
- **Topografia:** curvas de nível para trilha e outdoor.
- **Rotas:** percurso com ponto de início e anel de chegada.
- **Coordenadas:** LAT/LON em Space Mono, só com local real.

## Fotografia
- Preto e branco de alto contraste, documental, luz natural.
- Temas: falcão peregrino, pessoas reais treinando, cidade, montanha, trilha.
- O azul nunca colore a foto: entra como bloco, faixa, tipografia ou mesclagem (foto com fundo branco em `mix-blend-mode: multiply` sobre azul).
- Fotos do falcão prontas: `assets/falcao-retrato.jpg` (fundo preto), `assets/falcao-voo.jpg` (fundo branco).
- Não usar a foto do rapaz do mockup da camiseta.

## Grade de post e story
Símbolo no canto superior esquerdo, rótulo técnico em Space Mono à direita, mensagem no terço inferior, margem de 80 px, mira nos cantos opcional. @peregrinusclub no rodapé.

## Aplicações já desenhadas no manual
Embalagem, camisetas (frente e costas), boné, squeeze, ecobag, chaveiro, crachá "Acesso total", cartaz de evento, cartão de membro, papelaria (carta, envelope, cartão), letreiro em relevo na parede, post de treino.
