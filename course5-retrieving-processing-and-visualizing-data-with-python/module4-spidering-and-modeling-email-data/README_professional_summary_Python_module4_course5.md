Spidering and Modeling Email Data
Course 5 — Python for Everybody Specialization
Platform: Coursera – University of Michigan
Module 4 — Professional Summary

⸻

🎯 Module Objective

Module 4 introduced the second honors assignment: retrieving, cleaning, and modeling raw email data from the Sakai open-source project. This module extends the skills learned in Course 4 of the specialization and focuses on:

Spidering email archives

Parsing message metadata

Building relational models with SQLite

Cleaning inconsistent or malformed records

Generating histogram-style aggregates from the dataset

Understanding the structure of mailing list corpora

The goal was to walk through the full data-wrangling pipeline using the provided gmane tools:
retrieval → cleaning → modeling → basic analysis.

⸻

🛠️ Tools Used

Python 3

Provided spidering and modeling scripts:

gmane.py

gmodel.py

gbasic.py

SQLite + DB Browser for SQLite

content.sqlite and index.sqlite databases

Command Line Interface

⸻

📁 Directory Contents

This module folder contains:

content.sqlite — downloaded raw message data

index.sqlite — cleaned, modeled index built by gmodel.py

gmane.py — spidering script

gmodel.py — modeling script

gbasic.py — basic histogram/aggregation script

gmane.txt — spider output

gmodel.txt — modeling output

gbasic.txt — histogram output

Instructions_mailing_list_data_part1.txt

Instructor_note_mailing_list_data_part1.txt

PNG screenshots of each major step

⸻

📊 Summary of the Workflow
1. Spidering the Email Data

Using gmane.py, I downloaded email messages from:
http://mbox.dr-chuck.net/
into content.sqlite.

2. Inspecting the Raw Database

Using DB Browser, I confirmed:

The Messages table populated

Correct fields: id, email, sent_at, subject

Final count: 75 downloaded messages

3. Running gmodel.py to Build the Index

gmodel.py cleans and organizes data into:

index.sqlite

A normalized senders table

A cleaned messages table with sender IDs

4. Running gbasic.py to Create Summary Statistics

This script computes basic histogram data:

number of messages per sender

message distribution

top contributors

5. Validation

Using DB Browser and console output, I confirmed:

message counts

sender normalization

correct population of index tables

⸻

🧠 What I Learned

How raw mailing list archives are structured

How to normalize semi-structured timestamped data

How spidering and modeling scripts complement one another

Importance of checking intermediate databases (content.sqlite vs index.sqlite)

How histogram and frequency tables reveal sender patterns

⸻

🌟 Status

This module is marked complete in Coursera.
My first honors attempt did not pass (70%), and I am preparing a corrected second version.
This README reflects the official, polished summary for my GitHub portfolio.