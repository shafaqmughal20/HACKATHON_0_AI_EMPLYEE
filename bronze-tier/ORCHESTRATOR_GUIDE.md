# Orchestrator Guide - Bronze Tier

## 🎯 What is the Orchestrator?

The orchestrator is a simple Python script that helps you work through tasks in your AI Employee vault. It's like a task manager that:
- Shows you what needs to be done
- Presents tasks one at a time
- Helps you mark tasks as complete
- Moves finished work to the Done/ folder

**Think of it as your AI Employee's "work session" tool.**

---

## 🚀 How to Use

### Step 1: Start the Orchestrator

```bash
cd "/mnt/d/New folder/AI_Emplyee_Vault"
python orchestrator.py AI_Employee_Vault
```

### Step 2: Review the Task

The orchestrator will show you:
- Task filename
- Task title
- Priority level
- Current status
- Task content preview

### Step 3: Execute the Task

Use Claude Code to help you complete the task:
- Read what needs to be done
- Execute the required actions
- Verify the work is complete

### Step 4: Mark as Done

When finished, choose option `[d]` to:
- Update task status to "done"
- Add completion timestamp
- Move file to Done/ folder
- Log the activity

### Step 5: Repeat

The orchestrator automatically shows you the next task.

---

## 📋 Orchestrator Options

When viewing a task, you have these options:

### [d] Mark as Done
- Marks task complete
- Adds timestamp
- Moves to Done/ folder
- Logs completion
- Shows next task

### [s] Skip
- Leaves task in Needs_Action/
- Shows next task
- Use when you need to come back later

### [v] View Full Content
- Shows complete task file
- Useful for long tasks
- Returns to options menu

### [q] Quit
- Exits orchestrator
- Shows final summary
- Tasks remain in place

---

## 🎬 Example Session

```
==================================================================
🤖 Bronze-tier AI Employee Orchestrator
==================================================================

This orchestrator helps you work through tasks in Needs_Action/
It will show you each task, and you can mark it done when complete.

==================================================================
📊 CURRENT STATUS SUMMARY
==================================================================
📋 Tasks in Needs_Action/: 3
✅ Tasks in Done/: 5

📌 Next task: 2026-04-05_OrganizeFiles.md
==================================================================

==================================================================
📋 TASK 1/3
==================================================================
📄 File: 2026-04-05_OrganizeFiles.md
📌 Title: Organize Downloads Folder
⚡ Priority: MEDIUM
📊 Status: pending
🏷️  Type: task
==================================================================

---
type: task
created: 2026-04-05
priority: medium
status: pending
---

# Organize Downloads Folder

## Description
Sort all files in Downloads folder by type and date.

## Success Criteria
- All files categorized
- Proper naming convention
- Index created

==================================================================

==================================================================
🎯 WHAT TO DO:
==================================================================
1. Read the task above
2. Execute the task (use Claude Code to help)
3. When done, come back here
==================================================================

Options:
  [d] Mark as Done and move to Done/
  [s] Skip this task for now
  [v] View full task file
  [q] Quit orchestrator

Your choice: d

✅ Task moved to Done/: 2026-04-05_OrganizeFiles.md

✅ Task marked as done!

Press Enter to continue to next task...
```

---

## 🔄 Typical Workflow

### Morning Session
```bash
# Start orchestrator
python orchestrator.py AI_Employee_Vault

# Work through high priority tasks
# Mark each as done when complete
# Quit when done or taking a break
```

### Throughout the Day
```bash
# Files drop into Inbox/
# Filesystem watcher detects them
# Creates tasks in Needs_Action/

# Run orchestrator when ready to work
python orchestrator.py AI_Employee_Vault
```

### End of Day
```bash
# Final orchestrator session
# Complete remaining tasks
# Review summary
# Check Done/ folder for review
```

---

## 💡 Tips

