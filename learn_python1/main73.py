#PyQt5 radiobutton              ( with radiobutton we can select only once at a time from the radiogroup, but when it is seperated by with group it can)

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QRadioButton,QButtonGroup


class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,500,500)
        self.radio1=QRadioButton("visa",self)
        self.radio2=QRadioButton("master card",self)
        self.radio3=QRadioButton("gift card",self)
        self.radio4=QRadioButton("in-store",self)
        self.radio5=QRadioButton("in-petrolpump",self)
        self.button_group1=QButtonGroup(self)
        self.button_group2=QButtonGroup(self)

        self.initUI()


    def initUI(self):
        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0,50,300,50)
        self.radio3.setGeometry(0,100,300,50)
        self.radio4.setGeometry(0,150,300,50) 
        self.radio5.setGeometry(0,200,300,50)

        self.setStyleSheet("QRadioButton{"                # we can apply multiple css like properties to an entire group of widget here,
                             "font-size:30px;"
                             "font-family:Arial;"
                             "padding:10px;"
                             "}")   

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_change)       # to do some action when the radio button is selected with the helep  of function name "radio button change"
        self.radio2.toggled.connect(self.radio_button_change)       
        self.radio3.toggled.connect(self.radio_button_change)       # when the radio button is toggle we pass the function/method.
        self.radio4.toggled.connect(self.radio_button_change)
        self.radio5.toggled.connect(self.radio_button_change)



    def radio_button_change(self):
        radio_signal =self.sender()        # sender method find the radiobutton who  the sent the signal
        if radio_signal.isChecked():
            print(f"{radio_signal.text()} is selected!")  # .text() to return the text of the radio_signal which one  is the sender radio 1,2,3,4 or radio5.
def main():
   app = QApplication(sys.argv)
   window=mainwindow()
   window.show()
   sys.exit(app.exec_())
 

if __name__== "__main__":
    main()

