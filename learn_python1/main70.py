# PyQt5 layouts



import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QWidget,
                   QVBoxLayout,QHBoxLayout,QGridLayout)
from PyQt5.QtGui import QPixmap


class MainWindow(QMainWindow):  
    def __init__ (self):
        super().__init__()
        self.iniUI()

    
    def iniUI(self):
        central_widgit=QWidget()
        self.setCentralWidget(central_widgit)
        

        label1=QLabel("#1",self)
        label2=QLabel("#2",self)
        label3=QLabel("#3",self)
        label4=QLabel("#4",self)
        label5=QLabel("#5",self)


        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: green;")
        label3.setStyleSheet("background-color: blue;")
        label4.setStyleSheet("background-color: pink;")
        label5.setStyleSheet("background-color: yellow;")

        # layout manager start with vlayout, creating vertical layout manager

        # vbox = QVBoxLayout()        # for vertical/horizontal layout
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)


        # central_widgit.setLayout(vbox)  # we are setting the layout of central widgit with the  layout manager (vbox).



        gbox = QGridLayout()        # for   grid layout  
        gbox.addWidget(label1,0,0)            # you have to pass (label,row,column)
        gbox.addWidget(label2,0,1)
        gbox.addWidget(label3,1,0)
        gbox.addWidget(label4,1,1)
        gbox.addWidget(label5,0,2)


        central_widgit.setLayout(gbox)



def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())



if __name__ =="__main__" :
    main()