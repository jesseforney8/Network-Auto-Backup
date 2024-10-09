import sqlite3


def create_db():
## create db

    try:

        ### create or connect to db

        conn = sqlite3.connect("devices.db")

        ### create curser
        c = conn.cursor()

        ## create table

        c.execute("""CREATE TABLE devices (
                name text,
                ip text,
                username text,
                password text,
                secret text,
                filepath text,
                backed_up boolean,
                date1 text,
                schedule integer
                )""")

        conn.commit()

    except:
        pass


