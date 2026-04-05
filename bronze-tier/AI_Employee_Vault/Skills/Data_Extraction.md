---
type: skill
name: Data Extraction
category: analysis
difficulty: intermediate
created: 2026-04-05
last_used: 2026-04-05
success_rate: 100%
---

# Skill: Data Extraction

## Purpose
Extract structured information from documents and files, converting unstructured or semi-structured data into usable formats.

## When to Use
- Processing documents for key information
- Creating summaries from reports
- Migrating data between formats
- Building databases from files
- Extracting metadata
- Creating structured datasets

## Prerequisites
- Read access to source files
- Understanding of target data structure
- Knowledge of file formats (PDF, TXT, CSV, JSON, etc.)
- Write access to save extracted data

## Procedure

### 1. Identify Source and Target
```
Source:
- File type: PDF, Word, TXT, CSV, etc.
- Location: Full path
- Size: File size
- Format: Structured, semi-structured, unstructured

Target:
- Format: JSON, CSV, Markdown, etc.
- Structure: Define schema
- Location: Where to save
```

### 2. Define Extraction Schema
```
What to extract:
- Field 1: Name, type, validation rules
- Field 2: Name, type, validation rules
- Field 3: Name, type, validation rules

Example:
{
  "name": "string, required",
  "date": "YYYY-MM-DD, required",
  "amount": "number, optional",
  "category": "string, from predefined list"
}
```

### 3. Read Source File
```
1. Open file safely
2. Read contents
3. Verify file integrity
4. Handle encoding issues
5. Log file access
```

### 4. Parse Content
```
Based on file type:

Text Files:
- Read line by line
- Identify patterns
- Extract using regex or string matching

CSV Files:
- Parse headers
- Read rows
- Map columns to schema

JSON Files:
- Parse JSON structure
- Navigate nested objects
- Extract relevant fields

Documents (PDF, Word):
- Extract text content
- Identify sections
- Parse structured elements
```

### 5. Extract Data
```
For each data point:
1. Locate in source
2. Extract value
3. Validate format
4. Clean/normalize
5. Map to schema field
6. Handle missing data
```

### 6. Validate Extracted Data
```
Checks:
- [ ] All required fields present
- [ ] Data types correct
- [ ] Values within valid ranges
- [ ] No corruption or errors
- [ ] Consistent formatting
- [ ] Relationships maintained
```

### 7. Transform and Clean
```
Common transformations:
- Trim whitespace
- Normalize dates (YYYY-MM-DD)
- Standardize names (Title Case)
- Convert units
- Remove duplicates
- Fill missing values
```

### 8. Structure Output
```
Format options:

JSON:
{
  "extracted_date": "2026-04-05",
  "source_file": "document.pdf",
  "data": [
    {"field1": "value1", "field2": "value2"},
    {"field1": "value3", "field2": "value4"}
  ]
}

CSV:
field1,field2,field3
value1,value2,value3
value4,value5,value6

Markdown:
# Extracted Data

## Summary
- Total records: X
- Source: filename

## Data
| Field1 | Field2 | Field3 |
|--------|--------|--------|
| value1 | value2 | value3 |
```

### 9. Save Output
```
1. Choose appropriate format
2. Create output file
3. Write extracted data
4. Verify write succeeded
5. Check file integrity
```

### 10. Create Extraction Report
```
Document:
- Source file details
- Extraction date/time
- Records extracted
- Fields extracted
- Validation results
- Any issues encountered
- Output file location
```

## Quality Checks
- [ ] All source files processed
- [ ] Data extracted completely
- [ ] Validation passed
- [ ] Output format correct
- [ ] No data loss
- [ ] Extraction logged
- [ ] Output file created
- [ ] Report generated

## Common Pitfalls

### Pitfall 1: Encoding Issues
**Problem**: Special characters corrupted
**Solution**: Detect and handle encoding (UTF-8, ASCII, etc.)

### Pitfall 2: Missing Data
**Problem**: Required fields not found
**Solution**: Define default values or flag for review

### Pitfall 3: Format Inconsistency
**Problem**: Data in multiple formats
**Solution**: Normalize all data to standard format

### Pitfall 4: Large Files
**Problem**: Memory issues with big files
**Solution**: Process in chunks, stream data

## Examples

### Example 1: Extract Contact Info from Text
```
Source (contacts.txt):
John Doe
Email: john@example.com
Phone: 555-1234

Jane Smith
Email: jane@example.com
Phone: 555-5678

Output (contacts.json):
{
  "contacts": [
    {
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "555-1234"
    },
    {
      "name": "Jane Smith",
      "email": "jane@example.com",
      "phone": "555-5678"
    }
  ]
}
```

### Example 2: Extract Dates and Amounts from Report
```
Source: "Invoice dated 2026-04-05 for $1,234.56"

Extracted:
{
  "date": "2026-04-05",
  "amount": 1234.56,
  "currency": "USD"
}
```

## Variations

### Quick Extraction
- Simple patterns only
- Minimal validation
- Basic output format

### Deep Extraction
- Complex parsing
- Full validation
- Rich output with metadata
- Error handling
- Quality scoring

### Batch Extraction
- Multiple files
- Parallel processing
- Aggregated output
- Summary statistics

## Related Skills
- [[File_Organization]] - Organize extracted data
- [[Report_Generation]] - Create reports from extracted data
- [[Data_Validation]] - Validate extracted data quality

## Success Metrics
- 100% of source files processed
- >95% data extraction accuracy
- All validations passed
- Complete documentation
- Output files created successfully

## Notes
- Always validate extracted data
- Handle edge cases gracefully
- Log extraction details
- Keep source files unchanged
- Create backups before processing

---
**Last Updated**: 2026-04-05
**Times Used**: 1
**Success Rate**: 100%
**Estimated Time**: 10-60 minutes depending on complexity
