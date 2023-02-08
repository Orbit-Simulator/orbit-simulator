from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys, pymysql, aws_sql_conn as awsdb

class Signin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbit Simulator - Create New Account")
        self.setWindowIcon(QIcon(r'images/satellite.png'))
        self.setFixedSize(700, 400)
        self.show()
        
        def create_account(user, passwd, email):
            # user_name = self.user_name_input.text()
            # password = self.password_input.text()
            # email = self.email_address.text()
            db = awsdb.db
            cursor = db.cursor()
            with cursor:
                create_new_user_query = "CREATE USER {0} IDENTIFIED BY {1};".format(user, passwd)
                print(create_new_user_query)
                # cursor.execute(create_new_user_query, (user_name, password))
                db.commit()
                
                        
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
        
        #Login button
        self.login = QPushButton(self)
        self.login.setGeometry(290, 255, 150, 30)
        self.login.setText("Create Account")
        self.login.clicked.connect(create_account(self.user_name_input.text(), self.password_input.text(), self.email_address.text()))
        self.login.show()
        
        #Create accout button
        self.register = QPushButton(self)
        self.register.setGeometry(290, 305, 150, 30)
        self.register.setText("Back to Main Menu")
        self.register.show()



if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = Signin()
    win.show()
    app.exec_()
