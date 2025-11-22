import sqlite3
import csv

# Connect to SQLite
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Drop old tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
''')

# Create tables
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE,
    artist_id  INTEGER
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Read CSV and populate tables
fname = 'tracks.csv'
with open(fname, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header

    for row in reader:
        if len(row) < 7:
            continue

        title = row[0]
        artist = row[1]
        album = row[2]
        genre = row[3]
        count = row[4]
        rating = row[5]
        length = row[6]

        # Insert artist
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
        artist_id = cur.fetchone()[0]

        # Insert genre
        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
        genre_id = cur.fetchone()[0]

        # Insert album
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
        album_id = cur.fetchone()[0]

        # Insert track
        cur.execute('''
        INSERT OR REPLACE INTO Track 
        (title, album_id, genre_id, len, rating, count)
        VALUES (?, ?, ?, ?, ?, ?)''',
        (title, album_id, genre_id, length, rating, count))

# Save DB
conn.commit()

# Check sample output
print("\nSample output:")
cur.execute('''
SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track 
JOIN Genre ON Track.genre_id = Genre.id 
JOIN Album ON Track.album_id = Album.id 
JOIN Artist ON Album.artist_id = Artist.id 
ORDER BY Artist.name LIMIT 3
''')

for row in cur.fetchall():
    print(row)

cur.close()
