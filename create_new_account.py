#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit)
from PyQt5.QtGui import (QIcon, QPixmap)
import sys, pymysql, random, re
import aws_sql_conn as awsdb


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
        self.login = QPushButton(self, clicked=self.create_account)
        self.login.setGeometry(300, 450, 170, 30)
        self.login.setText("Create Account")
        self.login.show()
        
        #Back to Main Menu button
        self.register = QPushButton(self)
        self.register.setGeometry(480, 450, 120, 30)
        self.register.setText("Main Menu")
        self.register.show()
    
    
    def create_account(self):
        user_name = self.user_name_input.text()
        email = self.email_address.text()
        passwd = self.password_input.text()
        if Signin.check_user_name(self) == True and Signin.check_password(self) == True \
            and Signin.check_email(self) == True:
            db = awsdb.db
            cursor = db.cursor()
            with cursor:
                create_new_user_query = """INSERT INTO users VALUES (%s, %s, %s);"""
                cursor.execute(create_new_user_query, (Signin.generate_user_id(self), user_name, email))
                create_new_user_query = """CREATE USER %s IDENTIFIED BY %s"""
                cursor.execute(create_new_user_query, (user_name, passwd))
                db.commit()
                Signin.account_created(self)
        else:
            Signin.error_handling(self)
            
            
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
    
    # Function verifies if the user name is in correct format           
    def check_user_name(self): 
        to_check = self.user_name_input.text()
        if 6 <= len(to_check) <= 20:
            return True
        else:
            return False
    
    # Function verifies if the password is in correct format
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
                
    # Function verifies if the email is correct
    def check_email(self):
        to_check = self.email_address.text()
        if re.search("^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$", to_check):
            return True
        else:
            return False

    # Pop-up window with feedback when any of the input(username, passwd, email) is incorrect
    def error_handling(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Error during creating new account")
        message_box.setText("Please check and fix the following issues: ")
        message_box.setIcon(QMessageBox.Critical)
        message_box.setStandardButtons(QMessageBox.Ok)
        details_msg = []
        
        if Signin.check_user_name(self) == False:
            details_msg.append("User name must be between 6 and 20 characters long.\n")
        if Signin.check_password(self) == False:
            details_msg.append("Password must be at least 6 characters long, containing one upper case letter, one lowercase letter, one number and one special symbol.\n")
        if Signin.check_email(self) == False:
            details_msg.append("Invalid email address.\n")

        message_box.setDetailedText(''.join(details_msg))
        x = message_box.exec()
    
    # Inform the user that the account has been created succesfully
    def account_created(self):
        succesfull_acc = QLabel(self)
        succesfull_acc.setText("Your account has been created succesfully!")
        succesfull_acc.setGeometry(300, 500, 400, 30)
        succesfull_acc.show()

            

if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = Signin()
    win.show()
    app.exec_()
