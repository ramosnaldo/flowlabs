#!/bin/sh
# Copia os arquivos de marca deste pacote para a skill .claude/skills/villas-cavaliere-brand.
# Rode depois de mudar logos, tokens, fontes ou templates.
set -eu
pacote="$(cd "$(dirname "$0")/.." && pwd)"
skill="$pacote/../.claude/skills/villas-cavaliere-brand"

rm -rf "$skill/assets"
mkdir -p "$skill/assets/01-logos"
cp -R "$pacote/01-logos/svg" "$skill/assets/01-logos/"
cp "$pacote/01-logos/png/vc-avatar-instagram-1080.png" "$skill/assets/01-logos/"
cp -R "$pacote/02-tokens" "$pacote/03-fontes" "$pacote/04-templates-instagram" "$skill/assets/"
rm -rf "$skill/assets/04-templates-instagram/exportados"
echo "skill sincronizada em $skill"
