import sqlite3
import json

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

# Get top 25 pages by new_rank
cur.execute('SELECT id, url, old_rank, new_rank FROM Pages ORDER BY new_rank DESC LIMIT 25')
pages = cur.fetchall()

node_ids = set(page[0] for page in pages)

# Fetch links between top 25 only
cur.execute('SELECT from_id, to_id FROM Links')
all_links = cur.fetchall()

filtered_links = []
for from_id, to_id in all_links:
    if from_id in node_ids and to_id in node_ids and from_id != to_id:
        filtered_links.append((from_id, to_id))

data = {
    'nodes': [],
    'links': []
}

for page_id, url, old_rank, new_rank in pages:
    data['nodes'].append({
        'id': page_id,
        'url': url,
        'old_rank': old_rank,
        'new_rank': new_rank
    })

for from_id, to_id in filtered_links:
    data['links'].append({
        'source': from_id,
        'target': to_id
    })

with open('spider.js', 'w') as f:
    f.write("spiderJson = ")
    json.dump(data, f, indent=2)
    f.write(";")

print("Lightweight spider.js with top 25 nodes generated.")
