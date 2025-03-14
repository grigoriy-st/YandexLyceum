import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    _ = cur.execute(
        '''
        delete 
        from films
        
        where films.id in (
            select films.id
            from films inner join genres on genres.id = films.genre
            where genres.title = 'боевик' and films.duration >= 90
        )
        '''
    )
