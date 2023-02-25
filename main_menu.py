#!/usr/bin/python3

from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox, QPlainTextEdit, QHBoxLayout, QVBoxLayout, QMainWindow, QFormLayout, QGroupBox)
from PyQt5.QtGui import (QIcon, QPixmap)
from PyQt5.QtCore import (QSize, Qt)
import sys, random, re
from pysnc import ServiceNowClient
# from login import user_client


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Orbit Simulator - Main Menu")
        self.setWindowIcon(QIcon(r'images/satellite.png'))
        self.setFixedSize(900, 600)
        self.show()
    
        # Left Navigation Menu
        self.new_rocket_button = QPushButton(self)
        self.new_rocket_button.setText("Create New Rocket")
        self.new_rocket_button.setGeometry(20, 150, 170, 20)
        self.new_rocket_button.show()
       
        self.new_satelite_button = QPushButton(self)
        self.new_satelite_button.setText("Create New Satelite")
        self.new_satelite_button.setGeometry(20, 190, 170, 20)
        self.new_satelite_button.show()

        self.view_hangar_button = QPushButton(self)
        self.view_hangar_button.setText("View Hangar")
        self.view_hangar_button.setGeometry(20, 230, 170, 20)
        self.view_hangar_button.show()

        self.track_satelites = QPushButton(self)
        self.track_satelites.setText("Track Satelites")
        self.track_satelites.setGeometry(20, 270, 170, 20)
        self.track_satelites.show()

if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = MainMenu()
    win.show()
    app.exec_()
