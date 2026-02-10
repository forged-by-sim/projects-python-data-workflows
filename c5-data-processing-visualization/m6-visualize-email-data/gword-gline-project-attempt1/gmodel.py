import sqlite3

# Connect to original message database
conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

# Create and connect to new index database
conn2 = sqlite3.connect('index.sqlite')
cur2 = conn2.cursor()

# Reset index database tables
cur2.execute('DROP TABLE IF EXISTS Messages')
cur2.execute('DROP TABLE IF EXISTS Senders')

cur2.execute('''
CREATE TABLE Senders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE
)
''')

cur2.execute('''
CREATE TABLE Messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT,
    sender_id INTEGER
)
''')

# Debug line
print("Reading messages from content.sqlite...")

# Extract relevant messages from content.sqlite
cur.execute('SELECT email, subject FROM Messages WHERE email IS NOT NULL AND subject IS NOT NULL')

senders = dict()
count = 0

for row in cur:
    email = row[0]
    subject = row[1]

    if email not in senders:
        cur2.execute('INSERT OR IGNORE INTO Senders (email) VALUES (?)', (email,))
        conn2.commit()
        cur2.execute('SELECT id FROM Senders WHERE email = ?', (email,))
        sender_id = cur2.fetchone()[0]
        senders[email] = sender_id
    else:
        sender_id = senders[email]

    cur2.execute('INSERT INTO Messages (subject, sender_id) VALUES (?, ?)', (subject, sender_id))
    count += 1

conn2.commit()
print("Total messages inserted:", count)
print("Senders found:", len(senders))

# Close everything
cur.close()
cur2.close()
conn.close()
conn2.close()
