# Weather  api app using python

import sys
import requests
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,QPushButton,QVBoxLayout

from PyQt5.QtCore import Qt

class weatherapp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label= QLabel("enter city name:",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather",self)
        self.temperature_label=QLabel("70°F",self)      # for degree sign press alt 0176  and numluck should be on
        self.emoji_label = QLabel("☀️",self)
        self.discription_label = QLabel("sunny",self)

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("WeatherApp")
        
        vbox=QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.discription_label)

        self.setLayout(vbox)


        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.discription_label.setAlignment(Qt.AlignCenter)


# we will apply css based on an object name so we have to set that object name.
        self.city_label.setObjectName("city_lab")
        self.city_input.setObjectName("city_inp")
        self.get_weather_button.setObjectName("weather_button")
        self.temperature_label.setObjectName("temperature")
        self.emoji_label.setObjectName("emoji")
        self.discription_label.setObjectName("discription")

        self.setStyleSheet("""
                QLabel,QPushButton{
                           font-family:calibri;}
                    
                QLabel#city_lab{
                           font-size:40px;
                           font-style:italic;}
                    
                QLineEdit#city_inp{
                           font-size:40px;}
                QPushButton#weather_button{
                           font-size:30px;
                           font-weight:bold;}
                QLabel#temperature{
                           font-size:75px;}
                QLabel#emoji{
                           font-size:100px;
                           font-family:Segoe UI emoji;}
                QLabel#discription{
                           font-size:50px;}


                  """)
    # we have to connect to a signal to a slot
    def get_weather(self):
        pass
   
    def display_error(self,message):
        pass

    def display_weatherdata(self,data):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather=weatherapp()
    weather.show()
    sys.exit(app.exec_())
