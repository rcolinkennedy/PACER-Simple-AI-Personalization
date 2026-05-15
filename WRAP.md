# WRAP.md

Session-end ritual. Run this when a session is closing.

---

## Triggers

### Proactive (primary)

After substantive work — decisions made, tasks completed, things learned, context worth preserving — the agent initiates the wrap. Don't wait for the user to remember.

**When to trigger:** When the session has produced something worth capturing *and* the conversation is winding down. Signs: natural pause after completing a multi-step task, the user shifting to a different topic or saying goodbye, end of a planning or triage session, or a long idle gap after meaningful work.

**When NOT to trigger:** Mid-task, mid-conversation, or when the session has been purely conversational with nothing to persist. Don't interrupt flow.

**How:** Ask briefly — e.g. "Good stopping point — want me to wrap this session?" If yes, run auto mode. If the user says "show me first," run review mode.

### Manual (fallback)

These still work if the user invokes them directly:

**Auto mode** — User signals the session is over (e.g. "wrap it up," "we're done," "that's all for now"). Execute immediately, no review needed.

**Review mode** — User asks to see what you'd save before you write it (e.g. "what did you learn?," "show me before you save"). Show a draft, wait for confirmation, then write.

---

## Auto Mode — What to Do

1. **Append to `memory/daily/YYYY-MM-DD.md`** — write a short summary of what happened. Decisions made, things learned, context worth having next session. Distill, don't transcribe.

2. **Update `TASKS.md`** — review the session for task changes:
   - Mark completed items done (move to Done with date)
   - Add new items surfaced during the session (commitments, follow-ups, action items)
   - Move items between sections if status changed (e.g., Active → Waiting On)
   - Add items to Next Session for anything that should be picked up immediately next time

3. **Update `memory/MEMORY.md`** — only if something genuinely significant happened. New standing facts, changed context, important decisions. Leave it alone if nothing warrants it.

4. **Update entity files if relevant:**
   - `memory/projects/[name].md` — if a project moved forward
   - `memory/people/[name].md` — if something notable about a person came up
   - `memory/topics/[name].md` — if a topic deepened

5. **Flag `user/` suggestions** — if anything suggests a `user/` file should be updated (new voice example, changed preference, updated goal), say so. Don't write — propose.

---

## Review Mode — What to Show

Present a draft before writing anything. Format it clearly:

**What I'd add to today's daily log:**
> [proposed entry]

**Task changes:**
> [completions, new items, moves — or "no changes"]

**What I'd update in MEMORY.md (if anything):**
> [proposed change, or "nothing this session"]

**Entity file updates (if any):**
> [proposed changes]

**Suggestions for user/ files (if any):**
> [flag only — no writing without approval]

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
