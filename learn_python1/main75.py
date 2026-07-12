# setstylesheet() in PyQt5

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QWidget,QHBoxLayout


class mainwindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.button1=QPushButton("#1")
        self.button2=QPushButton("#2")
        self.button3=QPushButton("#3")
        self.initUI()
            
    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        hbox =QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)


        central_widget.setLayout(hbox)

        # to apply css property to a one widget(seperate button)
        # we will apply css based on an object name so we have to set that object name.

        self.button1.setObjectName("1button")
        self.button2.setObjectName("2button")
        self.button3.setObjectName("3button")
 

    # now applying css
        self.setStyleSheet("""
            QPushButton{
                           font-size:40px;
                           font-family:Arial;
                           padding:15px 75px;
                           margin:25px;
                           border:3px solid;
                           border-radius: 15px;
                           }

                
                           QPushButton#1button{       
                           background-color:hsl(12, 82%, 49%);
                           }
                           QPushButton#2button{       
                           background-color:hsl(204, 71%, 66%);
                           }
                           QPushButton#3button{       
                           background-color:hsl(136, 91%, 66%);
                           }

                
                           QPushButton#1button:hover{       
                           background-color:hsl(12, 82%, 69%);
                           }
                           QPushButton#2button:hover{       
                           background-color:hsl(204, 71%, 86%);
                           }
                           QPushButton#3button:hover{       
                           background-color:hsl(136, 91%, 86%);
                           }



                           """)


if __name__ == "__main__":
   app = QApplication(sys.argv)
   window= mainwindow()
   window.show() 
   sys.exit(app. exec_())

