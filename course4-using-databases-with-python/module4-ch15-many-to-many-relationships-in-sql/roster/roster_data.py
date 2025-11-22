import json
import sqlite3

# Connect to DB
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Drop and create tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Open the JSON file
fname = 'roster_data.json'
with open(fname) as f:
    data = json.load(f)

# Format: [ [ "Charley", "si110", 1 ], ... ]
for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # Insert user
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert course
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert member (with role!)
    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)',
                (user_id, course_id, role))

# Save to DB
conn.commit()

# Optional: Show a few rows to confirm
print("\n Sample query output:")
for row in cur.execute('''
SELECT User.name, Course.title, Member.role
FROM User JOIN Member JOIN Course
ON User.id = Member.user_id AND Course.id = Member.course_id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2
'''):
    print(row)

cur.close()
