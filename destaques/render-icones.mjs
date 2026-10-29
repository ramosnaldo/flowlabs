// Renderiza as capas de ícone/texto sobre o fundo gerado pelo gerar.py.
// Chamado pelo gerar.py (precisa do Playwright com Chromium).
import { readFileSync, writeFileSync, rmSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const DIR = dirname(fileURLToPath(import.meta.url));
const svg = (nome) => readFileSync(join(DIR, "icones", nome), "utf8");

// Largura do ícone: ~50% do círculo de 1080 px.
const ICONE = 540;

const CAPAS = [
  ["medalha", svg("medal-fill.svg")],
  ["bota-trilha", svg("bota-trilha.svg")],
  ["cerebro", svg("brain-fill.svg")],
  ["jejum", svg("jejum.svg")],
  ["70km", { numero: "70" }],
  ["50km", { numero: "50" }],
  ["halter", svg("halter.svg")],
  ["skate", svg("skate.svg")],
  ["voltar", svg("arrow-u-up-left-fill.svg")],
  ["livro", svg("livro.svg")],
  ["cachorro", svg("dog-fill.svg")],
  ["festa", svg("confetti-fill.svg")],
];

const fonte = (f) => `url(fontes/${f}) format("woff")`;
const css = `
@font-face { font-family: Picho; src: ${fonte("sedgwick-ave-display-latin-400-normal.woff")}; }
@font-face { font-family: Grafite; src: ${fonte("rubik-bubbles-latin-400-normal.woff")}; }
html, body { margin: 0; width: 1080px; height: 1920px; overflow: hidden; }
body { background: url(.fundo.png); display: grid; place-items: center; color: #fff; }
.icone svg { width: ${ICONE}px; height: ${ICONE}px; display: block; }
.km { display: flex; flex-direction: column; align-items: center; padding-top: 80px; }
.km .n { font: 400px/0.8 Picho; transform: rotate(-6deg) scaleY(1.3); }
.km .u { font: 230px/1 Grafite; margin-top: 40px; letter-spacing: 4px; }
`;

const corpo = (c) =>
  typeof c === "string"
    ? `<div class="icone">${c}</div>`
    : `<div class="km"><div class="n">${c.numero}</div><div class="u">KM</div></div>`;

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
for (const [nome, conteudo] of CAPAS) {
  const html = `<!doctype html><meta charset="utf-8"><style>${css}</style>${corpo(conteudo)}`;
  const tmp = join(DIR, "_tmp.html");
  writeFileSync(tmp, html);
  await page.goto("file://" + tmp, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: join(DIR, `destaque-${nome}.png`) });
  console.log("ok", `destaque-${nome}.png`);
}
await browser.close();
rmSync(join(DIR, "_tmp.html"), { force: true });
