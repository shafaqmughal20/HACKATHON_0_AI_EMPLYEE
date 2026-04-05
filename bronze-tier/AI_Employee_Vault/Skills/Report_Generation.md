---
type: skill
name: Report Generation
category: communication
difficulty: intermediate
created: 2026-04-05
last_used: 2026-04-05
success_rate: 100%
---

# Skill: Report Generation

## Purpose
Create formatted, informative reports from data, logs, and activities to communicate status, progress, and insights.

## When to Use
- Daily activity summaries
- Weekly status reports
- Monthly performance reviews
- Project completion reports
- Error/incident reports
- Data analysis summaries
- Dashboard updates

## Prerequisites
- Access to source data (logs, files, metrics)
- Understanding of report audience
- Knowledge of what metrics matter
- Write access to save reports

## Procedure

### 1. Define Report Scope
```
Questions to answer:
- What is the report about?
- Who is the audience?
- What time period does it cover?
- What decisions will it inform?
- What format is needed?
```

### 2. Gather Data
```
Sources to check:
- Logs/ folder for activity data
- Done/ folder for completed tasks
- Approved/ folder for success patterns
- Rejected/ folder for failure analysis
- Dashboard.md for current status
- Business_Goals.md for metrics

Data to collect:
- Quantitative: counts, times, percentages
- Qualitative: observations, insights, issues
- Temporal: trends over time
- Comparative: vs. goals, vs. previous period
```

### 3. Calculate Metrics
```
Common metrics:
- Task completion rate: (completed / total) * 100
- Average response time: sum(times) / count
- Error rate: (errors / total actions) * 100
- Approval rate: (approved / submitted) * 100
- Productivity: tasks per day/week
- Quality score: based on approval/rejection ratio
```

### 4. Analyze Data
```
Look for:
- Trends: improving, declining, stable
- Patterns: recurring issues, success factors
- Anomalies: unusual events, outliers
- Insights: what the data reveals
- Opportunities: areas for improvement
```

### 5. Structure Report
```
Standard report structure:

# Report Title
Date range and report type

## Executive Summary
- Key highlights (3-5 bullets)
- Most important findings
- Critical actions needed

## Metrics Overview
- Key performance indicators
- Comparison to goals
- Trend indicators

## Detailed Analysis
- Breakdown by category
- Supporting data
- Context and explanation

## Highlights
- Successes and wins
- Notable achievements
- Positive trends

## Challenges
- Issues encountered
- Blockers or obstacles
- Areas needing attention

## Insights & Learnings
- What worked well
- What didn't work
- Lessons learned

## Recommendations
- Suggested actions
- Process improvements
- Next steps

## Appendix (if needed)
- Detailed data tables
- Supporting documentation
- References
```

### 6. Format Report
```
Markdown formatting:

Headers:
# Main Title
## Section
### Subsection

Lists:
- Bullet point
1. Numbered item

Tables:
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Tasks  | 25    | 20     | ✅     |

Emphasis:
**Bold** for important
*Italic* for emphasis

Status indicators:
✅ Success/On track
⚠️ Warning/At risk
❌ Issue/Behind
🔄 In progress
```

### 7. Add Visualizations
```
Text-based charts:

Progress bar:
[████████░░] 80% complete

Trend indicator:
↗️ Increasing
↘️ Decreasing
→ Stable

Simple bar chart:
Task Completion:
Mon: ████████ 8
Tue: ██████ 6
Wed: ██████████ 10
Thu: ████████ 8
Fri: ████████████ 12
```

### 8. Review and Refine
```
Checklist:
- [ ] All data accurate
- [ ] Calculations correct
- [ ] Formatting consistent
- [ ] Clear and concise
- [ ] Actionable insights
- [ ] No sensitive data exposed
- [ ] Grammar and spelling checked
- [ ] Audience-appropriate language
```

### 9. Save and Distribute
```
1. Save to appropriate location
2. Use standard naming: YYYY-MM-DD_ReportType.md
3. Update Dashboard with link
4. Log report creation
5. Move to Done/ for review if needed
```

## Quality Checks
- [ ] Data sources verified
- [ ] Metrics calculated correctly
- [ ] Trends identified accurately
- [ ] Insights are meaningful
- [ ] Recommendations are actionable
- [ ] Format is clean and readable
- [ ] No errors or typos
- [ ] Report saved correctly

## Common Pitfalls

### Pitfall 1: Data Overload
**Problem**: Too much data, hard to read
**Solution**: Focus on key metrics, move details to appendix

### Pitfall 2: No Insights
**Problem**: Just numbers, no analysis
**Solution**: Always explain what the data means

### Pitfall 3: Missing Context
**Problem**: Numbers without comparison
**Solution**: Compare to goals, previous periods, benchmarks

### Pitfall 4: Unclear Recommendations
**Problem**: Vague suggestions
**Solution**: Specific, actionable next steps

## Examples

### Example 1: Daily Activity Report
```markdown
---
type: report
date: 2026-04-05
report_type: daily_activity
---

# Daily Activity Report - April 5, 2026

## Summary
- ✅ 12 tasks completed
- ⚠️ 2 tasks pending approval
- 🔄 3 tasks in progress
- ❌ 0 errors

## Metrics
- **Completion Rate**: 92% (target: 90%)
- **Average Response Time**: 15 minutes (target: 30 min)
- **Quality Score**: 100% (all approved)

## Highlights
- Processed 8 files from Inbox
- Created 2 new skills
- Organized Documents folder (150 files)

## Challenges
- None today

## Tomorrow's Focus
- Complete pending approval items
- Process new inbox items
- Update weekly report

---
**Status**: ✅ On Track
```

### Example 2: Weekly Summary Report
```markdown
# Weekly Summary - Week 14, 2026

## Executive Summary
- 58 tasks completed (target: 50) ✅
- 95% approval rate (target: 90%) ✅
- 3 new skills created
- 1 process improvement implemented

## Metrics Overview
| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| Tasks | 58 | 52 | ↗️ +12% |
| Approval Rate | 95% | 88% | ↗️ +7% |
| Avg Response | 18 min | 25 min | ↗️ -28% |
| Errors | 2 | 5 | ↗️ -60% |

## Task Breakdown
- File Organization: 25 tasks
- Data Extraction: 15 tasks
- Report Generation: 10 tasks
- Other: 8 tasks

## Insights
- Response time improved significantly
- File organization is most common task type
- Quality improving (fewer rejections)

## Recommendations
1. Create automation for file organization
2. Build template library for reports
3. Document data extraction patterns

---
**Overall Status**: ✅ Exceeding Expectations
```

## Variations

### Quick Report (5 minutes)
- Key metrics only
- Bullet points
- Minimal analysis

### Standard Report (15-30 minutes)
- Full structure
- Analysis and insights
- Recommendations

### Comprehensive Report (1+ hours)
- Deep analysis
- Multiple data sources
- Detailed visualizations
- Executive summary + appendix

## Related Skills
- [[Data_Extraction]] - Extract data for reports
- [[File_Organization]] - Organize report files
- [[Task_Routing]] - Route reports for approval

## Success Metrics
- Report completed on time
- All data accurate
- Clear insights provided
- Actionable recommendations
- Positive feedback from human

## Notes
- Keep reports concise and focused
- Use visuals to enhance understanding
- Always provide context for numbers
- Make recommendations specific and actionable
- Update report templates based on feedback

---
**Last Updated**: 2026-04-05
**Times Used**: 1
**Success Rate**: 100%
**Estimated Time**: 15-60 minutes depending on scope
