# PyQt5  GUI 
                    # this is boilarplate code to display window having title
import sys              # provide access to variable used and maintained by the python interperator
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):    # here we can customize window to display to the user
    def __init__ (self):
        super().__init__()        # in case we have to pass any argument to the parent (QMainwindow)
        
        self.setWindowTitle("my first gui")
        self.setGeometry(1500,600,300,300)
        self.setWindowIcon(QIcon("njr.png"))

def main():
    app = QApplication(sys.argv)    # by passing this argument this allow pyqt5 to process any command line argument intended for it.like commmand prompt , terminal
    window = MainWindow()           # befault behaviour for the  window is to hide it 
    window.show()                   # window pop for milisecond so access sys module
    sys.exit(app.exec_())           # exit method ensure clean exit of our program , and exec_() method wait around for user input and haldles events.such as click button,press keys,or close window.
    
    
if __name__ == "__main__":
    main() 
