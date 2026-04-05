---
type: guide
folder: rejected
---

# Rejected Folder

## Purpose
Failed tasks, rejected work, and learning opportunities. This is the "lessons learned" folder.

## What Lives Here
- Tasks that didn't meet quality standards
- Rejected approval requests
- Failed attempts
- Work that needs significant revision

## Required Feedback
When moving here, human must add:
```yaml
status: rejected
rejected_date: YYYY-MM-DD
rejection_reason: Brief explanation
feedback: Detailed feedback for improvement
retry_allowed: yes|no
```

## Rejection Reasons Template
```markdown
## Rejection Feedback

### What Went Wrong
Clear explanation of the issue

### Expected vs Actual
- **Expected**: What should have happened
- **Actual**: What actually happened

### How to Improve
Specific guidance for next time

### Retry Instructions
If retry allowed:
- [ ] Fix issue X
- [ ] Verify Y
- [ ] Resubmit to `Needs_Action/`
```

## AI Learning Process
1. Read rejection feedback carefully
2. Understand the gap
3. Update approach
4. Document learning in `Logs/`
5. If retry allowed, create corrected version
6. Apply lesson to future similar tasks

## Common Rejection Reasons
- Incomplete work
- Misunderstood requirements
- Quality below standards
- Missed success criteria
- Unauthorized decisions
- Insufficient documentation

## Value of This Folder
- **Learning**: Mistakes are teachers
- **Improvement**: Identify weak areas
- **Prevention**: Avoid repeating errors
- **Calibration**: Understand expectations better

## Retry Process
If retry is allowed:
1. Create new task file
2. Reference original: `retry_of: rejected_task_id`
3. Apply feedback
4. Submit to `Needs_Action/`
5. Link to original rejection for context

---
*Failure is feedback - use it to improve*
