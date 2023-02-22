#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys, pymysql, back_up.aws_sql_conn as aws_sql_conn




class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbit Simulator - Login")
        self.setWindowIcon(QIcon(r'images/satellite.png'))
        self.setFixedSize(900, 600)
        self.show()

        # User name input
        self.user_name_box = QLineEdit(self)
        self.user_name_box.setGeometry(300, 250, 250, 30)
        self.user_name_label = QLabel(self)
        self.user_name_label.setText("User Name")
        self.user_name_label.setGeometry(300, 220, 100, 30)
        self.user_name_box.show()
        self.user_name_label.show()
    
        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setGeometry(300, 330, 250, 30)
        self.password_label = QLabel(self)
        self.password_label.setText("Password")
        self.password_label.setGeometry(300, 300, 100, 30)
        self.password_input.show()
        self.password_label.show()
        
        #Login button
        self.login = QPushButton(self)
        self.login.setGeometry(300, 380, 80, 30)
        self.login.setText("Login")
        self.login.show()
        
        #Create accout button
        self.register = QPushButton(self)
        self.register.setGeometry(400, 380, 150, 30)
        self.register.setText("Create Account")
        self.register.show()
    


if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    app.exec_()


