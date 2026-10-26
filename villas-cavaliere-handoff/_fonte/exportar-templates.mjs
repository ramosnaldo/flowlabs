// Exporta cada peça dos templates de Instagram como PNG em tamanho real.
// Uso: node _fonte/exportar-templates.mjs [pasta-de-saida]
// Saída padrão: 04-templates-instagram/exportados
import { mkdirSync, readdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const raiz = join(dirname(fileURLToPath(import.meta.url)), '..');
const pasta = join(raiz, '04-templates-instagram');
const saida = process.argv[2] || join(pasta, 'exportados');
mkdirSync(saida, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 2000 } });

for (const arquivo of readdirSync(pasta).filter((f) => f.endsWith('.html')).sort()) {
  const url = pathToFileURL(join(pasta, arquivo)).href + '?exportar';
  await page.goto(url);
  await page.evaluate(() => document.fonts.ready);
  const pecas = page.locator('.peca');
  const n = await pecas.count();
  for (let i = 0; i < n; i++) {
    const nome = `${arquivo.replace(/\.html$/, '')}-${String(i + 1).padStart(2, '0')}.png`;
    await pecas.nth(i).screenshot({ path: join(saida, nome) });
    console.log(nome);
  }
}
await browser.close();
