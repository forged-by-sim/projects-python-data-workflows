Attempt 1 — Spidering and Modeling Email Data
Module 4 — Honors Assignment Attempt Log

⸻

📂 Attempt Overview

This README documents my first attempt at the Module 4 Honors assignment for:

Capstone: Retrieving, Processing, and Visualizing Data with Python – Module 4
University of Michigan — Python for Everybody

This attempt received a 70%, with a note for revision.
The following sections outline what I did, what worked, what didn’t, and what must be corrected on Attempt 2.

⸻

🛠️ Files Referenced in This Attempt
Python Scripts Used

gmane.py

gmodel.py

gbasic.py

SQLite Databases

content.sqlite

index.sqlite

Text Documents

Instructions_mailing_list_data_part1.txt

Instructor_note_mailing_list_data_part1.txt

Screenshots (from Attempt 1)

Message_count_SQLiteBrowser.png

Messages_shown_after_gmodel.py_execution.png

SQLiteBrowser_messages_downloaded_to_content.sqlite.png

gbasic.py_computes_basic_histogram_data.png

gmodel.py_makes_index.sqlite.png

These filenames match your folder exactly.

⸻

📘 Step-by-Step Attempt Record
1. Downloading the Email Messages (gmane.py)

Successfully executed gmane.py

A total of 75 messages were downloaded into content.sqlite

Verified in DB Browser
→ Screenshot: SQLiteBrowser_messages_downloaded_to_content.sqlite.png

2. Inspecting the Content Database

Viewed the raw Messages table

Verified email, subject, and timestamp fields
→ Screenshot: Message_count_SQLiteBrowser.png

3. Running the Modeling Script (gmodel.py)

Executed gmodel.py

Output showed:

“Reading messages from content.sqlite”

“Senders found: 41”

index.sqlite was created
→ Screenshot: gmodel.py_makes_index.sqlite.png
→ Screenshot: Messages_shown_after_gmodel.py_execution.png

4. Histogram/Sender Aggregation (gbasic.py)

Executed gbasic.py

Able to print lists of senders with counts
→ Screenshot: gbasic.py_computes_basic_histogram_data.png

⸻

❗ Instructor Feedback (Attempt 1)

(Referenced via your TXT file — not pasted directly)

From Instructor_note_mailing_list_data_part1.txt, feedback included:

Screenshot 1 cut off the data fields

Screenshot 2 was missing the expected gmodel.py output

Screenshot 3 did not show the correct index.sqlite structure

gbasic.py output screenshot needed additional detail

No code edits should be made to gbasic.py

⸻

🔍 Root Cause Analysis

The deduction from the instructor note:

1. Screenshots did not match rubric expectations

Some screenshots did not show the essential fields or correct windows, causing rubric mismatch.

2. Missing demonstration of the correct modeled database

index.sqlite was not captured with all expected sender/message relationships visible.

3. gbasic.py output incomplete

The screenshot did not display the full histogram output that reviewers expected.

4. Minor display inconsistencies

Window sizes and cropping cut off essential evidence.

⸻

🧠 What I Learned From Attempt 1

The importance of capturing complete database tables without cut-off columns

That each screenshot must clearly prove:

downloaded messages

modeled database

correct sender histogram

That the grading for this module is strict but structured

How to compare expected output vs. actual output

⸻

🚀 Plan for Attempt 2

Based on the instructor note, Attempt 2 will include:

Full screenshots of content.sqlite (Messages table)

Full screenshots of index.sqlite (senders + messages tables)

Terminal output for:

gmane.py

gmodel.py

gbasic.py

Correctly framed and uncropped captures

Ensuring no columns are hidden

Using side-by-side verification with expected output examples

Attempt 2 will be submitted after all corrections.