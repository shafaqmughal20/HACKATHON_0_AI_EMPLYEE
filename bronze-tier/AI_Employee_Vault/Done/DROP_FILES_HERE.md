---
type: guide
folder: inbox
purpose: file_drop_zone

status: done
completed: 2026-04-06 01:15:40---

# Inbox - File Drop Zone

## 🎯 Purpose
Drop any file here and the FilesystemWatcher will automatically detect it and create a processing task for the AI Employee.

## 📥 How It Works

### 1. Drop a File
Simply copy or move any file into this folder:
- Documents (PDF, Word, etc.)
- Spreadsheets (Excel, CSV, etc.)
- Images (JPG, PNG, etc.)
- Code files
- Data files
- Archives (ZIP, etc.)
- Any other file type

### 2. Automatic Detection
The FilesystemWatcher checks this folder every 30 seconds and:
- Detects new files
- Calculates file hash (prevents duplicates)
- Copies file to `Needs_Action/`
- Creates rich metadata action file
- Logs the activity

### 3. AI Processing
The AI Employee will:
- Review the file and metadata
- Determine appropriate action
- Execute or create a plan
- Update status and logs

## 📋 What Gets Created

For each file you drop, the system creates an action file with:

```yaml
---
type: file_drop
created: YYYY-MM-DD
timestamp: YYYY-MM-DD HH:MM:SS
priority: medium
status: pending
assigned_to: ai
---
```

### Metadata Included
- Original filename
- File type and category
- File size (human-readable)
- SHA256 hash
- Timestamps
- Location paths
- Type-specific suggestions

## 🚫 Files That Are Ignored

The watcher automatically skips:
- Hidden files (starting with `.`)
- README.md files
- Temporary files (`.tmp`, `.temp`, `~`)
- Directories
- Already processed files (by hash)

## 📊 File Categories

Files are automatically categorized:
- **document**: PDF, Word, text files
- **spreadsheet**: Excel, CSV
- **presentation**: PowerPoint
- **image**: JPG, PNG, GIF, etc.
- **video**: MP4, AVI, MOV, etc.
- **audio**: MP3, WAV, etc.
- **archive**: ZIP, RAR, 7Z, etc.
- **code**: Python, JavaScript, etc.
- **data**: JSON, XML, YAML, etc.
- **other**: Everything else

## 🔄 Processing Flow

```
1. Drop file → Inbox/
2. Watcher detects → Creates action file
3. Copies to → Needs_Action/
4. AI processes → Executes task
5. Completes → Moves to Done/
6. Review → Approve/Reject
```

## 💡 Tips

### For Best Results
- Use descriptive filenames
- One file at a time for testing
- Check `Needs_Action/` to see created tasks
- Review `Logs/` to see watcher activity

### Batch Processing
- Drop multiple files at once
- Watcher processes all in one cycle
- Each gets its own action file

### After Processing
- Original file stays in Inbox
- Can be deleted manually after AI processes
- Or keep as backup

## 🧪 Testing

### Test the Watcher
1. Start the watcher:
   ```bash
   python filesystem_watcher.py AI_Employee_Vault
   ```

2. Drop a test file here

3. Wait up to 30 seconds

4. Check `Needs_Action/` for:
   - Your file (copied)
   - Action file with metadata

5. Check `Logs/` for activity log

## 📝 Example Files to Try

### Simple Test
Create `test.txt` with some content and drop it here.

### Document Test
Drop a PDF or Word document.

### Data Test
Drop a CSV or JSON file.

### Image Test
Drop a JPG or PNG image.

## 🔍 Monitoring

### Check Watcher Status
The watcher logs to:
- Console (real-time)
- `Logs/watcher_YYYY-MM-DD.log`

### Verify Processing
After dropping a file, check:
1. `Needs_Action/` - File copied?
2. `Needs_Action/` - Action file created?
3. `Logs/` - Activity logged?
4. `Dashboard.md` - Status updated?

## ⚙️ Configuration

### Change Check Interval
```bash
python filesystem_watcher.py AI_Employee_Vault --interval 10
```
(Checks every 10 seconds instead of 30)

### Increase Logging
```bash
python filesystem_watcher.py AI_Employee_Vault --log-level DEBUG
```

## 🚨 Troubleshooting

### File Not Detected
- Wait full check interval (30s default)
- Check if file is hidden or temporary
- Verify watcher is running
- Check logs for errors

### Duplicate Processing
- System uses file hash to prevent duplicates
- Same file won't be processed twice
- Modify file to reprocess

### Permission Errors
- Ensure watcher has read access to Inbox
- Ensure watcher has write access to Needs_Action
- Check file isn't locked by another program

---

**Status**: 🟢 Ready for file drops
**Monitored By**: FilesystemWatcher
**Check Interval**: 30 seconds (default)
**Auto-Processing**: Enabled

Drop files here and let the AI Employee handle them!
