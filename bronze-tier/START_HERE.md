# 🎯 QUICK START - 3 Simple Steps

**Created**: 2026-04-06
**For**: Bronze-Tier AI Employee System

---

## ⚡ RIGHT NOW - Do These 3 Things

### Step 1: Run the Orchestrator (2 minutes)

```bash
cd "/mnt/d/HACKATHON_0_AI_EMPLYEE/AI_Emplyee_Vault/bronze-tier"
python orchestrator.py AI_Employee_Vault
```

**What happens:**
- Shows you the test task
- You press `[d]` to mark it done
- Task moves to Done/ folder

---

### Step 2: Start the Watcher (1 minute)

```bash
cd "/mnt/d/HACKATHON_0_AI_EMPLYEE/AI_Emplyee_Vault/bronze-tier"
python filesystem_watcher.py AI_Employee_Vault
```

**What happens:**
- Monitors Inbox/ folder
- Detects new files automatically
- Creates tasks in Needs_Action/
- **Leave this running!**

---

### Step 3: Test It (2 minutes)

Open a **NEW terminal** and run:

```bash
cd "/mnt/d/HACKATHON_0_AI_EMPLYEE/AI_Emplyee_Vault/bronze-tier"
echo "Organize my files" > AI_Employee_Vault/Inbox/organize_task.txt
```

**Wait 30 seconds**, then check:

```bash
ls AI_Employee_Vault/Needs_Action/
```

You should see new files created!

---

## ✅ That's It!

Your Bronze-tier AI Employee is now running.

### Daily Use:

**Morning:**
```bash
python filesystem_watcher.py AI_Employee_Vault
```
(Leave running all day)

**When you want to work:**
```bash
python orchestrator.py AI_Employee_Vault
```
(Process tasks one by one)

**Add new tasks:**
```bash
echo "Your task" > AI_Employee_Vault/Inbox/task.txt
```
(Watcher detects automatically)

---

## 📚 Full Documentation

For complete commands and details, see:
- **COMPLETE_COMMAND_REFERENCE.md** - All commands
- **ORCHESTRATOR_GUIDE.md** - How to use orchestrator
- **TEST_GUIDE.md** - Testing instructions
- **SYSTEM_SUMMARY.md** - System overview

---

## 🆘 Quick Help

**Watcher not detecting files?**
- Wait full 30 seconds
- Check: `ls AI_Employee_Vault/Inbox/`

**No tasks showing?**
- Check: `ls AI_Employee_Vault/Needs_Action/`
- Create test task (see Step 3 above)

**Need to stop watcher?**
- Press `Ctrl+C` in watcher terminal

---

**Status**: 🟢 System Ready
**Next**: Run Step 1 above!
