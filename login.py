from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys, random, re
from pysnc import ServiceNowClient
import servicenow_admin_auth

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbit Simulator - Login")
        self.setWindowIcon(QIcon(r'images/satellite.png'))
        self.setFixedSize(900, 600)
        self.show()

        # User name input
        self.user_name_input = QLineEdit(self)
        self.user_name_input.setGeometry(300, 350, 300, 30)
        self.user_name_text = QLabel(self)
        self.user_name_text.setText("User Name")
        self.user_name_text.setGeometry(300, 320, 330, 30)
        self.user_name_text.show()
        self.user_name_input.show()
    
        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setGeometry(300, 410, 300, 30)
        self.password_text = QLabel(self)
        self.password_text.setText("Password")
        self.password_text.setGeometry(300, 380, 500, 30)
        self.password_text.show()
        self.password_input.show()
        
        # Login button
        self.new_acc = QPushButton(self)
        self.new_acc.setGeometry(300, 450, 170, 30)
        self.new_acc.setText("Login")
        self.new_acc.show()
        
        #Back to Main Menu button
        self.main_menu = QPushButton(self)
        self.main_menu.setGeometry(480, 450, 120, 30)
        self.main_menu.setText("Register")
        self.main_menu.show()

    # Login with existing credentials
    def sign_in(self):
        user_client = ServiceNowClient('https://dev109438.service-now.com/',
                                       self.user_name_input.text(),
                                       self.password_input.text())
        return user_client
    





if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    app.exec_()