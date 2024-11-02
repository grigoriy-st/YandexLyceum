import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    _ = cur.execute(
        '''
        delete from films
        where films.id IN (
            select films.id
            from films inner join genres on genres.id = films.genre
            where films.year < 2000 
              and films.duration > 30 
              and genres.title = 'фантастика'
        )
        '''
    )
