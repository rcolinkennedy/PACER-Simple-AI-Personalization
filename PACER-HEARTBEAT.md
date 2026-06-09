# PACER Heartbeat

An operational checklist for **scheduled, autonomous agent cycles** — runs that fire on a timer rather than a conversation. Each cycle: read `context/heartbeat-state.json`, run the tasks whose cadence is due, update the state file, and output `HEARTBEAT_OK` if there's nothing to escalate.

## When to Use This

The Heartbeat is optional. PACER works fine as a purely interactive system. Add a heartbeat when you want your agent to do recurring work without being asked — refreshing a status page, pulling your calendar each morning, writing a day-end summary, keeping memory tidy.

You need three things:

1. **A scheduler** — anything that can start an agent session on a timer (a scheduled-task feature in your agent platform, cron + CLI agent, etc.)
2. **A trigger marker** — the scheduled prompt should contain `[HEARTBEAT_SESSION]` so the agent knows to load this file and skip the interactive startup ritual (see `AGENTS.md`)
3. **This file, customized** — the cadences and tasks below are a template. Replace the examples with your own tools and rhythm.

## Cadence Tiers

Cadences are tags. Each scheduled run evaluates every tier against the current time and the `last_run` timestamps in `context/heartbeat-state.json`, then executes the tiers that are due. All times are local per the `timezone` field in the state file.

The times below are **example placeholders** — set your own.

| Tag | Fires when... |
|---|---|
| `@every-cycle` | Every run |
| `@daily` | First run at or after an early-morning anchor (e.g., 5 AM) |
| `@morning` | First run in a morning window (e.g., 6–8 AM) |
| `@workday` | Weekdays, at one or more working-hours windows (e.g., 8 AM, 12:30 PM, 3 PM). Each window fires once: first run at or after that time where `last_run` is before that window today. |
| `@evening` | Last run in an evening window (e.g., 9–11 PM) |
| `@weekly` | A chosen weekday, first run at or after a chosen time (e.g., Friday 1 PM) |

Add, remove, or rename tiers to fit your rhythm. The pattern is what matters: **a tag, an eligibility rule, and a `last_run` timestamp that prevents double-firing.**

### How often should the scheduler fire?

More often than your tightest window. If your `@morning` window is 6–8 AM, a run must land inside it — hourly or half-hourly scheduling is typical. `@every-cycle` work runs on every one of those, so keep it cheap.

---

## Cadence Evaluation Log

**This runs first, before any cadence executes.** On every heartbeat run:

1. Read `context/heartbeat-state.json` for all `last_run` timestamps
2. Determine current local time from the `timezone` field
3. Evaluate every cadence tier against its eligibility rules (time window, day-of-week, `last_run`)
4. Check for exceptions (below). **Only log to the daily file if an exception is found.** Normal runs where nothing is due produce no log entry — this keeps daily files lean when the heartbeat fires many times a day.
5. Execute the due cadences in order

### What triggers a log entry

Write a cadence evaluation entry to `memory/daily/YYYY-MM-DD.md` only when:

- **A cadence fires** — log which one and the `last_run` delta. Confirms normal operation. Example: `**HB eval 06:10:** @morning fired (last: 2026-01-14 06:05, 24h delta)`
- **A cadence was eligible but didn't execute** — the failure case this logging exists to catch. Example: `**HB eval 08:04:** ⚠️ @morning eligible (in window) but not executed`
- **A `last_run` timestamp is stale** — more than 2× the expected interval for that cadence (e.g., a daily tier not run in 48h, a weekly tier not run in 2 weeks).

### What stays silent

Runs where nothing is due and no timestamps are stale produce no entry. `@every-cycle` needs no evaluation logging — it fires every run by definition.

---

## @every-cycle

Cheap health checks that run on every single heartbeat. File reads only — no external API calls.

**Daily file check** — Verify `memory/daily/YYYY-MM-DD.md` exists for today. If missing, create it with a single header line: `# YYYY-MM-DD`. (Safety net — `@daily` should create it, but may not have run yet.)

**MEMORY.md line count** — Read `memory/MEMORY.md` and count lines. Thresholds (tune to taste):

- ≤ 110 lines: no action
- 111–130 lines: log `MEMORY.md at [N] lines — approaching compaction threshold` to today's daily file
- 131+ lines: log warning to daily file AND add to `TASKS.md` Next Session: `Compact MEMORY.md — at [N] lines (compaction overdue)`

If nothing is due and nothing needs reporting, output `HEARTBEAT_OK` and end.

---

## @daily

Once-a-day maintenance. Good candidates:

