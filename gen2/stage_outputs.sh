#!/bin/sh
# Stage every Week 6 commit file under /mnt/user-data/outputs/booth-wk6/<repo dir>/ so Chrome's
# file_upload can send each directory to github.com/slentz9090/weekly-booth/upload/main/<dir>.
set -e
cd "$(dirname "$0")/.."
OUT=/mnt/user-data/outputs/booth-wk6
rm -rf "$OUT"
mkdir -p "$OUT/docs/data" "$OUT/docs/og" "$OUT/docs/dlffl" "$OUT/docs/foh" "$OUT/docs" "$OUT/gen2"
cp docs/data/dlffl_wk6_facts.json docs/data/foh_wk6_facts.json docs/data/dlffl_wk6_insights.json \
   docs/data/foh_wk6_insights.json docs/data/dlffl_season.json docs/data/foh_season.json "$OUT/docs/data/"
cp docs/og/dlffl-week-6.png docs/og/foh-week-6.png "$OUT/docs/og/"
cp docs/dlffl/week-6.html docs/dlffl/index.html "$OUT/docs/dlffl/"
cp docs/foh/week-6.html docs/foh/index.html "$OUT/docs/foh/"
cp docs/dlffl-latest.txt docs/foh-latest.txt "$OUT/docs/"
cp gen2/dlffl_wk6.py gen2/foh_wk6.py gen2/update_season.py gen2/hub.py gen2/og.py gen2/stage_outputs.sh "$OUT/gen2/"
find "$OUT" -type f | sort
