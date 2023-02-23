#!/usr/bin/python3
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys, random, re
import servicenow_auth
from datetime import datetime


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
        self.new_acc = QPushButton(self, clicked = self.create_user)
        self.new_acc.setGeometry(300, 450, 170, 30)
        self.new_acc.setText("Create Account")
        self.new_acc.show()
        
        #Back to Main Menu button
        self.main_menu = QPushButton(self)
        self.main_menu.setGeometry(480, 450, 120, 30)
        self.main_menu.setText("Main Menu")
        self.main_menu.show()
    
    # Register new user in Orbit Simulator Users Table && CMDB Users Table
    def create_user(self):
        if Signin.check_unique_username(self) == True and\
            Signin.check_valid_username(self) == True and\
                Signin.check_password(self) == True and\
                    Signin.check_email(self) == True:
            gr = servicenow_auth.client.GlideRecord('u_orbit_simulator_users')
            gr.initialize()
            gr.u_id = Signin.generate_user_id(self)
            gr.u_user_name = self.user_name_input.text()
            gr.u_password = self.password_input.text()
            gr.u_email_address = self.email_address.text()
            gr.u_date_created = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            gr.insert()
            
            gr = servicenow_auth.client.GlideRecord('sys_user')
            gr.initialize()
            gr.user_name = self.user_name_input.text()
            gr.user_password = self.password_input.text()
            gr.email = self.email_address.text()
            gr.sys_created_on = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            gr.name = f'Orbit Simulator - {self.user_name_input.text()}'
            gr.insert()
        else:
            Signin.error_handling(self)
    
    # Generate new user unique ID
    def generate_user_id(self):
        user_id = []
        length = 10 
        for i in range(length):
            if i < 3:
                user_id.append(chr(random.randrange(65,90)))
            else:
                user_id.append(chr(random.randrange(48,57)))
        user_id = ''.join(user_id)
        gr = servicenow_auth.client.GlideRecord('u_orbit_simulator_users')
        gr.query()
        for user in gr:
            to_check = gr.get_value('u_id')
            if to_check == user_id:
                Signin.generate_user_id(self)
            else:
                return user_id

    # Check if user name is unique
    def check_unique_username(self):
        gr = servicenow_auth.client.GlideRecord('u_orbit_simulator_users')
        gr.query()
        for username in gr:
            to_check = gr.get_value('u_user_name')
            if to_check == self.user_name_input.text():
                return False
            else:
                return True
    
    # Check if username is valid
    def check_valid_username(self):
        if len(self.user_name_input.text()) < 6:
            return False
        else:
            return True
    
    # Check if password is valid
    def check_password(self):
        to_check = self.password_input.text()
        while True:
            if (len(to_check)) < 6:
                return False
            elif not re.search("[A-Z]", to_check):
                return False
            elif not re.search("[a-z]", to_check):
                return False
            elif not re.search("[0-9]", to_check):
                return False
            elif not re.search("[!@\#$%&')(*+`./]", to_check):
                return False
            elif re.search("\s", to_check):
                return False
            else:
                return True
    
    # Check if email is valid
    def check_email(self):
        to_check = self.email_address.text()
        if re.search("^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$", to_check):
            return True
        else:
            return False        

    # Pop-up window with error messages
    def error_handling(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Error during creating new account")
        message_box.setText("Please check and fix the following issues:")
        message_box.setIcon(QMessageBox.Critical)
        message_box.setStandardButtons(QMessageBox.Ok)
        details_msg = []
        
        if Signin.check_unique_username(self) == False:
            details_msg.append("Username already exists\n")
        if Signin.check_valid_username(self) == False:
            details_msg.append("Invalid username. Username must be at least 6 characters\n")
        if Signin.check_password(self) == False:
            details_msg.append("Password must be at least 6 characters long, containing one upper case letter, one lowercase letter, one number and one special symbol.\n")
        if Signin.check_email(self) == False:
            details_msg.append("Invalid email address\n")
        
        message_box.setDetailedText(''.join(details_msg))
        x = message_box.exec()

            

if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = Signin()
    win.show()
    app.exec_()
