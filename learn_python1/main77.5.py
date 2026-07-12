# Stopwatch program using python PyQt5           ( tooo add functionality to the button we have to do some work on method start,stop,reset,update and format_time)

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)   # create a time object format (h,m,s,milisecond)
        self.time_label = QLabel("00:00:00:00",self)  # we will add this to self(stopwatch) so pass self and the other one is the text we will use in update display.
        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("stop",self)
        self.reset_button= QPushButton("Reset",self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):           # here we need 6 method to designing ui,to start stopwatch, to stop,to reset,to format_time and update.
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
        
      # for each of our button we have to connect a signal to a slot

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
    
    def start(self):
        self.timer.start(10)     # we will set and interval for a timeout  every 10 millisecond.


    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()                  # stop the time 
        self.time = QTime(0,0,0,0)        # reset to 0
        self.time_label.setText(self.format_time(self.time))       # and resetting to text on the time label

    def format_time(self,time):       # to return or display houre:minuts:second:millisecond,
        hours=time.hour()
        minuts=time.minute()
        second=time.second()
        milliseconds = time.msec()//10  # this will convert a 3digit millisecond to 2digit millisecond by dividing with 10
        return f"{hours:02}:{minuts:02}:{second:02}:{milliseconds:02}"   # 02 meanning adding two zeros "00" here we are using formatspecifier

    def update_display(self):
        self.time=self.time.addMSecs(10)                # we are updating the time with +10 milliseconds 10ms=1sec so.
        self.time_label.setText(self.format_time(self.time))  # hamley update vae ra ko time(self.time) eauta format ma pass garim and tyo format lai label ko text ma set garim so that we can see on the screen.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch() # creating the object name "stopwatch"
    stopwatch.show()
    sys.exit(app.exec_())