# 🔗 Project – Following Links with BeautifulSoup  
**Folder**: `m4-html-parsing-urllib`  
**Project Type**: Web Scraping · Link Traversal · HTML Automation  
**Tools Used**: Python, `urllib`, `BeautifulSoup`  

⸻

## 🎯 Project Overview  
This project simulated automated web navigation by following a series of embedded links using BeautifulSoup. The core logic involved selecting the **18th `<a>` tag** from each retrieved HTML page, extracting its `href`, and repeating the process **7 times** to identify a final target name.

I learned how to:

- Parse HTML with BeautifulSoup  
- Locate and iterate over `<a>` tags  
- Use `.get('href')` to extract links  
- Index into lists of elements safely  
- Automate repetitive traversal tasks with loop logic  

⸻

## 📂 Files Included  
- `following-links-in-python.py` – Python script to follow 18th link, 7 times  
- `solution-following-links-in-python.txt` – Step-by-step explanation of logic and loop structure  
- `known_by_Jemma.html` – Static HTML file for reproducible testing  
- `prompt_following_links_in_python1.png`  
- `prompt_following_links_in_python2.png`  
- `results_following_links_in_python.png` – Terminal output showing successful final name

⸻

## 🧠 Key Learnings  
This challenge strengthened my ability to traverse and manipulate real-world HTML structures, especially in situations where reliability, repeatability, and structure-aware indexing matter.

I also saw the value of using preserved `.html` files to debug or demonstrate scraping logic without worrying about changing external URLs or connectivity issues.

⸻

## 💡 Use Case Inspiration  
- Simulated training logs that jump between nested resources  
- Scraping linked citations, paginated content, or breadcrumb trails  
- Simulation scoreboards and multi-step training flows linked by anchor tags  

---
