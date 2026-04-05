---
type: guide
folder: plans
---

# Plans Folder

## Purpose
Complex tasks that require planning before execution. AI creates detailed plans here for review.

## When Tasks Come Here
- Multi-step processes
- Uncertain approach
- Significant impact
- Resource requirements unclear

## Plan Template
```markdown
---
type: plan
created: YYYY-MM-DD
status: draft|approved|in_progress
task_id: original_task_reference
---

# Plan: [Task Name]

## Objective
What we're trying to achieve

## Current Situation
What exists now

## Proposed Approach
Step-by-step plan:
1. Step one
2. Step two
3. Step three

## Resources Needed
- Time estimate
- Tools required
- Dependencies

## Risks & Mitigation
- Risk 1: mitigation strategy
- Risk 2: mitigation strategy

## Success Criteria
How we measure completion

## Approval Required?
Yes/No - explain why
```

## Workflow
1. AI creates plan
2. Moves to `Pending_Approval/` if needed
3. Once approved, executes plan
4. Updates progress in plan file
5. Moves to `Done/` when complete

---
*Plans ensure complex work is well thought out before execution*
