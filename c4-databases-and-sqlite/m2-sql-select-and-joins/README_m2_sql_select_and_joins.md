# 🗃️ M2 – SQL Queries & Single-Table Operations  

**Folder**: `m2-sql-select-and-joins`  
**Focus**: Querying SQLite databases using Python scripts and SQL for single-table data manipulation and aggregation  

⸻

🎯 Overview

This module introduced the core CRUD operations—**Create, Read, Update, Delete**—within the context of SQLite and Python. I learned how to build, query, and update local databases through real-world examples, focusing on **single-table schemas** and SQL statements executed from Python scripts.

Key skills practiced:
- Connecting Python to a SQLite database
- Writing SQL queries in `.py` scripts
- Using `cursor.execute()` and `commit()` for transactions
- Filtering and sorting with `SELECT`, `WHERE`, and `ORDER BY`
- Parsing email domains and counting frequency from structured data

⸻

🧪 Project: Our First Database

Built a script that parses email addresses from a text file, extracts the domain names, and stores frequency counts in a local SQLite database. Final results were printed and validated through SQL queries inside Python.

**Files:**
- `prompt_first_database.png` – Assignment prompt screenshot  
- `results_first_database.png` – Output screenshot showing final results  
- `solution_first-database.txt` – Alternate database creation logic  

⸻

🧮 Project: Counting Email in a Database

Extended the original project to include aggregation and sorting of domains by frequency using SQL's `ORDER BY`. Demonstrated how relational databases help structure and analyze large text data at scale.

**Files:**
- `prompt_counting_email_in_database.png` – Screenshot prompt for the advanced query extension 
- `emaildb.py` – Python script to parse and populate database  
- `emaildb.sqlite` – Final SQLite database with domain frequency counts  

⸻

🧠 Practice File

- `single-table-sql-practice.txt` – SQL statements for CRUD operations inside a single table  

⸻

📘 Reflection

This module solidified my confidence with databases and scripting. Writing dynamic Python scripts to build and query local databases was both intuitive and empowering. It deepened my understanding of how backend systems store and process structured data, laying the foundation for real-world ETL (Extract, Transform, Load) tasks. These skills are now part of my toolkit for logging simulation data, tracking user interactions, and structuring backend pipelines.

