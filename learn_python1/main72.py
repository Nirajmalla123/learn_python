# checkboxes in  PyQt5

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox
from PyQt5.QtCore import Qt         # Qtcore contai non gui classes


class mainwindow(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.checkbox=QCheckBox("first argument is text",self)  # 2nd argument is parent widget where we will be adding this checkbox
        self.initUI()

    def initUI(self):    # here we will initialize the user interface that is setting the  stylesheet and geometry
        self.checkbox.setGeometry(0,0,500,100)
        self.checkbox.setStyleSheet("font-size:30px;"
                                    "font-family:Arial;")
        
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)


        
    def checkbox_changed(self,state):
        if state==Qt.Checked:              # if state == 0 the it is unchacked and if state ==2 then it is checked 
            print("you checked it")
        else:
            print("you unchecked it")

def main():
    app=QApplication(sys.argv)
    window=mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
   main()