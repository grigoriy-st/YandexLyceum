import sqlite3

DB_NAME = 'music_db.sqlite'

genre = 'Rock'
con = sqlite3.connect(DB_NAME)
cur = con.cursor()

q1 = f'''
        select 
            track.TrackId
        from track
        inner join
            genre on genre.GenreId = track.GenreId
        where
            genre.Name = '{genre}'
            '''
track_ids = list(cur.execute(q1).fetchall())
track_ids = [str(i[0]) for i in track_ids]

q2 = f'''
        select distinct
            album.AlbumId
        from track
        inner join
            album on album.albumId = track.albumId
        where
            track.TrackId in ({', '.join(track_ids)})
        '''

album_ids = list(cur.execute(q2).fetchall())
album_ids = [str(i[0]) for i in album_ids]

q3 = f'''
        select distinct
            artist.name
        from artist
        inner join
            album on album.Artistid = artist.Artistid
        where
            album.AlbumId in ({', '.join(album_ids)})
        order by
            artist.name ASC
        '''

artist_names = list(cur.execute(q3).fetchall())
artist_names = [str(i[0]) for i in artist_names]

for i in artist_names:
    print(i)