### For Best Results
1. **Focus on one task at a time** - Don't multitask
2. **Use Claude Code** - Let AI help execute tasks
3. **Verify completion** - Check success criteria before marking done
4. **Take breaks** - Use [s] to skip and come back later
5. **Review Done/** - Check completed work regularly

### Task Execution Pattern
```
1. Orchestrator shows task
2. Read requirements carefully
3. Ask Claude Code to help execute
4. Verify work is complete
5. Mark as done in orchestrator
6. Move to next task
```

### When to Skip
- Task is blocked by another task
- Waiting on external information
- Need more time to think
- Taking a break

### When to Quit
- End of work session
- Need to do something else
- All tasks complete
- Taking a longer break

---

## 🎯 What Happens Behind the Scenes

### When You Mark a Task Done

1. **Updates Frontmatter**
   ```yaml
   status: pending → status: done
   completed: 2026-04-05 19:47:36
   ```

2. **Moves File**
   ```
   Needs_Action/task.md → Done/task.md
   ```

3. **Logs Activity**
   ```
   Logs/2026-04-05_daily.md:
   - 19:47:36 - Completed task: task.md
   ```

4. **Shows Next Task**
   - Automatically presents next item
   - Keeps you in flow

---

## 📊 Status Summary

The orchestrator shows you:
- **Tasks in Needs_Action/**: What's pending
- **Tasks in Done/**: What's completed today
- **Next task**: What you'll work on

This helps you:
- See progress
- Know what's left
- Stay motivated

---

## 🔧 Advanced Usage

### Run with Custom Path
```bash
python orchestrator.py /path/to/vault
```

### Check Status Without Running
```bash
ls -la AI_Employee_Vault/Needs_Action/
ls -la AI_Employee_Vault/Done/
```

### View Task Without Orchestrator
```bash
cat AI_Employee_Vault/Needs_Action/task.md
```

---

## 🚨 Troubleshooting

### No Tasks Showing
**Issue**: Orchestrator says "No tasks in Needs_Action/"
**Solution**: 
- Check if files are in Inbox/ (need to be routed)
- Run filesystem watcher to process inbox
- Manually move tasks to Needs_Action/

### Can't Mark Task Done
**Issue**: Error when marking done
**Solution**:
- Check file permissions
- Verify Done/ folder exists
- Check file isn't locked

### Task Disappeared
**Issue**: Task not showing up
**Solution**:
- Check Done/ folder (might be already complete)
- Check if filename is README.md (ignored)
- Verify file has .md extension

---

## 🎓 Integration with Other Tools

### With Filesystem Watcher
```bash
# Terminal 1: Run watcher (continuous)
python filesystem_watcher.py AI_Employee_Vault

# Terminal 2: Run orchestrator (when ready to work)
python orchestrator.py AI_Employee_Vault
```

### With Claude Code
```bash
# Start orchestrator
python orchestrator.py AI_Employee_Vault

# When task appears, ask Claude Code:
"Please help me complete this task: [describe task]"

# After Claude Code completes it:
# Mark as done in orchestrator
```

---

## 📈 Measuring Productivity

Track these metrics:
- **Tasks completed per session**
- **Time per task** (estimate)
- **Tasks remaining**
- **Completion rate**

The orchestrator helps by:
- Showing clear progress
- Logging completions
- Maintaining focus
- Preventing task switching

---

## 🎯 Bronze Tier Philosophy

The orchestrator is intentionally simple:
- ✅ Manual operation (you control when to work)
- ✅ One task at a time (focus)
- ✅ Clear status (no confusion)
- ✅ Simple workflow (easy to understand)

**Not included** (that's for Silver/Gold tier):
- ❌ Automatic execution
- ❌ Parallel processing
- ❌ AI decision making
- ❌ Complex scheduling

---

## 🚀 Quick Reference

```bash
# Start orchestrator
python orchestrator.py AI_Employee_Vault

# Options when viewing task:
[d] - Mark done and continue
[s] - Skip to next task
[v] - View full content
[q] - Quit orchestrator

# Files moved:
Needs_Action/task.md → Done/task.md

# Logs updated:
Logs/YYYY-MM-DD_daily.md
```

---

**Remember**: The orchestrator is your work session tool. Run it when you're ready to work through tasks, and it will guide you through them one by one.

**Status**: 🟢 Ready to Use
**Complexity**: Bronze (Simple)
**Mode**: Manual/Interactive
