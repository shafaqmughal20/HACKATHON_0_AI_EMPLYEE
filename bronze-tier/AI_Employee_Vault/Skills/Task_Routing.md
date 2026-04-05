---
type: skill
name: Task Routing
category: automation
difficulty: basic
created: 2026-04-05
last_used: 2026-04-05
success_rate: 100%
---

# Skill: Task Routing

## Purpose
Intelligently route incoming tasks from Inbox to the correct folder based on complexity, requirements, and approval needs.

## When to Use
- Processing new items in Inbox/
- Triaging work requests
- Organizing workflow
- Every time a new task arrives

## Prerequisites
- Read access to Inbox/
- Write access to all workflow folders
- Understanding of Company_Handbook rules
- Knowledge of task complexity assessment

## Procedure

### 1. Read Task File
```
1. Open task file from Inbox/
2. Parse frontmatter metadata
3. Read full description
4. Note any special requirements
5. Check for deadline or priority
```

### 2. Validate Task Format
```
Required fields:
- [ ] type: task
- [ ] created: date
- [ ] Task title present
- [ ] Description clear

If missing:
- Add missing metadata
- Log validation issue
- Proceed with routing
```

### 3. Assess Task Complexity
```
Simple Task Indicators:
✅ Single, clear action
✅ No planning needed
✅ Can execute immediately
✅ Low risk
✅ Familiar task type
✅ <30 minutes estimated

Complex Task Indicators:
⚠️ Multiple steps required
⚠️ Approach unclear
⚠️ Requires research
⚠️ High impact
⚠️ New task type
⚠️ >30 minutes estimated
```

### 4. Check Approval Requirements
```
Requires Approval if:
❌ Financial decision
❌ External communication
❌ Deleting data
❌ Sensitive information
❌ Strategic decision
❌ High risk action
❌ Uncertain about approach
❌ Outside defined scope

Reference Company_Handbook Section 6 for full list.
```

### 5. Determine Destination
```
Decision Tree:

Does it need approval?
├─ Yes → Pending_Approval/
└─ No
    └─ Is it complex?
        ├─ Yes → Plans/
        └─ No → Needs_Action/
```

### 6. Update Task Metadata
```
Add routing information:
---
processed_date: YYYY-MM-DD
processed_time: HH:MM:SS
routed_to: folder_name
routed_by: ai
routing_reason: brief explanation
---
```

### 7. Move Task File
```
1. Determine destination folder
2. Check destination exists
3. Move file (not copy)
4. Verify move succeeded
5. Confirm file in new location
6. Verify Inbox file removed
```

### 8. Log Routing Decision
```
Log entry should include:
- Task name
- Source: Inbox
- Destination: folder
- Reason: why routed there
- Timestamp
- Any special notes
```

### 9. Update Dashboard
```
Increment appropriate counter:
- Needs_Action count +1
- Plans count +1
- Pending_Approval count +1

Update last activity timestamp.
```

## Quality Checks
- [ ] Task file read completely
- [ ] Complexity assessed correctly
- [ ] Approval requirements checked
- [ ] Destination determined logically
- [ ] Metadata updated
- [ ] File moved successfully
- [ ] Routing logged
- [ ] Dashboard updated
- [ ] Inbox is clean

## Common Pitfalls

### Pitfall 1: Underestimating Complexity
**Problem**: Sending complex task to Needs_Action
**Solution**: When uncertain, err on side of creating a plan

### Pitfall 2: Missing Approval Requirements
**Problem**: Starting work that needs approval
**Solution**: Review Company_Handbook decision authority rules

### Pitfall 3: Incomplete Routing
**Problem**: File moved but not logged
**Solution**: Always complete all steps, including logging

### Pitfall 4: Wrong Destination
**Problem**: Task in wrong folder
**Solution**: Re-assess and move to correct location

## Decision Framework

```
┌─────────────────┐
│  New Task File  │
│   in Inbox/     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Read & Validate │
└────────┬────────┘
         │
         ▼
    ┌────────┐
    │Approval│
    │Needed? │
    └───┬────┘
        │
    Yes │ No
        │
    ┌───▼────────────┐  ┌──────────┐
    │ Pending_       │  │ Complex? │
    │ Approval/      │  └────┬─────┘
    └────────────────┘       │
                         Yes │ No
                             │
                    ┌────────▼──┐  ┌──────────┐
                    │  Plans/   │  │ Needs_   │
                    │           │  │ Action/  │
                    └───────────┘  └──────────┘
```

## Examples

### Example 1: Simple Task → Needs_Action
```
Task: "Organize Downloads folder"

Assessment:
✅ Clear action
✅ No approval needed
✅ Can do immediately
✅ Low risk

Decision: → Needs_Action/
Reason: Simple, routine file organization
```

### Example 2: Complex Task → Plans
```
Task: "Create monthly performance dashboard"

Assessment:
⚠️ Multiple steps (gather data, calculate metrics, format)
⚠️ Need to design structure
⚠️ First time doing this
⚠️ ~2 hours estimated

Decision: → Plans/
Reason: Complex, requires planning before execution
```

### Example 3: Sensitive Task → Pending_Approval
```
Task: "Delete old customer data files"

Assessment:
❌ Deleting data
❌ Potentially sensitive information
❌ Irreversible action

Decision: → Pending_Approval/
Reason: Destructive action with data, requires human approval
```

### Example 4: Uncertain Task → Pending_Approval
```
Task: "Update company website"

Assessment:
❌ External-facing
❌ Not sure if I have authority
❌ Could impact business

Decision: → Pending_Approval/
Reason: Uncertain about scope and authority, better to ask
```

## Variations

### Quick Routing (Obvious Cases)
- Immediate decision
- Clear destination
- Minimal logging

### Careful Routing (Uncertain Cases)
- Thorough assessment
- Review handbook rules
- Detailed logging
- Consider creating approval request

### Batch Routing (Multiple Tasks)
- Process all inbox items
- Group similar tasks
- Route in priority order
- Aggregate logging

## Related Skills
- [[Process_Inbox_Task]] - Original inbox processing skill
- [[File_Organization]] - Organize routed tasks
- [[Report_Generation]] - Report on routing metrics

## Success Metrics
- 100% of inbox items routed
- <5% misrouting rate (tasks moved to wrong folder)
- All routing decisions logged
- Dashboard always current
- No tasks stuck in Inbox

## Routing Statistics to Track
- Total tasks routed
- Breakdown by destination:
  - Needs_Action: X%
  - Plans: Y%
  - Pending_Approval: Z%
- Average routing time
- Misrouting rate
- Most common task types

## Notes
- When in doubt, choose Plans/ or Pending_Approval/
- Better to over-plan than under-plan
- Better to ask approval than assume authority
- Learn from misrouting - update this skill
- Keep Inbox empty - route everything

---
**Last Updated**: 2026-04-05
**Times Used**: 1
**Success Rate**: 100%
**Estimated Time**: 2-5 minutes per task
