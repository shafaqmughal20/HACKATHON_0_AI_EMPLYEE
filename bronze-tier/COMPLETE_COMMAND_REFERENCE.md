# 🚀 Bronze-Tier AI Employee - Complete Command Reference

**Last Updated**: 2026-04-06
**System Status**: ✅ Fully Operational

---

## 📊 Current System Status

### ✅ What's Working
- **Python Scripts**: 3 files ready (base_watcher.py, filesystem_watcher.py, orchestrator.py)
- **Total Files**: 48 markdown files created
- **Vault Structure**: All 10 folders operational
- **Skills Library**: 5 production skills ready
- **Documentation**: Complete

### 📁 Current Folder Status
```
Inbox/           3 files (including test files)
Needs_Action/    1 file (test_task.txt - ready to process!)
Plans/           0 files
Done/            25 files (system files moved here)
Pending_Approval/ 0 files
Approved/        0 files
Rejected/        0 files
Logs/            2 files
Skills/          5 files
```

---

## 🎯 PART 1: Daily Workflow Commands

### Morning Startup

```bash
# 1. Navigate to your vault
cd "/mnt/d/New folder/AI_Emplyee_Vault"

# 2. Check system status
ls -la AI_Employee_Vault/Needs_Action/
ls -la AI_Employee_Vault/Done/

# 3. Start the filesystem watcher (Terminal 1)
python filesystem_watcher.py AI_Employee_Vault
```

**Keep Terminal 1 running all day!**

---

## 🔄 PART 2: Processing Tasks

### Option A: Use Orchestrator (Recommended)

```bash
# Open NEW terminal (Terminal 2)
cd "/mnt/d/New folder/AI_Emplyee_Vault"

# Run orchestrator
python orchestrator.py AI_Employee_Vault

# Follow prompts:
# [d] - Mark task done
# [s] - Skip task
# [v] - View full content
# [q] - Quit
```

### Option B: Manual Processing with Claude Code

```bash
# Just ask Claude Code in this chat:
"Please check AI_Employee_Vault/Needs_Action/ and help me complete the tasks"

# Claude Code will:
# - Read the task files
# - Execute the tasks
# - Move completed files to Done/
```

---

## 📥 PART 3: Adding New Tasks

### Method 1: Drop Files into Inbox (Automated)

```bash
# Drop any file into Inbox
cp /path/to/your/file.txt AI_Employee_Vault/Inbox/

# Or create a text task
echo "Your task description here" > AI_Employee_Vault/Inbox/new_task.txt

# Watcher will automatically:
# - Detect the file (within 30 seconds)
# - Copy to Needs_Action/
# - Create action file with metadata
```

### Method 2: Create Task Directly in Needs_Action

```bash
# Create a properly formatted task
cat > AI_Employee_Vault/Needs_Action/my_task.md << 'EOF'
---
type: task
created: 2026-04-06
priority: high
status: pending
assigned_to: ai
---

# Task Title

## Description
What needs to be done

## Success Criteria
- Criterion 1
- Criterion 2

## Additional Context
Any relevant information
EOF
```

---

## 🧪 PART 4: Testing Commands

### Quick System Test

```bash
# 1. Create test file
echo "Test task for AI Employee" > AI_Employee_Vault/Inbox/test.txt

# 2. Wait 30 seconds, then check
ls -la AI_Employee_Vault/Needs_Action/

# 3. Run orchestrator
python orchestrator.py AI_Employee_Vault

# 4. Mark done with [d]

# 5. Verify in Done folder
ls -la AI_Employee_Vault/Done/
```

### Check Watcher Logs

```bash
# View today's watcher log
cat AI_Employee_Vault/Logs/watcher_2026-04-06.log

# View daily activity log
cat AI_Employee_Vault/Logs/2026-04-06_daily.md
```

---

## 📊 PART 5: Status & Monitoring Commands

### Check Current Status

```bash
# Quick overview
cd "/mnt/d/New folder/AI_Emplyee_Vault"

# Count pending tasks
ls AI_Employee_Vault/Needs_Action/*.md 2>/dev/null | wc -l

# Count completed tasks
ls AI_Employee_Vault/Done/*.md 2>/dev/null | wc -l

# View dashboard
cat AI_Employee_Vault/Dashboard.md
```

