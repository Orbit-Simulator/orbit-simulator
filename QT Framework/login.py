from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys, pymysql, aws_sql_conn



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
    


if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    app.exec_()


