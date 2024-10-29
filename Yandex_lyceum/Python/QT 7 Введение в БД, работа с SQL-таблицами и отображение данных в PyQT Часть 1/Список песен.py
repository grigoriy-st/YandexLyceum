import sqlite3

author = input()
con = sqlite3.connect('music_db.sqlite')
cur = con.cursor()

track_names = cur.execute(f'''
    select distinct track.name
    from track 
        inner join album on track.trackid = album.albumid
        inner join artist on album.albumid = artist.artistid
    where artist.name = '{author}'
    order by track.name
''').fetchall()

for name in track_names:
    print(name)