### Find Specific Files

```bash
# Find all tasks with "organize" in name
find AI_Employee_Vault -name "*organize*" -type f

# Find all high priority tasks
grep -r "priority: high" AI_Employee_Vault/Needs_Action/

# Find tasks created today
find AI_Employee_Vault/Needs_Action -name "2026-04-06*"
```

---

## 🛠️ PART 6: Maintenance Commands

### Clean Up Inbox

```bash
# After watcher processes files, clean up Inbox
rm AI_Employee_Vault/Inbox/*.txt

# Keep README files
# (Watcher ignores README.md automatically)
```

### Archive Old Completed Tasks

```bash
# Move old Done tasks to Approved
mkdir -p AI_Employee_Vault/Approved/2026-04/
mv AI_Employee_Vault/Done/2026-04-*.md AI_Employee_Vault/Approved/2026-04/
```

### View Logs

```bash
# Today's activity
cat AI_Employee_Vault/Logs/2026-04-06_daily.md

# Watcher activity
cat AI_Employee_Vault/Logs/watcher_2026-04-06.log

# All logs
ls -lh AI_Employee_Vault/Logs/
```

---

## 🚨 PART 7: Troubleshooting Commands

### Watcher Not Detecting Files

```bash
# 1. Check if watcher is running
ps aux | grep filesystem_watcher

# 2. Restart watcher
# Press Ctrl+C in Terminal 1, then:
python filesystem_watcher.py AI_Employee_Vault

# 3. Check file was created
ls -la AI_Employee_Vault/Inbox/

# 4. Wait full 30 seconds
# (Watcher checks every 30 seconds)
```

### Orchestrator Shows No Tasks

```bash
# Check if tasks exist
ls -la AI_Employee_Vault/Needs_Action/

# If empty, create a test task
cat > AI_Employee_Vault/Needs_Action/test.md << 'EOF'
---
type: task
created: 2026-04-06
priority: medium
status: pending
---

# Test Task
Test the orchestrator
EOF

# Run orchestrator again
python orchestrator.py AI_Employee_Vault
```

### Check System Health

```bash
# Verify all folders exist
ls -la AI_Employee_Vault/

# Check Python scripts
ls -la *.py

# Verify skills
ls -la AI_Employee_Vault/Skills/

# Check permissions
ls -la AI_Employee_Vault/Needs_Action/
ls -la AI_Employee_Vault/Done/
```

---

## 📋 PART 8: Quick Reference - Most Used Commands

### Daily Commands (Copy & Paste)

```bash
# Morning: Start watcher
cd "/mnt/d/New folder/AI_Emplyee_Vault"
python filesystem_watcher.py AI_Employee_Vault

# When ready to work: Run orchestrator (new terminal)
cd "/mnt/d/New folder/AI_Emplyee_Vault"
python orchestrator.py AI_Employee_Vault

# Add new task
echo "Task description" > AI_Employee_Vault/Inbox/task.txt

# Check status
ls AI_Employee_Vault/Needs_Action/
ls AI_Employee_Vault/Done/

# View dashboard
cat AI_Employee_Vault/Dashboard.md
```

---

## 🎯 PART 9: Current Task to Process

### You Have 1 Task Ready!

```bash
# File: AI_Employee_Vault/Needs_Action/test_task.txt
# Content: "Please create a summary of today's activities"

# To process it:
python orchestrator.py AI_Employee_Vault

# Or ask Claude Code:
"Please help me complete the task in Needs_Action/test_task.txt"
```

---

## 🔄 PART 10: Complete Workflow Example

### End-to-End Example

```bash
# === TERMINAL 1 ===
cd "/mnt/d/New folder/AI_Emplyee_Vault"
python filesystem_watcher.py AI_Employee_Vault
# Leave running...

# === TERMINAL 2 ===
cd "/mnt/d/New folder/AI_Emplyee_Vault"

# Drop a file
echo "Organize my downloads folder" > AI_Employee_Vault/Inbox/organize.txt

# Wait 30 seconds...

# Check it was processed
ls AI_Employee_Vault/Needs_Action/

# Run orchestrator
python orchestrator.py AI_Employee_Vault

# Read the task
# Press [d] to mark done
# Check Done folder
ls AI_Employee_Vault/Done/

# Success! ✅
```

