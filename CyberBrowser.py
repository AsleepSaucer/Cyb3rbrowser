#Project: Cyberbrowser
#Goal: make a functional web browser within python, add additional functions as possible and as time allows
#By: Jack Sieverding
#Date last edited: 11/7/2022
#Made in python 3.10.8
#imports to help with the browser
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
#sets up the Window class 
class Window(QMainWindow):
    def __init__(self):
        super(). __init__()
        
        #gives browser title, icon, and dimentions when launched
        self.setWindowTitle("Cyberbrowser")
        self.setWindowIcon(QIcon("icons/cyber.png"))
        self.setGeometry(200,200,900,600)
        
        #sets up the toolbar within the browser
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        #sets up back button and gives icon to button
        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("icons/back.png"))
        self.backButton.setIconSize(QSize (18,18))
        self.backButton.clicked.connect(self.backBTN)
        toolbar.addWidget(self.backButton)
        
        #sets up forward button and gives icon to button
        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("icons/forward.png"))
        self.forwardButton.setIconSize(QSize (18,18))
        self.forwardButton.clicked.connect(self.forwardBTN)
        toolbar.addWidget(self.forwardButton)
        
        #sets up refresh button and gives icon to button
        self.refreshButton = QPushButton()
        self.refreshButton.setIcon(QIcon("icons/refresh.png"))
        self.refreshButton.setIconSize(QSize (18,18))
        self.refreshButton.clicked.connect(self.refreshBTN)
        toolbar.addWidget(self.refreshButton)
        
        #sets up home button and gives icon to button
        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("icons/home.png"))
        self.homeButton.setIconSize(QSize (18,18))
        self.homeButton.clicked.connect(self.homeBTN)
        toolbar.addWidget(self.homeButton)
        
        #adds space to add addresses into the browser
        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Sanserif", 12))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolbar.addWidget(self.addressLineEdit)
        
        #sets up search button and gives icon to button
        self.searchbutton = QPushButton()
        self.searchbutton.setIcon(QIcon("icons/search.png"))
        self.searchbutton.setIconSize(QSize (18,18))
        self.searchbutton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchbutton)
        
        #sets the web browsing funtion and the first webpages that shows up
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'https://google.com'
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))
    
    #builds in the functionality for searching    
    def searchBtn(self):
        myurl = self.addressLineEdit.text()
        self.webEngineView.load(QUrl(myurl))
     
    #fucntionality for the back button   
    def backBTN(self):
        self.webEngineView.back()
        
    #fucntionality for the forward button 
    def forwardBTN(self):
        self.webEngineView.forward()
        
    #functionality for the reload button
    def refreshBTN(self):
        self.webEngineView.reload()    
    
    #functionality for the home button
    def homeBTN(self):
        self.webEngineView.load(QUrl('http://google.com'))
        
#creats a simple window for the application      
app = QApplication(sys.argv)
window=Window()
window.show()
sys.exit(app.exec_())