import sys
import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Coronavirus stat checker'
        self.left = 10
        self.top = 10
        self.width = 350
        self.height = 100
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(40, 20)
        self.textbox.resize(250,20)
        
        # Create a button in the window
        self.button = QPushButton('Check Stats', self)
        self.button.move(100,50)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        coronacountrequest = requests.get('https://corona.lmao.ninja/countries/'+textboxValue)
        coronacount = coronacountrequest.json()
        QMessageBox.about(self, textboxValue + ' Cases', 'Overall:'+'\n'+"Confirmed Cases: " + str(coronacount['cases'])+'\n'+'Confirmed Deaths: '+ str(coronacount['deaths'])+'\n'+'\n'+'Todays results:'+'\n'+'Confirmed Cases: '+str(coronacount['todayCases'])+'\n'+'Confirmed Deaths: '+str(coronacount['todayDeaths']))
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())