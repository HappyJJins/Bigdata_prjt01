from db import getConn

def insertData(date, cate, title):
    conn = getConn()
    cur = conn.cursor()
    ins_query = 'insert into crowling values({},"{}","{}")'.format(date, cate, title)
    cur.execute(ins_query)
    conn.commit()
    conn.close()