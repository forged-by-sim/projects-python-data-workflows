# 🐛 Module 2 — Attempt #1 Log  
**Course:** *Retrieving, Processing, and Visualizing Data with Python*  
**Specialization:** Python for Everybody  
**Folder:** `module2-building-a-search-engine/spider_attempt1`  

---

## 🧭 Overview

This README documents my **first attempt** at completing the Module 2 Honors assignment.  
The goal was to:

- Spider 100+ pages  
- Run the PageRank algorithm  
- Dump ranking results  
- Visualize the link graph  
- Repeat the process with a second starting URL  
- Submit screenshots for peer review  

I received a **70%** score with instructor feedback. This document captures the full technical trail.

---

## 📁 Files Included in Attempt #1

### Python Scripts
- `spider.py`  
- `sprank.py`  
- `spdump.py`  
- `spreset.py`  
- `spiderdump.py`

### Visualization Files
- `force_html.html`  
- `force.js`  
- `d3.v2.js`  
- *Missing:* `force.css` (key issue)

### Database
- `spider.sqlite`

### Output Screenshots
- `spdump_100_pages.png`  
- `spdump_109_pages.png`  
- `html_quotestoscrape.png`  
- `html_sparsed_dots_bryony.png`

### Text Files
- `Instructions_page_rank.txt`  
- `Instructor_note_page_rank.txt`

---

## ✔️ What Worked

### **1. Successful Crawling**
- Spidered **100 pages** from `quotes.toscrape.com`
- Spidered **109 pages** starting from `known_by_Bryony.html`
- `spider.sqlite` updated with `Pages` and `Links` records

### **2. Successful Dumps**
`spdump.py` printed rows from the SQLite database correctly for both runs.

### **3. Successful Visualizations**
- Two force graphs generated with multi-colored nodes  
- Both HTML files opened in the browser without crashing  

---

## ⚠️ What Went Wrong (Root Causes)

### **1. PageRank was NOT recalculated**
Instructor note:
> “sprank.py was not run before spdump.py in order to update the page rankings.”

Meaning:
- Your rankings stayed at the *initial* values  
- Node sizes & final ordering were incorrect  

### **2. force.css WAS missing**
Instructor note:
> “force.css was not stored in the same folder… judging from the missing lines connecting the nodes.”

Effect:
- The force-directed graph displayed **floating dots**  
- No connecting lines  
- No link relationships drawn  

### **3. Folder structure fragmentation**
Some visualization assets were in the root, others in `ot/`.

Effect:
- Browser could not load all dependencies  
- CSS styling and link lines never activated  

---

## 🔍 Technical Breakdown of Mistakes

### **A. Correct workflow should be:**

spider.py → sprank.py → spdump.py → force_html.html

I ran:

spider.py → spdump.py → force_html.html


### **B. CSS dependency issue**
`force.css` is required to render edges properly.

The browser silently loads the HTML but produces incomplete visuals.

### **C. Database ranking never updated**
Because `sprank.py` was skipped, PageRank iteration never happened.

`spdump.py` therefore printed default values.

---

## 📸 Attempt 1 Results

### 1. Quotes.toscrape.com — Force Graph  
*(screenshot included in repo)*

### 2. Known_by_Bryony — Force Graph  
*(screenshot included in repo)*

### 3. spdump (100 rows)  
*(screenshot included)*

### 4. spdump (109 rows)  
*(screenshot included)*

---

## 💬 Instructor Feedback (Referenced, Not Embedded)

Files:
- `Instructor_note_page_rank.txt`

Summary:
- Must run `sprank.py` before dumping  
- Need `force.css` in same folder  
- Mention feedback when requesting reset  

---

## 💡 What I Learned

- PageRank only works if ranking iterations are executed  
- Visualization requires completing ALL HTML/CSS/JS dependencies  
- Folder consistency matters  
- SQLite pipelines break if scripts are run out of order  
- Force-directed graphs can load without errors but still be *incomplete*

This attempt clarified the **entire pipeline** and taught me how to organize files for browser-based visualization.

---

## 🔧 Plan for Attempt #2

- Reset database using `spreset.py`  
- Re-run crawler (100 pages)  
- Run `sprank.py` to compute new ranks  
- Run `spdump.py` to verify updated values  
- Ensure `force.css` is placed with:
  - `force_html.html`  
  - `force.js`  
  - `d3.v2.js`  

- Regenerate screenshots  
- Submit updated visualizations  
- Cross-check with instructor note before submitting  

---

## 🏁 Status

Attempt #1 completed, documented, and graded.  
Preparing for Attempt #2 with full understanding of required workflow.

---

