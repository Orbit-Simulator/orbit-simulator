from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys, pymysql



class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbit Simulator")
        self.setWindowIcon(QIcon(r'images/satellite.png'))
        self.setFixedSize(700, 400)
        self.show()

        # User name input
        self.user_name_box = QLineEdit(self)
        self.user_name_box.setGeometry(280, 105, 150, 30)
        self.user_name_box.show()

        # # Email input
        # self.email_address = QLineEdit(self)
        # self.email_address.setGeometry(280, 155, 150, 30)
        # self.email_address.show()
    
        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setGeometry(280, 155, 150, 30)
        self.password_input.show()
        
        #Login button
        self.login = QPushButton(self)
        self.login.setGeometry(280, 205, 150, 30)
        self.login.setText("Login")
        self.login.show()
        
        #Create accout button
        self.register = QPushButton(self)
        self.register.setGeometry(280, 255, 150, 30)
        self.register.setText("Create Account")
        self.register.show()
    
    def connect_to_sql():
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

if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    app.exec_()


