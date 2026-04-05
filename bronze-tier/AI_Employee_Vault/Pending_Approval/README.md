---
type: guide
folder: pending_approval
---

# Pending Approval Folder

## Purpose
Items requiring human decision or approval before proceeding.

## What Comes Here
- Major decisions
- Uncertain situations
- High-impact actions
- Budget/spending requests
- External communications
- Policy questions
- Complex plans
- Error escalations

## Approval Request Template
```markdown
---
type: approval_request
created: YYYY-MM-DD
priority: high|medium|low
decision_needed_by: YYYY-MM-DD (optional)
---

# Approval Request: [Topic]

## What Needs Approval
Clear statement of what you're asking

## Context
Why this needs approval and relevant background

## Options
1. **Option A**: Description
   - Pros: ...
   - Cons: ...
   
2. **Option B**: Description
   - Pros: ...
   - Cons: ...

## AI Recommendation
Which option and why

## Impact if Delayed
What happens if decision is delayed

## Questions to Answer
- Question 1?
- Question 2?

---
## Decision
**Status**: pending|approved|rejected
**Date**: 
**Decision**: 
**Notes**: 
```

## Human Response Process
1. Review the request
2. Update the Decision section
3. Move to appropriate folder:
   - Approved → `Approved/` or back to `Needs_Action/`
   - Rejected → `Rejected/` with explanation

## AI Behavior
- Waits for decision
- Does NOT proceed without approval
- Checks this folder regularly
- Implements decision once made

## Priority Handling
- **High**: Check within 4 hours
- **Medium**: Check within 24 hours
- **Low**: Check within 3 days

---
*When in doubt, ask for approval - better safe than sorry*
