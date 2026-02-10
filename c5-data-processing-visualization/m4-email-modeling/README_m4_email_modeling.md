# 📧 M4 – Email Modeling & Metadata Aggregation  
**Folder**: `m4-email-modeling`  
**Focus**: Spidering raw email archives, modeling sender relationships, and analyzing frequency patterns using SQLite  

⸻

## 🎯 Overview  
This project explored how to **extract, normalize, and analyze metadata** from open-source mailing list archives. It introduced a full data-wrangling pipeline—beginning with web scraping and ending with relational modeling and summary statistics. The work was conducted using pre-built Python scripts that simulate real-world tasks in email parsing and SQLite-backed analysis.

⸻

## 🛠️ Core Skills Practiced

- Spidering email archives using Python  
- Parsing raw metadata (e.g., sender, timestamp, subject)  
- Normalizing inconsistent or malformed records  
- Modeling structured data into SQLite  
- Aggregating and analyzing message frequencies  
- Debugging intermediate results using DB Browser  

⸻

## 📂 Folder Contents

| File/Folder | Description |
|-------------|-------------|
| `gmane-project-attempt1/` | Full project that includes all scripts, outputs, and screenshots |
| `README_m4_email_modeling.txt` | Technical summary of the module pipeline and objectives |
| `README_gmane_project.txt` | Attempt log documenting results, root cause analysis, and feedback |

⸻

## 🧪 Tools & Technologies

- Python 3  
- SQLite & DB Browser  
- Scripts used:
  - `gmane.py` – Spidering raw emails  
  - `gmodel.py` – Data modeling into structured index  
  - `gbasic.py` – Frequency aggregation and histograms  
- `.sqlite` files for storing raw and modeled data  
- Console + visual validation steps  

⸻

## 💬 Reflection  
This project deepened my understanding of how to **work with semi-structured data at scale**. I learned how to normalize email metadata, debug SQLite population, and apply data modeling to real-world communication logs. It also reinforced the value of **clean, well-documented pipelines**—especially when validating output across multiple tools (CLI and GUI). While my first attempt required revision, the experience sharpened both my technical accuracy and attention to detail.

---
