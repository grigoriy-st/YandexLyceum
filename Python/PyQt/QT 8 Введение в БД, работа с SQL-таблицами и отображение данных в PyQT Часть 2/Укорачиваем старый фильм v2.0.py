import sqlite3


def get_result(name):
    con = sqlite3.connect(name)
    cur = con.cursor()
    _ = cur.execute(
        '''
        update films
        set
            duration = duration / 3
        where films.year = 1973
        '''
    ).fetchall()

    con.commit()
