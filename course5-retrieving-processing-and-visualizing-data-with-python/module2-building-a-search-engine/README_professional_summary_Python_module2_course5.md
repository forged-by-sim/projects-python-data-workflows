# 📘 Module 2 — Building a Search Engine  
**Course:** *Retrieving, Processing, and Visualizing Data with Python*  
**Specialization:** Python for Everybody  
**Platform:** University of Michigan — Coursera  
**Folder:** `module2-building-a-search-engine`

---

## 🎯 Module Objective

Module 2 introduces a simplified version of the **Google PageRank algorithm** and teaches how search engines model the structure of the web. The goal is to spider a website, record outbound links, build a link graph, calculate page rankings, and visualize the results.

This module is the **first Honors assignment** in the Capstone and extends concepts from Course 4 of the specialization.

---

## 🧩 What This Module Covers

- Basics of search engine crawling  
- Building a directed graph from webpages  
- Storing link relationships in SQLite  
- Running the PageRank algorithm  
- Visualizing the resulting graph structure  
- Understanding how ranking scores emerge over multiple iterations

---

## 🔄 PageRank Workflow

A complete workflow consists of:

1. **Spider webpages** using: spider.py

Creates/updates:
- `spider.sqlite`
- `Pages`, `Links`, and `Webs` tables

2. **Compute new rankings** using: sprank.py

- Iteratively updates the `Rank` column  
- Based on inbound/outbound link structure  

3. **Dump results** using: spdump.py

- Prints URLs, IDs, old rank, new rank  
- Used for screenshots & peer-grade evidence  

4. **Visualize** using: force_html.html

with:
- `force.js`
- `d3.v2.js`
- `force.css`

This produces an interactive force-directed graph showing nodes (pages) and edges (links).

---

## 🛠️ Tools and Files Used

### Python Scripts  
- `spider.py` — crawl & store link data  
- `sprank.py` — compute new PageRank values  
- `spdump.py` — print out rankings  
- `spreset.py` — reset database for second attempt  

### JavaScript / Visualization  
- `force_html.html`  
- `d3.v2.js`  
- `force.js`  
- `force.css`  

### Database  
- `spider.sqlite`  
- Stores pages, links, old rank, new rank, and web list

---

## 📁 Directory References

This module may include:

- `Instructions_page_rank.txt` (assignment instructions)  
- `Instructor_note_page_rank.txt` (feedback text)  
- `spider.sqlite`  
- Visualization files (HTML/JS/CSS)  
- Python scripts (spider/sprank/spdump/reset)

---

## 📸 Expected Outputs

- Command line output of `spdump.py` (100 rows minimum)  
- Force-directed graph showing connected nodes  
- A second graph using a different starting URL  
- Peer-grade submission screenshots  

---

## 💡 Summary

Module 2 teaches the foundations of how search engines gather information and determine importance through link analysis. By completing the spider–rank–visualize pipeline, learners gain hands-on exposure to algorithms behind real search engine systems.

---





