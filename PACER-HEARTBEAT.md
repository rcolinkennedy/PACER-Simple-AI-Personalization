# PACER Heartbeat

Operational checklist for scheduled heartbeat cycles. Each cycle: read `context/heartbeat-state.json`, run tasks whose cadence is due, update state, output `HEARTBEAT_OK` if nothing to escalate.

## Cadence Tiers

All times are local per the `timezone` field in `context/heartbeat-state.json`.

| Tag | Fires when... |
|---|---|
| `@every-cycle` | Every run |
| `@daily` | First run at or after 5 AM |
| `@breakfast` | First run in 6–9 AM window |
| `@bedtime` | Last run in 9 PM–midnight window |
| `@weekly` | Friday, first run at or after 1 PM |

## Notion Page IDs

- **Session Handoff Log:** `32dc1a40-0ce6-8152-8a22-d6ed5d7dd2a4`
- **Active Context:** `32dc1a40-0ce6-81c5-ab27-cdda26ae1b2e`

---

## @every-cycle

No tasks in v1. Output `HEARTBEAT_OK` if no other cadence tiers are due.

---

## @daily

**Lite handoff ingestion** — Read the Notion Session Handoff Log. Compare by date and content — if an entry's substance already appears in the daily log for that date, skip it. For each new entry:
- Append a summary to the appropriate daily file (attribute as "Lite session:" or "Notion Agent:")
- Update `memory/MEMORY.md` and entity files (`memory/projects/`, `memory/people/`, `memory/topics/`) if warranted
- Respect `Sync priority: elevated` — ensure those facts reach Active Context prominently
- **Never touch `user/`**

**Active Context refresh** — Regenerate the Notion Active Context page from current PACER state:
- Sources: `memory/MEMORY.md`, `TASKS.md`, today's + yesterday's `memory/daily/*.md`
- ~5K characters max, Notion-compatible blocks (headings, bullets, paragraphs — no markdown tables or code blocks)
- Only rewrite page body if state materially changed; always update the heartbeat timestamp footer:
  `*Last heartbeat: YYYY-MM-DD HH:MM [local TZ abbreviation]*`

**Handoff log culling** — Keep 5–7 recent entries in the Session Handoff Log, under ~8K chars. Remove oldest. Preserve page structure.

**Task sync** — Push `TASKS.md` Active + Waiting On + Next Session sections to the "Open Items" section on Active Context. Format as simple bulleted list.

**External status reconciliation** — After task sync, cross-check TASKS.md Active and Waiting On items against current status in their linked systems (Linear, ClickUp, Gmail, Calendar). Completions win: move to Done with date and source. Ambiguous closures (e.g., tracking issue closed but underlying work continues elsewhere): flag in daily file + Next Session. Log all auto-moves to daily file.

**MEMORY.md health** — Check `memory/MEMORY.md` line count (target: under 100). Flag stale entries for review. Scan recent daily files for anything worth distilling into long-term memory.

**Daily log entry** — Append heartbeat summary to `memory/daily/YYYY-MM-DD.md`:
```
**Heartbeat (automated):** [What happened — entries ingested or "no new entries", Active Context status, handoff log status, any issues.]
```

---

## @breakfast

**Google Calendar** — Pull today's events via Google Calendar MCP. Log schedule summary. Flag conflicts, OOO blocks, or anything notable.

**Gmail** — Check starred/flagged threads. Log any requiring attention. Escalate threads waiting on replies beyond a reasonable window.

**Linear full pull** — Scan all active RCK issues: status, recent comments, blockers, anything that moved since last breakfast. More comprehensive than the `@every-cycle` status check.

**ClickUp** — Check AI-Delegated list (`901319471366`) for new items. Check active project spaces from MEMORY.md (AI Assisted, Product Briefly, Projects) for task status changes.

**Active Context status reconciliation** — Fetch the Notion Active Context page. Find all referenced RCK-## issues and ClickUp task IDs. Query Linear and ClickUp for current status of each. Update any stale statuses in place on the page (weekly plan table, Open Threads, Open Items). Preserve page structure — update status fields only, don't delete or reorder content.

**Daily log check** — Verify `memory/daily/YYYY-MM-DD.md` exists for today. Create if missing.

Log a breakfast summary to the daily file.

---

## @bedtime

**End-of-day summary** — Append a brief summary to today's daily log: what the heartbeat observed across the day's cycles, any escalations made, any quiet signals worth noting.

---

## @weekly

**Vacation gate** — Check Google Calendar for multi-day vacation events covering this week (not just a long weekend or single OOO day). If Colin is on vacation for the week, skip the weekly update below and log "Weekly update skipped — vacation" to daily file. Regular OOO days and long weekends still get updates.

**Weekly project updates** — Generate weekly updates per `skills/rck-weekly-update/SKILL.md`. Run once per active project that had activity this week. Output to Notion Project Updates database + `Outputs/` markdown. For Personal AI System, also syndicate status to Linear.

---

## Escalation Rules

- **Log only** — routine observations, nominal status → daily file only
- **Escalate** — anything needing Colin's attention → daily file AND add to `TASKS.md` Next Session section
- **HEARTBEAT_OK** — if an `@every-cycle` run finds nothing due and nothing to report, output this and end. No daily log entry needed.

## Behavior

- **Idempotent:** Safe to run multiple times. State file prevents duplicate cadence-gated runs.
- **Autonomous:** No interactive questions. Make decisions, log ambiguity if needed.
- **Fail gracefully:** If an MCP tool is unavailable or a page can't be read, log the failure in the daily file and continue with remaining tasks. Don't crash or retry indefinitely.
- **State update:** After completing tasks for a cadence tier, write the current timestamp to `context/heartbeat-state.json` for that tier.
