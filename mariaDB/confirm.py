# from libs.db.mariaconfig import getConn
from maria import getConn

conn=getConn()
print(conn)