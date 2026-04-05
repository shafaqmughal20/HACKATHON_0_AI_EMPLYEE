---
type: guide
folder: logs
---

# Logs Folder

## Purpose
Complete audit trail of all AI Employee activities. Every action is logged here.

## Log Types

### 1. Daily Activity Log
**Filename**: `YYYY-MM-DD_daily.md`

```markdown
---
type: daily_log
date: YYYY-MM-DD
---

# Daily Activity Log - April 5, 2026

## Summary
- Tasks completed: X
- Tasks started: Y
- Approvals requested: Z
- Errors encountered: N

## Morning Cycle (00:00 - 12:00)
- 08:00 - Checked Inbox, found 2 new tasks
- 08:15 - Started task: [Task Name]
- 09:30 - Completed task: [Task Name]
- 10:00 - Created approval request for [Topic]

## Afternoon Cycle (12:00 - 18:00)
- 13:00 - Processed 3 items from Needs_Action
- 15:45 - Error encountered: [Description]
- 16:00 - Escalated to Pending_Approval

## Evening Cycle (18:00 - 24:00)
- 19:00 - Updated Dashboard
- 20:00 - Created plan for complex task
- 21:00 - End of day summary

## Metrics
- Response time: Avg X minutes
- Completion rate: Y%
- Error rate: Z%

## Learnings
- What worked well today
- What could be improved
- Patterns noticed

## Tomorrow's Focus
- Priority items for next day
```

### 2. Task Log
**Filename**: `YYYY-MM-DD_task_[TaskName].md`

```markdown
---
type: task_log
task_id: unique_id
date: YYYY-MM-DD
---

# Task Log: [Task Name]

## Timeline
- **Created**: 2026-04-05 08:00
- **Started**: 2026-04-05 08:15
- **Completed**: 2026-04-05 09:30
- **Duration**: 1h 15m

## Actions Taken
1. Action 1 - timestamp
2. Action 2 - timestamp
3. Action 3 - timestamp

## Decisions Made
- Decision 1: Rationale
- Decision 2: Rationale

## Challenges
- Challenge encountered and how resolved

## Outcome
Final result and status
```

### 3. Error Log
**Filename**: `YYYY-MM-DD_error_[Description].md`

```markdown
---
type: error_log
severity: high|medium|low
date: YYYY-MM-DD
resolved: yes|no
---

# Error Log: [Error Description]

## What Happened
Detailed description of the error

## When
Exact timestamp

## Context
What was being attempted

## Impact
What was affected

## Root Cause
Why it happened

## Resolution
How it was fixed (or escalated)

## Prevention
How to avoid in future
```

### 4. Weekly Summary
**Filename**: `YYYY-WXX_weekly_summary.md`

```markdown
---
type: weekly_summary
week: XX
year: 2026
---

# Weekly Summary - Week XX, 2026

## Overview
- Total tasks: X
- Completed: Y
- Success rate: Z%

## Highlights
- Major accomplishments
- Significant learnings

## Challenges
- Issues encountered
- How they were handled

## Metrics
- Average response time
- Completion rate
- Error rate
- Approval rate

## Improvements Made
- Process refinements
- New skills learned

## Next Week Focus
- Priorities
- Goals
```

## Logging Rules

### Must Log
- Every task start/completion
- All decisions made
- Errors and how resolved
- Approval requests
- Status changes
- File movements

### Log Format
- Use timestamps (HH:MM format)
- Be specific and factual
- Include relevant context
- Link to related files
- Note outcomes

### Retention
- Daily logs: Keep 90 days
- Task logs: Keep 180 days
- Error logs: Keep 1 year
- Weekly summaries: Keep indefinitely

## Why Logging Matters
- **Accountability**: Track what was done
- **Debugging**: Understand what went wrong
- **Learning**: Identify patterns
- **Metrics**: Measure performance
- **Audit**: Prove compliance
- **Improvement**: Data-driven optimization

---
*If it's not logged, it didn't happen*
