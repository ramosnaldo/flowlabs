// Exporta os SVGs de 01-logos/svg para PNG (2000 px, fundo transparente)
// e PDF vetorial, e gera o avatar do Instagram 1080 x 1080.
//
// Uso: node _fonte/exportar.mjs   (precisa do pacote playwright com Chromium)
import { readFileSync, readdirSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const raiz = join(dirname(fileURLToPath(import.meta.url)), '..');
const pastaSvg = join(raiz, '01-logos/svg');
const pastaPng = join(raiz, '01-logos/png');
const pastaPdf = join(raiz, '01-logos/pdf-vetor');
mkdirSync(pastaPng, { recursive: true });
mkdirSync(pastaPdf, { recursive: true });

const LADO_PNG = 2000;

function medidas(svg) {
  const [, , w, h] = svg.match(/viewBox="([^"]+)"/)[1].split(' ').map(Number);
  return { w, h };
}

const browser = await chromium.launch();
const page = await browser.newPage();

for (const arquivo of readdirSync(pastaSvg).filter((f) => f.endsWith('.svg')).sort()) {
  const svg = readFileSync(join(pastaSvg, arquivo), 'utf8');
  const { w, h } = medidas(svg);
  const nome = arquivo.replace(/\.svg$/, '');

  // PNG: o lado maior com 2000 px
  const k = LADO_PNG / Math.max(w, h);
  const pw = Math.round(w * k);
  const ph = Math.round(h * k);
  const solto = svg.replace(/ width="[^"]+" height="[^"]+"/, ` width="${pw}" height="${ph}"`);
  await page.setViewportSize({ width: pw, height: ph });
  await page.setContent(
    `<html><body style="margin:0;background:transparent">${solto}</body></html>`
  );
  await page.locator('svg').screenshot({ path: join(pastaPng, `${nome}.png`), omitBackground: true });

  // PDF vetorial no tamanho do desenho (1 unidade = 1,5 pt = 2 px)
  const vw = Math.ceil(w * 2);
  const vh = Math.ceil(h * 2);
  const vetor = svg.replace(/ width="[^"]+" height="[^"]+"/, ` width="${vw}" height="${vh}"`);
  await page.setContent(
    `<html><head><style>@page{size:${vw}px ${vh}px;margin:0}html,body{margin:0}svg{display:block}</style></head><body>${vetor}</body></html>`
  );
  await page.pdf({ path: join(pastaPdf, `${nome}.pdf`), preferCSSPageSize: true, printBackground: false });
}

// Avatar: fundo Lapela, simbolo negativo centralizado com 40% da altura
const simbolo = readFileSync(join(pastaSvg, 'vc-simbolo-negativa.svg'), 'utf8')
  .replace(/ width="[^"]+" height="[^"]+"/, ' height="432"');
await page.setViewportSize({ width: 1080, height: 1080 });
await page.setContent(`<html><body style="margin:0">
  <div style="position:relative;width:1080px;height:1080px;display:grid;place-items:center;
    background:radial-gradient(120% 120% at 0% 0%,#5394A9 0%,#1B2A4A 42%,#0F1E25 100%)">
    ${simbolo}
    <svg style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none;opacity:.30;mix-blend-mode:overlay">
      <filter id="vcg"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/></filter>
      <rect width="100%" height="100%" filter="url(#vcg)"/>
    </svg>
  </div></body></html>`);
await page.screenshot({ path: join(pastaPng, 'vc-avatar-instagram-1080.png') });

await browser.close();
console.log('PNG e PDF exportados');
