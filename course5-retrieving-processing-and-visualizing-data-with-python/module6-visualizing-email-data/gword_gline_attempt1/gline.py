import sqlite3
import datetime

# Open both index and content databases
conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

conn2 = sqlite3.connect('content.sqlite')
cur2 = conn2.cursor()

counts = dict()

# Read and count messages by YYYY-MM
for row in cur2.execute('SELECT sent_at FROM Messages'):
    try:
        sent_at = row[0]
        if sent_at is None or len(sent_at) < 10:
            continue
        dt = datetime.datetime.strptime(sent_at[:10], '%Y-%m-%d')
        key = dt.strftime('%Y-%m')
        counts[key] = counts.get(key, 0) + 1
    except:
        continue

# Sort the data
sorted_counts = sorted(counts.items())

# Write to gline.js
with open('gline.js', 'w') as f:
    f.write("gline = [ ['Year', 'Messages']")
    for key, val in sorted_counts:
        f.write(f",\n['{key}', {val}]")
    f.write("\n];\n")

print(" Data successfully written to gline.js")
