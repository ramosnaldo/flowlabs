#!/bin/sh
# Monta o site publicado no Vercel em public/:
#   /                  Turma da Tati
#   /villas-cavaliere/ Handoff de marca Villas Cavaliere (guia, logos, tokens, fontes, templates)
set -eu
cd "$(dirname "$0")/.."

rm -rf public
mkdir -p public/villas-cavaliere

cp -R turma-da-tati/. public/

vc=villas-cavaliere-handoff
cp -R "$vc/01-logos" "$vc/02-tokens" "$vc/03-fontes" "$vc/04-templates-instagram" public/villas-cavaliere/
rm -rf public/villas-cavaliere/04-templates-instagram/exportados
# <base> mantém os caminhos relativos certos com ou sem a barra final em /villas-cavaliere
sed 's|<meta charset="utf-8">|<meta charset="utf-8">\n<base href="/villas-cavaliere/">|' "$vc/guia-handoff.html" > public/villas-cavaliere/index.html

echo "public/ pronto"
