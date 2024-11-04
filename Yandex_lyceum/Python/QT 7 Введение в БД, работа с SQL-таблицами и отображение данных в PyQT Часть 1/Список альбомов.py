import sqlite3

con = sqlite3.connect('music_db.sqlite')
cur = con.cursor()

genre_name = input()
track_names = cur.execute(
    f'''
    select distinct
    album.Title
    from
        Album
    inner join artist on album.ArtistId = artist.ArtistId
    inner join track on album.AlbumId = track.AlbumId
    inner join genre on genre.GenreId = track.GenreId
    where genre.Name = '{genre_name}'
    order by
        artist.ArtistId,
        album.Title
    ''').fetchall()

for name in track_names:
    print(name[0])

con.close()
