import sqlite3

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

howmany = int(input('How many to dump? '))
print("Top", howmany, "email list participants:")

cur.execute('''
    SELECT Senders.email, COUNT(*) 
    FROM Messages 
    JOIN Senders ON Messages.sender_id = Senders.id 
    GROUP BY Senders.email 
    ORDER BY COUNT(*) DESC 
    LIMIT ?
''', (howmany,))

for row in cur:
    print(row[0], row[1])

print("\nTop email list organizations:")

cur.execute('''
    SELECT SUBSTR(Senders.email, INSTR(Senders.email, '@')+1) AS org, COUNT(*) 
    FROM Messages 
    JOIN Senders ON Messages.sender_id = Senders.id 
    GROUP BY org 
    ORDER BY COUNT(*) DESC 
    LIMIT ?
''', (howmany,))

for row in cur:
    print(row[0], row[1])

conn.close()