---

## 📚 PART 11: Documentation Files

### Available Guides

```bash
# System overview
cat SYSTEM_SUMMARY.md

# Testing guide
cat TEST_GUIDE.md

# Orchestrator manual
cat ORCHESTRATOR_GUIDE.md

# Quick start
cat AI_Employee_Vault/QUICKSTART.md

# Company rules
cat AI_Employee_Vault/Company_Handbook.md

# Business goals
cat AI_Employee_Vault/Business_Goals.md
```

---

## 🎓 PART 12: Skills Reference

### Available Skills (in Skills/ folder)

1. **File_Organization.md** - Organize files by type and date
2. **Data_Extraction.md** - Extract structured data from documents
3. **Task_Routing.md** - Route tasks to correct folders
4. **Report_Generation.md** - Create formatted reports
5. **Process_Inbox_Task.md** - Automated inbox processing

```bash
# View a skill
cat AI_Employee_Vault/Skills/File_Organization.md

# List all skills
ls -la AI_Employee_Vault/Skills/
```

---

## ⚡ PART 13: Power User Commands

### Batch Operations

```bash
# Process multiple files at once
for file in /path/to/files/*.txt; do
    cp "$file" AI_Employee_Vault/Inbox/
done

# Count tasks by priority
grep -r "priority: high" AI_Employee_Vault/Needs_Action/ | wc -l
grep -r "priority: medium" AI_Employee_Vault/Needs_Action/ | wc -l
grep -r "priority: low" AI_Employee_Vault/Needs_Action/ | wc -l

# Generate quick report
echo "=== Status Report ==="
echo "Pending: $(ls AI_Employee_Vault/Needs_Action/*.md 2>/dev/null | wc -l)"
echo "Done: $(ls AI_Employee_Vault/Done/*.md 2>/dev/null | wc -l)"
echo "Approved: $(ls AI_Employee_Vault/Approved/*.md 2>/dev/null | wc -l)"
```

---

## 🚀 PART 14: Next Steps

### What to Do Now

1. **Process Current Task**
   ```bash
   python orchestrator.py AI_Employee_Vault
   ```

2. **Start Daily Operations**
   ```bash
   # Terminal 1: Start watcher
   python filesystem_watcher.py AI_Employee_Vault
   
   # Terminal 2: Work on tasks as they come
   python orchestrator.py AI_Employee_Vault
   ```

3. **Add Your Own Tasks**
   ```bash
   echo "Your task here" > AI_Employee_Vault/Inbox/mytask.txt
   ```

---

## 📞 Quick Help

### Common Questions

**Q: How do I stop the watcher?**
A: Press `Ctrl+C` in Terminal 1

**Q: How do I see what tasks are pending?**
A: `ls AI_Employee_Vault/Needs_Action/`

**Q: How do I manually execute a task?**
A: Ask Claude Code: "Help me complete tasks in Needs_Action/"

**Q: Where do completed tasks go?**
A: `AI_Employee_Vault/Done/`

**Q: How do I check logs?**
A: `cat AI_Employee_Vault/Logs/2026-04-06_daily.md`

---

## ✅ System Ready Checklist

- [x] All Python scripts created (3 files)
- [x] All folders created (10 folders)
- [x] All documentation created (48 files)
- [x] Skills library ready (5 skills)
- [x] Test task created and ready
- [x] Watcher tested and working
- [x] System fully operational

---

## 🎯 Your Next Command

**Right now, run this to process your test task:**

```bash
python orchestrator.py AI_Employee_Vault
```

**Or ask Claude Code:**
"Please help me complete the task in Needs_Action/test_task.txt - create a summary of today's activities"

---

**System Status**: 🟢 **READY FOR PRODUCTION**

**You're all set! Start using your Bronze-tier AI Employee now!** 🚀
