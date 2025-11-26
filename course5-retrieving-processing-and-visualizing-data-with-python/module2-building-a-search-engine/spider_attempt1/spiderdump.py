import sqlite3
import json

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# Get the top 25 pages by new_rank
cur.execute('''
    SELECT id, url, new_rank FROM Pages
    ORDER BY new_rank DESC LIMIT 25
''')

top_pages = cur.fetchall()
node_ids = [row[0] for row in top_pages]

# Map each node ID to index in the nodes array
node_index_map = {page_id: idx for idx, (page_id, _, _) in enumerate(top_pages)}

nodes = []
for page_id, url, new_rank in top_pages:
    nodes.append({
        "weight": 1,
        "rank": new_rank,
        "id": page_id,
        "url": url
    })

# Now collect links only between the top 25
cur.execute('SELECT from_id, to_id FROM Links')
all_links = cur.fetchall()

links = []
for from_id, to_id in all_links:
    if from_id in node_ids and to_id in node_ids:
        links.append({
            "source": node_index_map[from_id],
            "target": node_index_map[to_id]
        })

# Output spider.js
data = {
    "nodes": nodes,
    "links": links
}

with open("spider.js", "w") as f:
    f.write("spiderJson = ")
    f.write(json.dumps(data, indent=2))
    f.write(";")

print(" spider.js file with 25 nodes generated.")
