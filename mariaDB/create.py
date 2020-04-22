from maria import getConn

def create_table():
    conn=getConn()
    cur=conn.cursor()
    cur.execute('''
        create table hj(
            name varchar(20),
            kor int,
            math int,
            eng int)
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()