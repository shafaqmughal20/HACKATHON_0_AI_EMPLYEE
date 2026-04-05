---
type: guide
folder: needs_action
---

# Needs Action Folder

## Purpose
Tasks that are ready to execute immediately. No planning required - just do it.

## Characteristics
- Clear, actionable tasks
- All information available
- No approval needed to start
- Can be completed independently

## AI Behavior
- Picks tasks from here to work on
- Updates status to `in_progress`
- Moves to `Done/` when complete
- Logs all activity

## Task States
Tasks here should have:
```yaml
status: pending
assigned_to: ai
```

## Examples of Tasks Here
- File organization
- Data formatting
- Report generation (with template)
- Routine updates
- Document creation

## Not Here
- Tasks needing approval → `Pending_Approval/`
- Tasks needing planning → `Plans/`
- Completed tasks → `Done/`

---
*AI processes this folder by priority: high → medium → low*