**Active Context refresh** — If you maintain an "active context" surface outside this repo (a page in `<your-active-context-store>` — Notion, Obsidian, a wiki, a plain hosted doc — that other agents or devices read), regenerate it from current PACER state:

- Sources: `memory/MEMORY.md`, `TASKS.md`, today's + yesterday's `memory/daily/*.md`
- Keep it small (~5K characters) and in whatever format the store renders well
- Only rewrite the body if state materially changed; always update a heartbeat timestamp footer: `*Last heartbeat: YYYY-MM-DD HH:MM [local TZ]*`

**Task sync** — Push the open sections of `TASKS.md` to your active-context surface, if you have one.

**External status reconciliation** — Cross-check `TASKS.md` Active and Waiting On items against their linked systems (`<your-issue-tracker>`, `<your-task-app>`, email, calendar). Completions win: move to Done with date and source. Ambiguous closures: flag in the daily file + Next Session. Log all auto-moves.

**MEMORY.md compaction** — The line-count pulse runs at `@every-cycle`; here, do the actual work: consolidate or remove stale entries until under 100 lines. Scan recent daily files for anything worth distilling into long-term memory.

**Daily log entry** — Append a heartbeat summary to `memory/daily/YYYY-MM-DD.md`:

```
**Heartbeat (automated):** [What happened, what was refreshed, any issues.]
```

---

## @morning

Start-of-day pull. Gather what the day looks like and surface it wherever you read it (a briefing file in `Outputs/`, a page in `<your-active-context-store>`, a message — your call). Example tasks:

**Calendar** — Pull today's events via `<your-calendar tool>`. Log a schedule summary. Flag conflicts or anything notable.

**Issue tracker** — Scan your active issues in `<your-issue-tracker>` (e.g., Linear, GitHub, Jira): status, recent comments, blockers, anything that moved since yesterday.

**Tasks** — Pull today's undone tasks from `<your-task-app>`. Flag overdue and high-priority items.

**Briefing** — Assemble the above into a morning briefing. Tip: keep the briefing's layout and formatting rules in a single config file (e.g., `context/briefing-config.md`) so the template lives in one place, not inline here.

Log a morning summary to the daily file.

---

## @workday

Working-hours check-ins, weekdays only. Use for mid-day updates: refresh the morning briefing with status changes, pick up any work you've queued for the agent, catch new items that arrived since the last window.

A single `last_run` timestamp gates all windows: if `last_run` is before the current window's time today, fire.

Append a workday summary to the daily file.

---

## @evening

Day-end wrap. Example tasks:

**End-of-day summary** — Append a brief summary to today's daily log: what the heartbeat observed across the day's cycles, escalations made, quiet signals worth noting.

**Cleanup** — Archive or prune anything that accumulates: completed items past a retention window, stale generated artifacts, etc.

---

## @weekly

Once-a-week jobs. Example tasks:

**Weekly review/update** — Generate a weekly summary per active project, saved to `Outputs/` (and/or published to `<your-active-context-store>`).

**Vacation gate** — Before running weekly tasks, check the calendar for a multi-day vacation covering the week. If so, skip and log "Weekly skipped — vacation."

---

## State File

`context/heartbeat-state.json` tracks the last completed run per cadence tier. Copy `context/heartbeat-state.json.example` to `context/heartbeat-state.json`, set your timezone, and leave the timestamps `null` — the heartbeat fills them in. The live file is personal state and is gitignored.

After completing the tasks for a cadence tier, write the current timestamp to that tier's `last_run` field. This is what makes runs idempotent.

---

## Escalation Rules

- **Log only** — routine observations, nominal status → daily file only
- **Escalate** — anything needing the user's attention → daily file AND `TASKS.md` Next Session section
- **HEARTBEAT_OK** — if a run finds nothing due and nothing to report, output this and end. No daily log entry needed.

## Behavior

- **Idempotent:** Safe to run multiple times. The state file prevents duplicate cadence-gated runs.
- **Autonomous:** No interactive questions. Make decisions; log ambiguity if needed.
- **Fail gracefully:** If a tool is unavailable or a source can't be read, log the failure in the daily file and continue with remaining tasks. Don't crash or retry indefinitely.
- **State update:** After completing a cadence tier's tasks, update its `last_run` in `context/heartbeat-state.json`.

---

## Make It Yours

Everything above the Escalation Rules is a template. Start with `@every-cycle` + `@daily` only, run it for a week, then add tiers as real needs appear. Resist adding tasks the heartbeat *could* do — every task runs unattended, so each one should earn its place.
