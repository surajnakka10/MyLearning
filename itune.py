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
for each in item_holder:
	found = False
	for entry in each:
		if found:
		    print(entry.text)
		    found = False
    	if entry.tag == 'key' and entry.text == 'Artist':
    		found = True
