---
type: skill
name: Process Inbox Task
category: automation
difficulty: basic
created: 2026-04-05
last_used: 2026-04-05
success_rate: 100%
---

# Skill: Process Inbox Task

## Purpose
Automatically intake and route new tasks from the Inbox folder to the appropriate destination.

## When to Use
- New `.md` file appears in `Inbox/`
- Regular inbox monitoring cycle
- Manual inbox check requested

## Prerequisites
- Task file has proper frontmatter
- Task description is clear
- Success criteria defined (if applicable)

## Procedure

### 1. Read Task File
- Open the file completely
- Parse frontmatter metadata
- Read full description
- Note any special requirements

### 2. Validate Task
Check for required fields:
- [ ] `type: task` present
- [ ] `created` date present
- [ ] Task title exists
- [ ] Description is clear

### 3. Assess Complexity
**Simple Task** (→ Needs_Action):
- Clear, straightforward action
- No planning required
- Can execute immediately
- Low risk

**Complex Task** (→ Plans):
- Multi-step process
- Approach unclear
- Requires planning
- Significant impact

**Needs Approval** (→ Pending_Approval):
- Financial decision
- External communication
- Policy question
- High risk action

### 4. Route Task
Move file to appropriate folder:
```bash
# Simple task
mv Inbox/task.md Needs_Action/

# Complex task
mv Inbox/task.md Plans/

# Needs approval
mv Inbox/task.md Pending_Approval/
```

### 5. Update Metadata
Add routing information:
```yaml
processed_date: 2026-04-05
routed_to: folder_name
processed_by: ai
```

### 6. Log Activity
Create log entry in `Logs/`:
- Timestamp
- Task name
- Routing decision
- Reasoning

### 7. Update Dashboard
Increment appropriate counter:
- Needs Action count
- Plans count
- Pending Approval count

## Quality Checks
- [ ] Task file moved (not copied)
- [ ] Metadata updated
- [ ] Log entry created
- [ ] Dashboard updated
- [ ] Inbox is empty after processing

## Common Pitfalls

### Pitfall 1: Misrouting Complex Tasks
**Problem**: Sending complex task to Needs_Action
**Solution**: If uncertain, err on side of creating a plan first

### Pitfall 2: Missing Approval Requirements
**Problem**: Starting work that needs approval
**Solution**: Review Company_Handbook decision authority rules

### Pitfall 3: Incomplete Logging
**Problem**: Not documenting routing decision
**Solution**: Always log why task went to specific folder

## Decision Framework

```
Is it clear what to do?
├─ No → Plans/
└─ Yes
    └─ Does it need approval?
        ├─ Yes → Pending_Approval/
        └─ No → Needs_Action/
```

## Examples

### Example 1: Simple Task
```markdown
---
type: task
created: 2026-04-05
priority: medium
---

# Organize Downloads Folder
Sort files by type and date
```
**Decision**: → Needs_Action/ (clear, simple, no approval needed)

### Example 2: Complex Task
```markdown
---
type: task
created: 2026-04-05
priority: high
---

# Implement New Reporting System
Create monthly reports with data from 3 sources
```
**Decision**: → Plans/ (multi-step, needs planning)

### Example 3: Needs Approval
```markdown
---
type: task
created: 2026-04-05
priority: high
---

# Purchase Software License
Buy $500 annual subscription
```
**Decision**: → Pending_Approval/ (financial decision)

## Variations

### Batch Processing
When multiple tasks in Inbox:
1. Process by priority (high → medium → low)
2. Group similar tasks
3. Route all before starting execution

### Urgent Tasks
If `priority: high` and `deadline` is soon:
1. Process immediately
2. Flag in Dashboard
3. Notify if approval needed

## Related Skills
- [[Execute Simple Task]]
- [[Create Task Plan]]
- [[Request Approval]]
- [[Update Dashboard]]

## Success Metrics
- 100% of inbox items processed
- <5% misrouting rate
- All tasks logged
- Dashboard always current

---
**Last Updated**: 2026-04-05
**Times Used**: 1
**Success Rate**: 100%
