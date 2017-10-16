import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('/Users/surajnakka/Documents/Projects/Corsera Python/Database/itunedb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

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
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
'''
	)

input_parse = ET.parse('/Users/surajnakka/Documents/Projects/Corsera Python/Library.xml')
item_holder = input_parse.findall('dict/dict/dict')
output = {}
for each in item_holder:
    found = False
    for entry in each:
        if found:
            output[tag1] = entry.text
            found =False
        if entry.tag == 'key' and entry.text in ['Genre', 'Artist', 'Album', 'Name', 'Total Time', 'Rating', 'Play Count']:
            found = True
            tag1 = entry.text
    if output.get('Name') is None or output.get('Artist') is None or output.get('Album') is None or output.get('Genre') is None:
        continue 
    cur.execute('insert or ignore into Artist(name) values(?)',(output['Artist'],))
    cur.execute('insert or ignore into Genre(name) values(?)',(output['Genre'],))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (output['Artist'], ))
    artist_id = cur.fetchone()[0]
    print output['Artist'], artist_id
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( output['Album'], artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (output['Album'], ))
    album_id = cur.fetchone()[0]
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (output['Genre'], ))
    genre_id = cur.fetchone()[0]
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ? ,?)''', 
        ( output['Name'], album_id, genre_id, output.get('Total Time'), output.get('Rating'), output.get('Play Count') ) )
    conn.commit()
    output = {}
