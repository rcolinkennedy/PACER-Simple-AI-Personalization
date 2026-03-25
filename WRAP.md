# WRAP.md

Session-end ritual. Run this when a session is closing.

---

## Triggers

### Auto mode — just do it

Run immediately, no review needed, when the user says things like:

- "we're done" / "that's it" / "that's all for now"
- "wrap up" / "wrap it up" / "end session"
- "good session" / "see you later" / "thanks, bye"
- "save this" / "commit this" / "lock it in"

### Review mode — show first, then write

Show a draft of what you'd save, wait for the user to confirm or adjust, then write:

- "what have you learned?" / "what did you learn?"
- "what would you remember?" / "what should we save?"
- "show me before you save" / "what are you taking away?"
- "did you get all that?"

Review mode is useful when the session covered something nuanced, sensitive, or where the user might want to add context before it's committed.

---

## Auto Mode — What to Do

1. **Append to `memory/daily/YYYY-MM-DD.md`** — write a short summary of what happened. Decisions made, things learned, context worth having next session. Distill, don't transcribe.

2. **Update `memory/MEMORY.md`** — only if something genuinely significant happened. New standing facts, changed context, important decisions. Leave it alone if nothing warrants it.

3. **Update entity files if relevant:**
   - `memory/projects/[name].md` — if a project moved forward
   - `memory/people/[name].md` — if something notable about a person came up
   - `memory/topics/[name].md` — if a topic deepened

4. **Flag `user/` suggestions** — if anything suggests a `user/` file should be updated (new voice example, changed preference, updated goal), say so. Don't write — propose.

5. **Refresh Notion Active Context** — If PACER state changed this session (project status, decisions, open threads), regenerate the Notion Active Context page (`32dc1a40-0ce6-81c5-ab27-cdda26ae1b2e`) from current PACER state. Skip if nothing material changed. Also ingest any new entries from the Session Handoff Log (`32dc1a40-0ce6-8152-8a22-d6ed5d7dd2a4`) that haven't been processed yet.

---

## Review Mode — What to Show

Present a draft before writing anything. Format it clearly:

**What I'd add to today's daily log:**
> [proposed entry]

**What I'd update in MEMORY.md (if anything):**
> [proposed change, or "nothing this session"]

**Entity file updates (if any):**
> [proposed changes]

**Suggestions for user/ files (if any):**
> [flag only — no writing without approval]

**Notion Active Context refresh (if PACER state changed):**
> [yes — regenerating from current state / no — nothing material changed this session]

Then ask: *"Anything to add or change before I save?"*

Once confirmed — write it all.

---

## What's Worth Capturing

Good candidates:
- Decisions made and why
- Things the user explicitly asked to remember
- Lessons that would change how you'd approach something next time
- New facts about people, projects, or recurring topics
- Context that would be confusing to lose

Skip:
- Details that won't matter next session
- Routine task completions with no lasting implications
- Secrets — unless explicitly asked to keep them
- Raw back-and-forth — distill, don't log

---

## Memory Maintenance

Occasionally (every few sessions), during a wrap:

1. Scan recent `memory/daily/` files
2. Pull anything worth keeping long-term into `memory/MEMORY.md`
3. Remove entries from `memory/MEMORY.md` that are stale or no longer relevant

Keep `memory/MEMORY.md` under 100 lines. It's curated wisdom, not a running archive.
