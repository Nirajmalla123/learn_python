# PyQt5  QLables
                   
import sys            
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt          # Qt is use for allignment


class MainWindow(QMainWindow):    
    def __init__ (self):
        super().__init__()        
        self.setWindowTitle("my first gui")
        self.setGeometry(1500,600,300,300)
        self.setWindowIcon(QIcon("njr.png"))
        label = QLabel("content",self)
        label.setFont(QFont("arial",20))
        label.setGeometry(0,0,300,100)
        label.setStyleSheet("color:#87eb75;"
                            "background-color:#838fd6;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration:underline;")        # use color picker from google you can use rgb or hex value
        # label.setAlignment(Qt.AlignTop)    # verticaly top similarly, use bottom,Vcenter and for horizontal use AlignHcenter,Alignleft,AlignRight
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  #  for using both vertically and horizontally
        label.setAlignment(Qt.AlignCenter)   # shortcut vertical and horizontal center

def main():
    app = QApplication(sys.argv)   
    window = MainWindow()           
    window.show()                  
    sys.exit(app.exec_())         
    
    
if __name__ == "__main__":
    main() 
