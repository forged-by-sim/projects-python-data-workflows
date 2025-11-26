import sqlite3

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

# Create Senders and Messages tables in a new DB
conn2 = sqlite3.connect('index.sqlite')
cur2 = conn2.cursor()

cur2.execute('DROP TABLE IF EXISTS Messages')
cur2.execute('DROP TABLE IF EXISTS Senders')

cur2.execute('''
CREATE TABLE Senders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE
)''')

cur2.execute('''
CREATE TABLE Messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    sender_id INTEGER
)''')

# Read messages from content.sqlite
print("Reading messages from content.sqlite...")

cur.execute('SELECT email, subject FROM Messages')
senders = dict()

for row in cur:
    email = row[0]
    subject = row[1]

    if email is None or subject is None:
        continue

    if email not in senders:
        cur2.execute('INSERT OR IGNORE INTO Senders (email) VALUES (?)', (email,))
        conn2.commit()
        cur2.execute('SELECT id FROM Senders WHERE email = ?', (email,))
        sender_id = cur2.fetchone()[0]
        senders[email] = sender_id
    else:
        sender_id = senders[email]

    cur2.execute('INSERT INTO Messages (subject, sender_id) VALUES (?, ?)', (subject, sender_id))

conn2.commit()
print("Senders found:", len(senders))

cur.close()
conn.close()
cur2.close()
conn2.close()
