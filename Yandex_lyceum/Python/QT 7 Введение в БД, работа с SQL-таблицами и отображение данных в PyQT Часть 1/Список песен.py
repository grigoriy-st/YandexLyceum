import sqlite3

author = input()
con = sqlite3.connect('music_db.sqlite')
cur = con.cursor()

try:
    result = cur.execute(
        f'''
        select distinct track.Name 
        from 
            track
        join 
            album ON album.AlbumId = track.AlbumId,
            artist ON artist.artistId = album.ArtistId
        where 
            artist.Name = {author}
        order by 
            track.Name
        '''
    )
    for track in result:
        print(track)
except sqlite3.OperationalError:
    ...
finally:
    con.close()