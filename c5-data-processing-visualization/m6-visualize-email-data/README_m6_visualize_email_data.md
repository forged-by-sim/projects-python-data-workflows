# 🌐 M6 – Visualizing Word Frequencies & Message Timelines  
**Folder**: `m6-visualize-email-data`  
**Focus**: Creating visual insights from email datasets using word clouds and time-series charts  

⸻

## 🎯 Overview  
This project introduced techniques for **visualizing trends in large text datasets** using HTML and JavaScript. Building on cleaned SQLite email archives from earlier modules, I practiced generating:

- Word frequency visualizations using `gword.py`  
- Timeline charts using `gline.py`  

The result was a lightweight **mini analytics dashboard** created entirely with Python and browser-based tools—mirroring real-world patterns in newsrooms, simulation logs, or discussion forums.

⸻

## 🛠️ Core Skills Practiced

- Extracting structured insights from SQLite databases  
- Transforming raw subject lines into frequency dictionaries  
- Aggregating message volume by timestamp (month, year)  
- Exporting data from Python → JSON → browser-based D3 visualizations  
- Troubleshooting visualization issues (e.g., missing data, cropping, formatting)

⸻

## 📂 Folder Contents

| File/Folder | Description |
|-------------|-------------|
| `gword-gline-project-attempt1/` | Full first-attempt project output including visualizations, screenshots, and scripts |
| `README_m6_visualize_email_data.txt` | Module-level overview of visualization objectives and tools used |
| `README_gword_gline_project.txt` | Project log and reflection for Attempt 1 |

⸻

## 📊 Visual Outputs

### 1. 📈 Participant & Organization Statistics (`gbasic.py`)
- Validated email modeling  
- Displayed top individual contributors and domain breakdowns

### 2. ☁️ Word Cloud (`gword.py → gword.htm`)
- Highlighted most frequent subject line terms  
- Larger words = higher frequency  
- Offers qualitative insight into discussion themes

### 3. 📅 Timeline of Messages (`gline.py → gline.htm`)
- Messages visualized by **month** and **year**  
- Revealed seasonal trends, burst activity, and participation dips  
- Useful for evaluating historical communication volume

⸻

## 🧠 Key Takeaways

- Translated text metadata into **visual stories**  
- Practiced a full ETL + Visualization workflow:  
  `SQLite → Python → JavaScript → Browser`  
- Gained confidence in diagnosing pipeline issues and refining evidence for technical submissions  
- Learned how front-end tools (e.g., D3) integrate with Python-generated output

⸻

## 💬 Reflection  
This project tied together the entire specialization by shifting from data collection and cleaning to **interpretable, shareable insights**. The experience reflects real-world ETL + analytics workflows and bridges coding with communication. While my first attempt required revisions, it gave me the blueprint for producing polished, impactful visualizations in the second.

---
