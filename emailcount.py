import sqlite3

conn = sqlite3.connect('/Users/surajnakka/Documents/Projects/Corsera Python/Database/emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

with open(r'/Users/surajnakka/Documents/Projects/Corsera Python/email.txt', 'r') as inputFile:
	for each in inputFile:
		if each.startswith('From '):
			pieaces = each.split()
			name, domain = pieaces[1].split('@')
			cur.execute('Select count from Counts where org = ?', (domain,))
			row = cur.fetchone()
			if not row:
				cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
			else:
				cur.execute('update Counts SET count = count + 1 WHERE org = ?',(domain,))
				conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()