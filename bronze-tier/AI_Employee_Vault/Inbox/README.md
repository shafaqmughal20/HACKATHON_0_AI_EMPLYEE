---
type: guide
folder: inbox
---

# Inbox Folder

## Purpose
This is where new tasks and requests arrive. The AI Employee monitors this folder and processes items automatically.

## How to Use

### For Humans
1. Drop a new `.md` file here with your task/request
2. Use the template below
3. AI will process it within the next cycle
4. File will be moved to appropriate folder

### Task Template
```markdown
---
type: task
created: YYYY-MM-DD
priority: high|medium|low
deadline: YYYY-MM-DD (optional)
---

# Task Title

## Description
What needs to be done?

## Success Criteria
How do we know it's complete?

## Additional Context
Any relevant information, links, or requirements.
```

## Processing Rules
- AI checks this folder regularly
- New files trigger immediate processing
- Files are moved (not copied) to next stage
- Empty inbox = all caught up

## Examples

### Simple Task
```markdown
---
type: task
created: 2026-04-05
priority: medium
---

# Organize Project Files

Sort all files in Downloads folder by type and date.
```

### Complex Task (Needs Planning)
```markdown
---
type: task
created: 2026-04-05
priority: high
requires_planning: true
---

# Create Monthly Report

Generate comprehensive report including:
- Sales data
- Customer feedback
- Performance metrics
```

---
*Keep this folder clean - processed items are automatically moved*
