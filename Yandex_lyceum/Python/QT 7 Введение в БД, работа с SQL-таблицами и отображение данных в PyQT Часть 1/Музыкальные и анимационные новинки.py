import sqlite3

con = sqlite3.connect(input())

cur = con.cursor()

result = cur.execute("""select films.title
from films inner join genres on genres.id=films.genre
where genres.title='комедия' and films.duration>=60""").fetchall()

for elem in result:
    print(elem[0])

con.close()
