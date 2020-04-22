from maria import getConn

#테이블 값 보여주기(select)
def select_a():
    conn = getConn()
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM hj')

    result = cur.fetchall()

    for i in result:
        print(i)

    conn.close()

if __name__ == '__main__' :
    select_a()