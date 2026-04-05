---
type: guide
folder: done
---

# Done Folder

## Purpose
Completed tasks awaiting human review and approval.

## What Lives Here
- Finished work
- Tasks marked complete by AI
- Awaiting quality check
- Ready for approval/rejection

## Required Updates
When AI moves task here, it must add:
```yaml
status: done
completed_date: YYYY-MM-DD
completion_notes: Brief summary of what was done
```

## Human Review Process
1. Review completed work
2. Check against success criteria
3. Verify quality
4. Decision:
   - ✅ Approve → Move to `Approved/`
   - ❌ Reject → Move to `Rejected/` with feedback
   - 🔄 Revise → Move back to `Needs_Action/` with notes

## AI Self-Check Before Moving Here
- [ ] Objective achieved
- [ ] Success criteria met
- [ ] Quality standards followed
- [ ] Documentation complete
- [ ] Log entry created

## Completion Template
```markdown
## Completion Summary
**Completed**: 2026-04-05
**Time Spent**: X hours
**Outcome**: Brief description

### What Was Done
- Action 1
- Action 2
- Action 3

### Results
- Result 1
- Result 2

### Notes
Any relevant observations or learnings
```

---
*This folder is the quality gate - nothing is truly complete until reviewed*
