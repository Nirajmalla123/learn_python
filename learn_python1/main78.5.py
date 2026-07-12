# Weather  api app using python  (for the functionality of the  or method)

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
        self.temperature_label=QLabel(self)      # for degree sign press alt 0176  and numluck should be on
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("WeatherApp")
        
        vbox=QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)


        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)


# we will apply css based on an object name so we have to set that object name.
        self.city_label.setObjectName("city_lab")
        self.city_input.setObjectName("city_inp")
        self.get_weather_button.setObjectName("weather_button")
        self.temperature_label.setObjectName("temperature")
        self.emoji_label.setObjectName("emoji")
        self.description_label.setObjectName("discription")

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
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "fe0dc858cfc8cc0553eca163c5100646"   # these are local variable
        city=self.city_input.text()
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response=requests.get(url) # when we make an api request, we will be returned with a response object / with our response object we have to convert it to json format.
            response.raise_for_status() # this method raise and exception, if we are going to handeled any httperror, we have to raise an exception.
            data = response.json()     # converting to a json format
          # print(data) look for  http status code 200 so successful and 404 is error or not foun city
            if data["cod"]==200:
                self.display_weatherdata(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request\nplease check your input")
                case 401:
                    self.display_error("Unauthorized\ninvalid API key")
                case 403:
                    self.display_error("Forbidden\naccess is denied")
                case 404:
                    self.display_error("Not found\nCity not found")
                case 500:
                    self.display_error("Internal server Error\nplease try again later")
                case 502:
                    self.display_error("Bad Gateway\ninvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable\nserver is down")
                case 504:
                     self.display_error("Geteway Timeout\nNo response from the server")
                case _ :
                    self.display_error(f"HTTP error occured\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error")
        except requests.exceptions.TooManyRedirects:
            self.display_error("too many redirects:\nCheck th url")
                
        except requests.exceptions.RequestException as req_error:  #this can be due to network issue, invalid url 
            self.display_error(f"Request Error:\n{req_error}")

   
    def display_error(self,msg):
        self.temperature_label.setStyleSheet("font-size:25px;")
        self.temperature_label.setText(msg)
        self.emoji_label.clear()        # we should clear our emoji and discription  when we get error message.
        self.description_label.clear()

    def display_weatherdata(self,data):
     self.temperature_label.setStyleSheet("font-size:75px;")
     temperature_k = data["main"]["temp"]
     temperature_c = temperature_k - 273.15
     temperature_f = (temperature_k * 9/5) -459.67


     weather_id = data["weather"][0]['id']      # not clearly understand topic
     weather_description = data["weather"][0]['description']     
     
     self.temperature_label.setText(f"{temperature_c:.0f}°C")                   # displaying temperature
     self.emoji_label.setText(self.get_weather_emoji(weather_id))
     self.description_label.setText(weather_description)                        # Displaying weather condition

     # not much understand topic 👇. decorator of static method
    @staticmethod #they belong to a class but don't require any instance specific data or any methods.
    def get_weather_emoji(weather_id): # this method isn't going to rely on any class data or instance data but we could make it static method.
        if 200 <= weather_id <=232:
            return"🌩️"
        elif 300<= weather_id <=321:
            return"⛅"
        elif 500<=weather_id<=531:
            return"🌧️"
        elif 600<=weather_id<=622:
            return"❄️"
        elif 701<=weather_id<=741:
            return"🌫️"
        elif weather_id==762:
            return"🌋"
        elif weather_id ==771:
            return "💨"
        elif weather_id==781:
            return "🌪️"
        elif weather_id==800:
            return "☀️"
        elif 801<=weather_id<=804:
            return "☁️"
        else:
            return""
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather=weatherapp()
    weather.show()
    sys.exit(app.exec_())
 