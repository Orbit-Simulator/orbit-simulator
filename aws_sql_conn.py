import pymysql

host_name = 'localhost'
user_name = 'root'
passwd = 'Password1'
db_port = 3306

db = pymysql.connect(host = host_name,
                     user = user_name,
                     password = passwd,
                     port = db_port)

cursor = db.cursor()
db.commit()
