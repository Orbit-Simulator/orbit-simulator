# import aws_sql_conn as awsdb

# def create_account(name, passwd, email):
#     # user_name = self.user_name_input.text()
#     # password = self.password_input.text()
#     # email = self.email_address.text()
#     db = awsdb.db
#     cursor = db.cursor()
#     cursor.execute("""USE orbit_simulator;""")
#     db.commit()
#     with cursor:
#         # create_new_user_query = """CREATE USER `test`@`local` IDENTIFIED BY `test`;"""
#         create_new_user_query = """INSERT INTO users VALUES (%s, %s, %s)"""
#         print(create_new_user_query)
#         cursor.execute(create_new_user_query, (name, passwd, email))
#         db.commit()

# # create_account()