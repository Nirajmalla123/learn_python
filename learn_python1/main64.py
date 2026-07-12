# ALARAM CLOCK using Python

import time
import datetime
import pygame


def set_alaram(alaram_time):     # function to set alaram
   print("Alaram is set")
   sount_source = "music.mp3"
   toexitfrominnerloop=True
   while toexitfrominnerloop:
      current_time=datetime.datetime.now().strftime("%H:%M:%S")
      print(current_time)
      time.sleep(1) 
      if current_time==alaram_time:
          print("wake up !")
          pygame.mixer.init()
          pygame.mixer.music.load(sount_source)
          pygame.mixer.music.play()
          
          while pygame.mixer.music.get_busy():
             time.sleep(1)
             toexitfrominnerloop=False
          
            

if __name__=="__main__":
   alaram_time=input("Enter the alaram time (HH:MM:SS):")
   set_alaram(alaram_time)