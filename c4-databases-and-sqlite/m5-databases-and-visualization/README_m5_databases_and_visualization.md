# 🗺️ M5 – Databases and Visualization  
**Folder**: `m5-databases-and-visualization`  
**Focus**: Integrating databases, geolocation APIs, and data visualization through Python, SQLite, and JavaScript  

⸻

🎯 Overview

This module brought together everything from earlier lessons — object-oriented programming, SQL, and data modeling — and applied it to real-world **geospatial visualization**. I learned to retrieve location data from external sources, parse it into a database, and plot the results on a map using the **OpenStreetMap API** with JavaScript.

Key skills practiced:
- Using geocoding APIs to retrieve latitude and longitude  
- Storing location data in SQLite databases  
- Converting `.sqlite` contents into `.js` files for map plotting  
- Visualizing geographic data using `where.html` and OpenStreetMap  
- Linking Python, SQL, and JS in a single pipeline  

⸻

🗃️ Project: Geolocation Data Visualization

Parsed and stored location data using `geoload.py`, then used `geodump.py` to create a JavaScript file of coordinates. Finally, visualized the results with `where.html`, which displayed the plotted data using OpenStreetMap.

**Files:**
- `geoload.py` – Pulls and stores location data  
- `geodump.py` – Converts SQLite data into JavaScript array  
- `opengeo.sqlite` – Final database of geocoded locations  
- `where.data` – Location input text file  
- `where.js` – Auto-generated JavaScript file of lat/lon pairs  
- `where.html` – HTML template using OpenStreetMap API  
- `geoload_university_of_central_florida.png` – Screenshot of geocoding in action  
- `geodump_university_of_central_florida.png` – Screenshot of JavaScript output  
- `mapview_university_of_central_florida.png` – Final map visualization 
- `retrieving_geodata_visualization.txt` – Notes on extracting, storing, and visualizing geodata location 

⸻

📘 Reflection

This was my favorite module of the course. It allowed me to **see code come alive on a map**, showing how backend logic (Python & SQLite) can drive real-time frontend visuals (JS & OpenStreetMap). It gave me confidence in working across tools and languages — a crucial skill for building **interactive dashboards, simulation mapping, or training data overlays**.

From a single `.txt` file to a plotted point on the globe — this tied everything together.