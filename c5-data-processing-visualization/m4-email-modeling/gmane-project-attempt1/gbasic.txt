import sqlite3

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

# Join Messages with Senders to get the sender email
cur.execute('''
    SELECT Senders.email, Messages.subject
    FROM Messages JOIN Senders
    ON Messages.sender_id = Senders.id
''')

counts = dict()
for message in cur:
    sender = message[0]
    subject = message[1]

    if sender not in counts:
        counts[sender] = 1
    else:
        counts[sender] += 1

print('Loaded messages=', len(counts))

while True:
    sval = input('How many to dump: ')
    if len(sval) < 1:
        break
    try:
        count = int(sval)
    except:
        print("Please enter a number.")
        continue

    if count > 0:
        for key in sorted(counts, key=counts.get, reverse=True)[:count]:
            print(key, counts[key])
