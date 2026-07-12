# how we can create push button in pyqt5


import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QLabel, QPushButton



class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.button=QPushButton("cilck me!",self)         # normally when creating widget we have to prefix that widget with "self" and follow the name of  the widget. use self show that we can use it in method.
        self.label=QLabel("hello",self)
        self.initUI()

    def initUI(self):        # within this methos we are handaling managing user interface(UI). 
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size:30px;")
        self.button.clicked.connect(self.on_click)        # when we press this button we perform the slot ie.(self.on_click)

        self.label.setGeometry(195,300,300,100)
        self.label.setStyleSheet("font-size:50px;")

    def on_click(self):
        # print("Button clicked!")
        # self.button.setText("clicked")              # this change the button text when it is press. in mainwindow.
        # self.button.setDisabled(True)
        
        self.label.setText("good bye!")
def main():
    app=QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec_())



if __name__ =="__main__":
    main()
