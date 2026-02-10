# 📨 Project – Email Spidering & Relational Modeling (Attempt 1)  
**Folder**: `gmane-project-attempt1`  
**Project Type**: Email Data Wrangling · SQLite Modeling · Frequency Analysis  
**Tools Used**: Python, SQLite, DB Browser, `gmane.py`, `gmodel.py`, `gbasic.py`  

⸻

## 🎯 Project Overview  
This project focused on **retrieving, cleaning, and modeling email data** from a mailing list archive. Using a pipeline of Python scripts and SQLite databases, I downloaded raw messages, structured them into normalized tables, and performed basic frequency analysis (e.g., messages per sender

⸻

## 🧪 Pipeline Summary

1. **Download Email Messages** (`gmane.py`)  
   - Pulled 75 messages from a test archive  
   - Stored results in `content.sqlite`

2. **Model the Database** (`gmodel.py`)  
   - Created normalized tables: `Senders`, `Messages`  
   - Cleaned malformed records and extracted sender IDs  
   - Output stored in `index.sqlite`

3. **Analyze Sender Frequency** (`gbasic.py`)  
   - Aggregated number of messages per sender  
   - Generated histograms and top-contributor stats

⸻

## 📂 Files Included

| File | Description |
|------|-------------|
| `gmane.py` | Script to spider and download raw messages |
| `gmodel.py` | Script to clean and model sender/message structure |
| `gbasic.py` | Script to compute histogram of sender message counts |
| `content.sqlite` | Raw email archive database |
| `index.sqlite` | Modeled database with cleaned sender/message tables |
| `gmane.txt`, `gmodel.txt`, `gbasic.txt` | Console outputs and debug logs |
| `README_gmane_project.txt` | Full attempt log with instructor feedback and correction plan |
| `*.png` | Screenshots of database tables and script output |

⸻

## 🧠 Key Learnings  
This attempt helped me:

- Understand the structure of raw mailing list archives  
- Normalize semi-structured timestamped data  
- Track how multiple scripts chain together for ETL-style workflows  
- Confirm output via both terminal and database browser inspection  
- Recognize the importance of complete, uncropped evidence in technical submissions  

⸻

## ⚠️ Issues Identified (Attempt 1)

| Area | Problem |
|------|---------|
| Screenshots | Some missing or cropped; essential fields not shown |
| Output | `index.sqlite` relationships not clearly captured |
| Validation | Histogram printout from `gbasic.py` lacked detail |
| Visual Evidence | Feedback noted key UI elements not visible due to window sizing |

⸻

## 🛠️ Plan for Attempt 2

- Full uncropped screenshots of `content.sqlite` (Messages table)  
- Screenshots of `index.sqlite` showing full sender/message normalization  
- Confirmed histogram printout from `gbasic.py`  
- Cross-check against rubric examples  
- Submit clean output logs and confirm outputs via both DB Browser and terminal  

⸻

## 💬 Reflection  
This project taught me how to **debug multi-step ETL pipelines**, improve submission quality, and produce portfolio-worthy documentation. The structure of `content.sqlite` vs `index.sqlite` gave me a better understanding of how **relational modeling** supports cleaner data analysis downstream.

---
