from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys, pymysql, random, re
import aws_sql_conn as awsdb


class Signin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbit Simulator - Create New Account")
        self.setWindowIcon(QIcon(r'images/satellite.png'))
        self.setFixedSize(700, 400)
        self.show()
                                            
        # User name input
        self.user_name_input = QLineEdit(self)
        self.user_name_input.setGeometry(220, 105, 300, 30)
        self.user_name_input.show()

        # Email input
        self.email_address = QLineEdit(self)
        self.email_address.setGeometry(220, 155, 300, 30)
        self.email_address.show()
    
        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setGeometry(220, 205, 300, 30)
        self.password_input.show()
        
        #Create a new account button
        self.login = QPushButton(self, clicked=self.create_account)
        self.login.setGeometry(290, 255, 170, 30)
        self.login.setText("Create Account")
        self.login.show()
        
        #Back to Main Menu button
        self.register = QPushButton(self)
        self.register.setGeometry(290, 305, 170, 30)
        self.register.setText("Back to Main Menu")
        self.register.show()
    
    
    def create_account(self):
        user_name = self.user_name_input.text()
        email = self.email_address.text()
        passwd = self.password_input.text()
        if Signin.check_user_name(self) == True and Signin.check_password(self) == True:
            db = awsdb.db
            cursor = db.cursor()
            with cursor:
                create_new_user_query = """INSERT INTO users VALUES (%s, %s, %s);"""
                cursor.execute(create_new_user_query, (Signin.generate_user_id(self), user_name, email))
                create_new_user_query = """CREATE USER %s IDENTIFIED BY %s"""
                cursor.execute(create_new_user_query, (user_name, passwd))
                db.commit()
            
    def generate_user_id(self):
        user_id = []
        length = 10 
        for i in range(length):
            if i < 3:
                user_id.append(chr(random.randrange(65,90)))
            else:
                user_id.append(chr(random.randrange(48,57)))
        awsdb.cursor.execute("""SELECT * FROM users;""")
        result = awsdb.cursor.fetchall()
        for row in result:
            to_check = row[0]
            if to_check == ''.join(user_id):
                generate_user_id()
            else:
                return ''.join(user_id)
                
    def check_user_name(self):
        to_check = self.user_name_input.text()
        if 6 < len(to_check) < 15:
            return True
        else:
            return False

    def check_password(self):
        to_check = self.password_input.text()
        while True:
            if (len(to_check)) < 6:
                return False
            elif not re.search("[A-Z]", to_check):
                return False
            elif not re.search("[a-z]", to_check):
                return False
            elif not re.seach("[0-9]", to_check):
                return False
            elif not re.search("[!@\#$%&')(*+`-./]", to_check):
                return False
            elif re.seach("\s", to_check):
                return False
            else:
                return True
                
    def check_email(self):
        pass
            

if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = Signin()
    win.show()
    app.exec_()
