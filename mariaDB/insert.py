
from maria import getConn

def insert_value(name, kor, eng, mat):
    conn = getConn()
    cursor = conn.cursor()
    ins_query = "insert into hj values('{}', {}, {}, {})".format(name, kor, eng, mat)
    cursor.execute(ins_query)
    conn.commit()
    conn.close()

def insert_b():
    conn=getConn()
    cur=conn.cursor()
    ins_query='insert into hj values(%s, %d, %d, %d)'
    li=[('김철수',78,51,45),('이영희',84,75,92),('김창수',84,23,49)]
    cur.executemany(ins_query.li)

    conn.commit()
    conn.sclo
if __name__ == "__main__":
    insert_value("홍길동", 70, 80, 90)