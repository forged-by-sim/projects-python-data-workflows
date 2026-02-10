# 📊 Project – Email Visualization (Word Clouds & Time-Series Graphs)  
**Folder**: `gword-gline-project-attempt1`  
**Type**: Exploratory Visualization · Data Parsing · Pipeline Debugging  
**Tools Used**: Python, SQLite, HTML, JavaScript, D3.js  

⸻

## 🎯 Project Goal  
This project aimed to **visualize patterns within an email archive** by:

- Generating a **word cloud** to show frequently used terms across messages  
- Creating a **line chart** to display message volume over time (monthly & yearly)  

I attempted to combine Python data processing with browser-based charting. Although the pipeline ran from database to HTML output, the final results had several issues in formatting, logic, and script ordering.

⸻

## 🧪 Outputs Attempted

1. **Word Cloud** (`gword.py`)  
   - Extracted word frequencies from `content.sqlite`  
   - Output files: `gword.htm`, `gword.js`, `d3.layout.cloud.js`  
   - Screenshot: `word_cloud_visualization.png`  
   - ⚠️ Output showed some words but likely included improperly parsed tokens or inconsistent formatting  

2. **Time-Series Graphs** (`gline.py`)  
   - Aggregated email counts by month and by year  
   - Files: `gline.htm`, `year/gline.htm`, and their corresponding `.js` files  
   - Screenshots:  
     - `gline.py_message_count_by_month.png`  
     - `gline.py_message_count_by_year.png`  
   - ⚠️ Timeline was incomplete or failed to show accurate counts  

⸻

## 📂 Folder Contents

| File | Description |
|------|-------------|
| `gword.py`, `gline.py` | Python scripts to extract and format data |
| `gword.htm`, `gword.js` | Files used to render word cloud in browser |
| `gline.htm`, `gline.js` | Monthly message count visual |
| `year/gline.htm`, `year/gline.js` | Annual message count visual |
| `d3.v2.js`, `d3.layout.cloud.js` | Required libraries for rendering output |
| `content.sqlite`, `index.sqlite` | Source email databases |
| `README_gword_gline_project.txt` | Notes on attempt, breakdown of issues |
| `*.png` | Screenshots for documentation and debugging |

⸻

## 🧠 Lessons Learned  

- D3-based visualizations **require clean data structures** and script linking  
- Python scripts must be **run in the correct order** and validated with sample outputs  
- Browser outputs often fail silently if data is malformed or libraries are mislinked  
- Intermediate files like `.js` and `.json` must be **checked for valid syntax**  
- A successful pipeline requires **modular testing**, not just end-to-end execution  

⸻

## 💬 Reflection  

This was a valuable **first pass** at a complex multi-tool pipeline. While the visualizations did not fully function as intended, I gained critical insights into where breakdowns can occur—from raw SQL extraction to browser rendering. Debugging these layers will directly support future simulations where real-time visual outputs are essential.

This attempt marks a foundational learning checkpoint—and I’m ready to rebuild it stronger in version 2.

---
