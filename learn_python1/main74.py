# LineEdit widget / text boxes  in PyQt5

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QPushButton


class mainwindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.line_edit=QLineEdit(self)
        self.button=QPushButton("submit",self)
        self.initUI()
    
    def initUI(self):
        self.line_edit.setGeometry(10,10,200,40)
        self.button.setGeometry(210,10,100,40)
        self.line_edit.setStyleSheet("font-size:25px;"
                                     "font-family:Arial")
        

        self.line_edit.setPlaceholderText("enter your name")     # to  add the placeholder text in the textbox/lineEdit i.e. partially visible text written in the empty text box. 
        self.button.clicked.connect(self.submit)     # show when we click the button we call the methos name "submit"  


    def submit(self):
        text= self.line_edit.text()   # text methos to get the text from the line edit or text box
        print(f"Hello {text}")

if __name__ =="__main__":
    app=QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec_())