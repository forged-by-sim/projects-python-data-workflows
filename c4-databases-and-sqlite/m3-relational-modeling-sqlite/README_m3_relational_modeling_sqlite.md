# 🎼 M3 – Relational Modeling with SQLite  
**Folder**: `m3-relational-modeling-sqlite`  
**Focus**: Designing normalized schemas and querying across multiple related tables using SQL and Python  

⸻

🎯 Overview

This module focused on **relational data modeling** and how to structure information across multiple tables using foreign keys. I practiced building normalized schemas from real-world datasets, writing SQL JOIN queries, and scripting the full workflow with Python and SQLite.

Key skills practiced:
- Representing data using related tables (e.g., tracks, albums, genres, artists)  
- Designing schemas with foreign keys and primary keys  
- Writing multi-table JOIN queries to extract linked records  
- Importing `.csv` and `.xml` data into structured formats  
- Debugging and evolving query logic over multiple script iterations  

⸻

🗃️ Project: Multi-Table Database – Tracks & Artists

Designed a relational schema representing musical tracks and loaded the `tracks.csv` file into `trackdb.sqlite` using Python. Performed multi-table JOINs to list tracks by genre, artist, and album.

**Files:**
- `trackdb.sqlite` – Final SQLite database  
- `tracks.csv` – Raw input data used to populate the database  
- `tracks.py` – Script that processes and inserts CSV data  
- `results_tracks.png` – Screenshot showing query results  
- `prompt_musical_track_database1.png`, `prompt_musical_track_database2.png` – Task instructions  

⸻

📁 Bonus: Script Evolution Archive

Included an `old tracks files` folder to document earlier iterations of the `tracks.py` script and compare logic improvements over time.

**Files:**
- `old tracks files/Library.xml` – Initial XML version of input data  
- `old tracks files/tracks.py` – Previous version of track processing script  

⸻

🧠 Practice File

- `multi-table-relational-sql-practice.txt` – SQL JOIN and foreign key chaining exercises  

⸻

📘 Reflection

This project helped bridge theory and practice. By creating real JOIN queries and seeing them work inside a structured database, abstract relationships became tangible. The musical track database made it easy to simulate linking tables together through key relationships. Working with `.csv`, `.sqlite`, and `.py` in unison gave me confidence in **ETL-style workflows** — a foundational skill for simulation logging, analytics, and backend reporting pipelines.

