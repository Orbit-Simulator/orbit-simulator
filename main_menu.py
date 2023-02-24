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
        # self.setFixedSize(900, 600)
        self.show()



if __name__ == "__main__":            
    app = QApplication(sys.argv)
    win = MainMenu()
    win.show()
    app.exec_()