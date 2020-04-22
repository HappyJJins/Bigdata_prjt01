from db import getConn

def create_table():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('''create table crowling(
                                         date int,
                                         category varchar(20),
                                         title varchar(10000)
                                         )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()