#!/usr/bin/env bash
# 1) catat session id, dipakai nosm-sync-check untuk menulis penanda terverifikasi
# 2) suntikkan satu baris penunjuk (tanpa menyalin aturan apa pun)
set -uo pipefail
IN=$(cat)
SID=$(printf '%s' "$IN" | jq -r '.session_id // ""')
[ -n "$SID" ] && { mkdir -p "$HOME/.claude"; printf '%s' "$SID" > "$HOME/.claude/nosm-current-session"; }
printf '%s' '{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"Sebelum pekerjaan BO 建设／流程建设 apa pun di repo ini: jalankan skill `nosm-sync-check`, lalu skill `bo-build`. Aturannya ada di sana, bukan di pesan ini. Jawab hanya setelah membaca dan memahami sumber resminya; sampaikan rekomendasi beserta alasan dan dasarnya. Jangan mulai mengeksekusi task tanpa persetujuan pengguna."}}'
