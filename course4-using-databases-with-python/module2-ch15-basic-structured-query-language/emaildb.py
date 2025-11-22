
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ').strip()
if len(fname) < 1:
    fname = 'mbox.txt'

try:
    fh = open(fname)
except FileNotFoundError:
    print(f" Could not find file: {fname}")
    exit()

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    if len(pieces) < 2:
        continue
    email = pieces[1]
    if '@' not in email:
        continue
    domain = email.split('@')[1]

    cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
print("\nTop 10 domains:")
for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()
