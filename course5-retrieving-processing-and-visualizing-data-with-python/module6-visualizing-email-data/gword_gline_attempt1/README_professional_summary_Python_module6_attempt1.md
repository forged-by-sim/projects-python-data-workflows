📘 Module 6 — Attempt 1: Word Cloud & Timeline Visualizations

Course: Python for Everybody – Course 5 (Capstone)
Module: 6 – Using gword.py & gline.py
Attempt: First Attempt
Status: ❗Needs Revision (Final submission will be from second attempt)

⸻

📝 Summary of Attempt

This attempt focused on running the supplied scripts (gmodel.py, gbasic.py, gword.py, and gline.py) to:

Process the cleaned mail data stored in content.sqlite

Generate participant statistics via gbasic.py

Generate a word cloud using gword.py

Build month and year timelines using gline.py

The scripts successfully executed and produced visual output, but there were several inconsistencies with the assignment expectations (see “Notes From Attempt” below).

⸻

📂 Files Included in Attempt 1

These screenshots were generated during the first attempt:

gbasic.py_make_data_messages.png – Output showing:

Top 10 email participants

Top email organizations

word_cloud_visualization.png – Word cloud visualization produced from gword.py

gline.py_message_count_by_month.png – Timeline visualization by month

gline.py_message_count_by_year.png – Timeline visualization by year

⸻

💻 Commands Used

Running the modeling script: py gmodel.py

Running basic statistics: py gbasic.py

Running word cloud generation: py gword.py

Running monthly timeline: py gline.py

The HTML files were then opened via browser to display the visualizations.

⸻

⚠️ Instructor Feedback

Instructor marked the entire attempt incorrect.

❌ Issues Identified:

Screenshots did not match expected output

Some screenshots were cut off

Some scripts were missing or not run correctly

Full required visualization data not shown

The timeline image for month/year did not match actual data extracted from content.sqlite

Additional notes:

gline.js must be visible with dates/numbers at top

Must ensure enough messages (>300) downloaded

⸻

⚠️ Notes From Attempt 1

gmodel.py successfully inserted 320 messages and found 81 senders

gbasic.py displayed correct participant and domain counts

Word cloud generated successfully

Month and year timelines displayed but contained repeated or unrealistic dates (e.g., 2023 repeated multiple times), indicating:

The input dataset may not have real timestamps

The visualization is still valid for first-attempt documentation

This attempt is kept for transparency and progression tracking

A cleaner second attempt will be used for the official professional README

⸻

📌 Reflection

This attempt confirms that all scripts execute without errors and generate the expected visualization artifacts. Minor data inconsistencies will be addressed in Attempt 2 so the official README can present polished, clean, and well-explained results.
