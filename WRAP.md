# WRAP.md

Session-end ritual. Run this when a session is closing.

---

## Triggers

**Auto mode** — User signals the session is over (e.g. "wrap it up"). Execute immediately, no review needed.

**Review mode** — User asks to see what you'd save before you write it (e.g. "what did you learn?"). Show a draft, wait for confirmation, then write.

---

## Auto Mode — What to Do

1. **Append to `memory/daily/YYYY-MM-DD.md`** — write a short summary of what happened. Decisions made, things learned, context worth having next session. Distill, don't transcribe.

2. **Update `TASKS.md`** — review the session for task changes:
   - Mark completed items done (move to Done with date)
   - Add new items surfaced during the session (commitments, follow-ups, action items)
   - Move items between sections if status changed (e.g., Active → Waiting On)
   - Add items to Next Session for anything that should be picked up immediately next time

3. **Sync tasks to Notion Active Context** — push the Active, Waiting On, and Next Session sections from `TASKS.md` to the "Open Items" section on the Notion Active Context page (`32dc1a40-0ce6-81c5-ab27-cdda26ae1b2e`). Format as simple bulleted list using Notion-compatible blocks. This is how Lite embodiments see current task state.

4. **Update `memory/MEMORY.md`** — only if something genuinely significant happened. New standing facts, changed context, important decisions. Leave it alone if nothing warrants it.

5. **Update entity files if relevant:**
   - `memory/projects/[name].md` — if a project moved forward
   - `memory/people/[name].md` — if something notable about a person came up
   - `memory/topics/[name].md` — if a topic deepened

6. **Flag `user/` suggestions** — if anything suggests a `user/` file should be updated (new voice example, changed preference, updated goal), say so. Don't write — propose.

---

## Review Mode — What to Show

Present a draft before writing anything:

```
Daily log: [entry]
MEMORY.md: [change or "no change"]
Entity updates: [changes or "none"]
user/ suggestions: [proposals or "none"]

Anything to adjust?
```

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
