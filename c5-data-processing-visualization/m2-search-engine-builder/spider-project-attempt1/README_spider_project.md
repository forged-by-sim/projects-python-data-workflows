# 🕷️ Project – Web Spider & PageRank Visualization  
**Folder**: `spider-project-attempt1`  
**Project Type**: Web Crawling · PageRank · SQLite · D3.js Visualization  
**Tools Used**: Python, SQLite, `urllib`, `BeautifulSoup`, D3.js  

⸻

## 🎯 Project Overview  
This project implemented a mini search engine by crawling pages, storing hyperlinks in a database, calculating PageRank scores, and visualizing the results as a **force-directed graph**. The goal was to spider two sets of 100+ pages each, compute link-based rankings, and render them using `force.html`.

This was my **first attempt** at the honors assignment, which earned a score of 70%. The attempt helped me identify the importance of file order, CSS dependencies, and full pipeline execution.

⸻

## 🧪 Technical Breakdown  
The project was completed in four key stages:

1. **Spider Pages** using `spider.py`  
   - Crawled and stored page data in `spider.sqlite`  
   - Built `Pages`, `Links`, and `Webs` tables

2. **Compute Rankings** using `sprank.py`  
   - Iteratively updated the `Rank` field  
   - Based on link structure from `Pages` and `Links`

3. **Dump Results** using `spdump.py`  
   - Exported `old_rank` and `new_rank` for each page  
   - Verified graph convergence and URL rankings

4. **Visualize** using `force.html`  
   - Used D3.js to display a node-link web graph  
   - Required `d3.v2.js`, `force.js`, and `force.css`

⸻

## 📂 Files Included

| File | Description |
|------|-------------|
| `spider.py`, `sprank.py`, `spdump.py`, `spreset.py` | Scripts to crawl pages, calculate PageRank, and reset the database |
| `spider.sqlite` | SQLite database tracking pages and links |
| `force.html`, `d3.v2.js`, `force.js` | Interactive force-directed graph (browser-based) |
| `spdump_100pages.png`, `spdump_109pages.png` | Screenshots of database output dumps |
| `html_quotestoscrape.png`, `html_sparsed_dots_bryony.png` | Force graph visualizations for both crawled sites |
| `README_spider_project.txt` | Full attempt log with root cause analysis, errors, and next-step plan |

⸻

## 🧠 Key Learnings  
This project revealed the **sensitivity of multi-stage pipelines**. I discovered that missing even one step (e.g. not running `sprank.py`) causes the final graph to display default values. I also learned that CSS (`force.css`) is essential for rendering node connections, and that file placement impacts browser loading behavior.

Most importantly, I gained a deeper understanding of:

- PageRank algorithms  
- Link-based authority modeling  
- Pipeline debugging across Python, SQL, and JS  
- How to fix graph rendering errors due to missing assets or incorrect script order  

⸻

## ⚠️ What Went Wrong

- Skipped `sprank.py`, so rankings were never updated  
- `force.css` was missing, causing graph to show "floating dots"  
- Folder structure placed key assets in `ot/`, breaking visualization links  
- Graph displayed but lacked interactivity and connections

⸻

## 🛠️ Plan for Attempt #2  
- Use `spreset.py` to reset the database  
- Re-run spidering with 100+ pages  
- Run `sprank.py` before dumping  
- Ensure `force.css` is in the same folder as `force.html`  
- Regenerate screenshots for updated graphs  
- Submit a cleaner, fully working version with instructor confirmation

⸻

## 💬 Reflection  
Despite the mistakes, this attempt clarified the **entire pipeline**. It was a turning point in understanding how each file connects, why order matters, and how visualization relies on backend correctness. This project mimicked real-world scenarios where systems silently fail if small components go missing or misfire.

---
