# Digital Clock using PyQt5 in python

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)  # this will be the label that display time
        self.timer = QTimer(self)      # we are adding the timer to the clock 
        self.initUI()

        

    def initUI(self):            # with in this method that we will be desiginig the layout of the digital clock 
        self.setWindowTitle("Digital Clock")   # setting the title for the window
        self.setGeometry(600,400,300,100)

        vbox = QVBoxLayout() # this will arrange all  of  our widget vertically 
        vbox.addWidget(self.time_label) # we are adding our label  to our layout manager "vbox"
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:140px;"
                                      "font-family:Arial;"
                                      "color:green;")
        self.setStyleSheet("background-color: black;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()


    def update_time(self):
            current_time = QTime.currentTime().toString("hh:mm:ss AP")
            self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())     # for the proper exit ( until we exit , the window will show )