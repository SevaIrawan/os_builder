#!/usr/bin/env bash
# Gerbang NOSM. Menolak tulisan ke objek yang diatur doc NOSM selama skill
# nosm-sync-check belum dijalankan di session ini.
# Penanda ditulis oleh nosm-sync-check setelah verifikasi selesai.
set -uo pipefail

IN=$(cat)
TOOL=$(printf '%s' "$IN" | jq -r '.tool_name // ""')
SID=$(printf '%s' "$IN" | jq -r '.session_id // "unknown"')
FP=$(printf '%s' "$IN" | jq -r '.tool_input.file_path // ""')

# sudah diverifikasi di session ini -> lolos
[ -f "$HOME/.claude/nosm-sync-verified/$SID" ] && exit 0

case "$TOOL" in
  Edit|Write|NotebookEdit)
    # hanya file yang diatur doc NOSM; file lain bebas
    case "$FP" in
      */CLAUDE.md|*/docs/04-anchor-navigation.md|*/.claude/skills/*) ;;
      *) exit 0 ;;
    esac
    ;;
  mcp__*Rovo*createConfluencePage|mcp__*Rovo*updateConfluencePage|\
  mcp__*Rovo*createJiraIssue|mcp__*Rovo*editJiraIssue|\
  mcp__*Rovo*transitionJiraIssue|mcp__*Rovo*addCommentToJiraIssue|\
  mcp__n8n__create_workflow_from_code|mcp__n8n__update_workflow|\
  mcp__n8n__publish_workflow|mcp__n8n__unpublish_workflow|\
  mcp__n8n__execute_workflow|mcp__n8n__archive_workflow)
    ;;
  *) exit 0 ;;
esac

jq -nc --arg t "$TOOL" '{
  hookSpecificOutput: {
    hookEventName: "PreToolUse",
    permissionDecision: "deny",
    permissionDecisionReason: ("Gerbang NOSM: skill nosm-sync-check belum dijalankan di session ini, jadi " + $t + " ditolak. Jalankan skill nosm-sync-check lebih dulu, lalu bo-build. Aturannya ada di skill itu, bukan di pesan ini.")
  }
}'
