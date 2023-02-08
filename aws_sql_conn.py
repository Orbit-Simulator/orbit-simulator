import pymysql

host_name = 'orbit-simulator.cvwquqtl5fz5.eu-central-1.rds.amazonaws.com'
user_name = 'register'
passwd = 'register'
db_port = 3306

db = pymysql.connect(host = host_name,
                     user = user_name,
                     password = passwd,
                     port = db_port)

cursor = db.cursor()
db.commit()
