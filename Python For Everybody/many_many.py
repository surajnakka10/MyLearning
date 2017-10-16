import json
import sqlite3

conn = sqlite3.connect('/Users/surajnakka/Documents/Projects/Corsera Python/Database/rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

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


with open ('/Users/surajnakka/Documents/Projects/Corsera Python/roster_data.json') as reader:
	 data = json.loads(reader.read())
	 for each in data:
	 	name = each[0]
	 	title = each[1]
	 	role = each[2]
	 	cur.execute('''Insert or ignore into user(name) values(?)''',(name,))
	 	cur.execute('''Insert or ignore into course(title)values(?)''',(title,))
	 	cur.execute('select id from user where name = ?', (name,))
	 	user_id = cur.fetchone()[0]
	 	cur.execute('select id from course where title = ?',(title,))
	 	course_id = cur.fetchone()[0]
	 	cur.execute('''insert or replace into member(user_id, course_id, role) values (?,?,?)''', (user_id,course_id,role))
conn.commit()
