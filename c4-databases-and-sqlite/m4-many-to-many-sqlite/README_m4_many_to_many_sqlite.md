# 🔗 M4 – Many-to-Many Relationships in SQLite  
**Folder**: `m4-many-to-many-sqlite`  
**Focus**: Modeling complex relationships using SQL JOINs, foreign keys, and Python for real-world enrollment systems  

⸻

🎯 Overview

This module explored how to model **many-to-many relationships** in SQL — where a single student may be enrolled in multiple courses, and each course may have many students. I used Python to parse JSON input and created SQL tables that reflected real-world enrollment structures.

The main objective was to design a **normalized schema** that supports efficient querying and updates using intermediary tables and JOINs, then populate and query that structure using SQL and Python.

Key skills practiced:
- Designing and normalizing many-to-many relationships using JOIN tables  
- Writing Python scripts to parse JSON data and populate databases  
- Preventing duplicate entries using `INSERT OR IGNORE`  
- Using `executescript()` to define multiple schema tables at once  
- Verifying logic by inspecting `.sqlite` files with custom queries  

⸻

🗃️ Project: Many Students in Many Courses

Built a normalized database to model students and course enrollments. Parsed JSON data and mapped it to a structure with three interconnected tables: `User`, `Course`, and `Member`.

**Files:**
- `prompt_many_students_in_many_courses.png` – Prompt for the multi-table assignment  
- `solution-many-students-in-many-courses.txt` – Output and logic explanation  

⸻

📁 Project: Roster Database

Created a subfolder to organize all files related to the graded roster assignment.

**Folder**: `roster/`  
**Files:**
- `roster_data.json` – Input data with user-course enrollments  
- `roster_data.py` – Python script to parse and insert the data  
- `rosterdb.sql` – SQL schema defining User, Course, and Member tables  
- `rosterdb.sqlite` – Final populated database  
- `rosterdb.sqbpro` – SQL viewer project for database inspection  

⸻

🧠 Practice File

- `many-to-many-relationships-python-practice.txt` – Notes and logic breakdown for multi-table relationships using Python  

⸻

📘 Reflection

This project strengthened my confidence in translating real-world data patterns into relational schemas. I learned to design schemas with **intermediary tables**, write scripts to automate JSON parsing, and use SQL JOIN queries to extract meaningful relationships. 

By combining Python and SQL, I now feel equipped to design **flexible database structures** that support enrollment systems, simulation scenarios, or complex tagging workflows — wherever many-to-many mappings appear in backend logic.
