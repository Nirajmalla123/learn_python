# Stopwatch program using python PyQt5

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt



class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)   # create a time object format (h,m,s,milisecond)
        self.time_label = QLabel("00:00:00:00",self)  # we will add this to self(stopwatch) so pass self.
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("stop",self)
        self.reset_button= QPushButton("Reset",self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):           # here we need 6 method to designing ui,to start stopwatch, to reset,to format_time and update.
        self.setWindowTitle("StopWatch")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)   # it will center align the time

        hbox =  QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)


        vbox.addLayout(hbox)   # In vbox we add hbox layout , so that only the buttons are arrange in horizontal

        self.setStyleSheet("""
                           QPushButton,QLabel{
                           padding:20px;
                           font-weight:bold;
                           font-family:calibri;}

                           QPushButton{
                           font-size:30px;
                            }

                           QLabel{
                           font-size:100px;
                           background-color:hsl(232, 73%, 74%);
                           border-radius:20px;
                           }
                           """)
        
     
    
    def start(self):
        pass

    def reset(self):
        pass

    def format_time(self,time):
        pass

    def update_display(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch() # creating the object name "stopwatch"
    stopwatch.show()
    sys.exit(app.exec_())