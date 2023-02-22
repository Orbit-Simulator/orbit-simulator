#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys, random, re




class Signin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbit Simulator - Create New Account")
        self.setWindowIcon(QIcon(r'images/satellite.png'))
        self.setFixedSize(900, 600)
        self.show()
                                            
        # User name input
        self.user_name_input = QLineEdit(self)
        self.user_name_input.setGeometry(300, 250, 300, 30)
        self.user_name_text = QLabel(self)
        self.user_name_text.setText("User Name")
        self.user_name_text.setGeometry(300, 220, 330, 30)
        self.user_name_text.show()
        self.user_name_input.show()

        # Email input
        self.email_address = QLineEdit(self)
        self.email_address.setGeometry(300, 330, 300, 30)
        self.email_address_text = QLabel(self)
        self.email_address_text.setText("Email Address")
        self.email_address_text.setGeometry(300, 300, 330, 30)
        self.email_address_text.show()
        self.email_address.show()
    
        # Password input
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setGeometry(300, 410, 300, 30)
        self.password_text = QLabel(self)
        self.password_text.setText("Password")
        self.password_text.setGeometry(300, 380, 500, 30)
        self.password_text.show()
        self.password_input.show()
        
        #Create a new account button
        self.new_acc = QPushButton(self)
        self.new_acc.setGeometry(300, 450, 170, 30)
        self.new_acc.setText("Create Account")
        self.new_acc.show()
        
        #Back to Main Menu button
        self.main_menu = QPushButton(self)
        self.main_menu.setGeometry(480, 450, 120, 30)
        self.main_menu.setText("Main Menu")
        self.main_menu.show()
    
    


            

if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = Signin()
    win.show()
    app.exec_()
