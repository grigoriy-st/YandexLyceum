import sqlite3

con = sqlite3.connect('music_db.sqlite')
cur = con.cursor()

genre_name = input()
album_names = cur.execute(f'''
    select distinct album.title
    from 
        track inner join genre on track.genreid = genre.genreid
        track inner join album on track.albumid = album.albumid
        album inner join artist on artist.artistid = album.artistid
    where
        genre.genreid = '{genre_name}'
    order by 
        artist.artistid
        artist.Name
''').fetchall()

for name in track_names:
    print(name[0])

con.close()
