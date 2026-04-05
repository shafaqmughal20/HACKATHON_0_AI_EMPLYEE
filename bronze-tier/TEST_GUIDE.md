# Bronze-tier AI Employee - Quick Test Guide

## 🧪 Test Your Filesystem Watcher

Follow these steps to verify everything works:

### Step 1: Start the Watcher

```bash
cd "/mnt/d/New folder/AI_Emplyee_Vault"
python filesystem_watcher.py AI_Employee_Vault
```

You should see:
```
============================================================
Bronze-tier AI Employee - Filesystem Watcher
============================================================
Vault Path: AI_Employee_Vault
Check Interval: 30 seconds
Log Level: INFO

Monitoring Inbox folder for new files...
Drop any file into Inbox/ to trigger processing

Press Ctrl+C to stop
============================================================
```

### Step 2: Create a Test File

Open a new terminal and create a test file:

```bash
cd "/mnt/d/New folder/AI_Emplyee_Vault/AI_Employee_Vault/Inbox"
echo "This is a test file for the AI Employee system" > test_document.txt
```

### Step 3: Watch the Magic

Within 30 seconds, the watcher should:
1. Detect the new file
2. Log: "Found 1 new file(s) in Inbox"
3. Copy it to `Needs_Action/`
4. Create an action file with rich metadata

### Step 4: Verify Results

Check `Needs_Action/` folder:
```bash
ls -la AI_Employee_Vault/Needs_Action/
```

You should see:
- `test_document.txt` (your file, copied)
- `2026-04-05_FileDropped_test_document.md` (action file)

### Step 5: Review the Action File

```bash
cat AI_Employee_Vault/Needs_Action/2026-04-05_FileDropped_test_document.md
```

Should contain:
- File metadata (name, size, type)
- SHA256 hash
- Timestamps
- Suggested actions
- Success criteria

### Step 6: Check Logs

```bash
cat AI_Employee_Vault/Logs/watcher_2026-04-05.log
```

Should show:
- File detection
- Processing steps
- Success confirmation

## 🎯 What to Test

### Test Different File Types

1. **Text Document**
   ```bash
   echo "Meeting notes" > AI_Employee_Vault/Inbox/notes.txt
   ```

2. **JSON Data**
   ```bash
   echo '{"name": "test", "value": 123}' > AI_Employee_Vault/Inbox/data.json
   ```

3. **CSV File**
   ```bash
   echo "name,age,city\nJohn,30,NYC" > AI_Employee_Vault/Inbox/data.csv
   ```

4. **Python Script**
   ```bash
   echo "print('Hello AI Employee')" > AI_Employee_Vault/Inbox/script.py
   ```

### Test Duplicate Prevention

Drop the same file twice:
```bash
cp AI_Employee_Vault/Inbox/test_document.txt AI_Employee_Vault/Inbox/test_document_copy.txt
```

The watcher should:
- Detect it's the same content (by hash)
- Skip processing the duplicate
- Log: "File already processed"

### Test Batch Processing

Drop multiple files at once:
```bash
cd AI_Employee_Vault/Inbox
echo "File 1" > file1.txt
echo "File 2" > file2.txt
echo "File 3" > file3.txt
```

Watcher should process all three in one cycle.

## ✅ Success Criteria

Your system is working if:
- [x] Watcher starts without errors
- [x] New files are detected within 30 seconds
- [x] Files are copied to Needs_Action/
- [x] Action files are created with metadata
- [x] Activity is logged
- [x] Duplicates are prevented
- [x] Multiple files are handled

## 🐛 Troubleshooting

### Watcher Won't Start

**Error**: `FileNotFoundError: Vault path does not exist`
**Fix**: Check the vault path is correct
```bash
ls -la AI_Employee_Vault/
```

### Files Not Detected

**Issue**: Dropped file but nothing happens
**Checks**:
1. Wait full 30 seconds
2. Check file isn't hidden (`.filename`)
3. Check file isn't README.md
4. Verify watcher is running (check terminal)

### Import Error

**Error**: `ModuleNotFoundError: No module named 'base_watcher'`
**Fix**: Run from the correct directory
```bash
cd "/mnt/d/New folder/AI_Emplyee_Vault"
python filesystem_watcher.py AI_Employee_Vault
```

### Permission Errors

**Error**: `PermissionError: [Errno 13]`
**Fix**: Check file permissions
```bash
chmod 755 AI_Employee_Vault/Inbox/
chmod 755 AI_Employee_Vault/Needs_Action/
```

## 🚀 Next Steps

Once testing is successful:

1. **Keep Watcher Running**
   ```bash
   # Run in background (Linux/Mac)
   nohup python filesystem_watcher.py AI_Employee_Vault > watcher.log 2>&1 &
   ```

2. **Start Using It**
   - Drop real files into Inbox/
   - Let AI process them
   - Review results in Done/

3. **Monitor Performance**
   - Check Dashboard.md daily
   - Review Logs/ for issues
   - Track metrics in Business_Goals.md

4. **Customize**
   - Adjust check interval if needed
   - Modify file type suggestions
   - Add custom processing rules

## 📊 Expected Output

### Console Output (Watcher)
```
2026-04-05 19:35:30 - FilesystemWatcher - INFO - Found 1 new file(s) in Inbox
2026-04-05 19:35:30 - FilesystemWatcher - INFO -   - test_document.txt
2026-04-05 19:35:30 - FilesystemWatcher - INFO - Updates detected - creating action file
2026-04-05 19:35:30 - FilesystemWatcher - INFO - Processing file: test_document.txt
2026-04-05 19:35:30 - FilesystemWatcher - INFO - Copied to: test_document.txt
2026-04-05 19:35:30 - FilesystemWatcher - INFO - Created action file: 2026-04-05_FileDropped_test_document.md
2026-04-05 19:35:30 - FilesystemWatcher - INFO - Successfully processed: test_document.txt
2026-04-05 19:35:30 - FilesystemWatcher - INFO - Action file created: ...
```

### File Structure After Test
```
AI_Employee_Vault/
├── Inbox/
│   ├── test_document.txt (original)
│   └── DROP_FILES_HERE.md
├── Needs_Action/
│   ├── test_document.txt (copy)
│   └── 2026-04-05_FileDropped_test_document.md (action)
└── Logs/
    └── watcher_2026-04-05.log (activity log)
```

---

**Ready to test?** Start the watcher and drop a file! 🚀
