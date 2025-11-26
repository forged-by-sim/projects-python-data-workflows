import sqlite3
import collections

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('SELECT subject FROM Messages')
counts = dict()

for row in cur:
    text = row[0]
    if text is None:
        continue
    words = text.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print("Loaded", len(counts), "words")
biglist = sorted([(v, k) for k, v in counts.items()], reverse=True)

fhand = open('gword.js', 'w')
fhand.write("gword = [\n")
for count, word in biglist[:100]:
    fhand.write("{text: '" + word + "', size: " + str(count) + "},\n")
fhand.write("\n];\n")
fhand.close()
print("Output written to gword.js")
print("Open gword.htm in a browser to view")
