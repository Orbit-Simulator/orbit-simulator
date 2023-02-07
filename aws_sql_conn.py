import pymysql

#db = pymysql.connect(host="orbit-simulator.cvwquqtl5fz5.eu-central-1.rds.amazonaws.com",
#                    user="admin",
#                     password="ParolA12345!!",
#                    port=3306)

host_name = 'orbit-simulator.cvwquqtl5fz5.eu-central-1.rds.amazonaws.com'
user_name = ''
passwd = ''
db_port = 3306

db = pymysql.connect(host = host_name,
                     user = user_name,
                     password = passwd,
                     port = db_port)

cursor = db.cursor()
db.commit()
