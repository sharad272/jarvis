import pyautogui
from PIL import Image,ImageGrab
import time

def collision(data):
    for i in range(170,290):
        for j in range(460,490):
            if data[i,j]<100 and data[i,j]>35:
               pyautogui.keyDown('up')
               time.sleep(0.14)
               pyautogui.keyDown('down')
               time.sleep(0.05)
               pyautogui.keyUp('down')
               return True   
            if data[i,j]>100 and data[i,j]<225:
                pyautogui.keyDown('up')
                return True
    for i in range(175,260):
       for j in range(300,440):
            if data[i,j]<90 and data[i,j]>35:
               pyautogui.keyDown('down')
               time.sleep(0.15)
               pyautogui.keyUp('down')
               return True
            if data[i,j]>100 and data[i,j]<200:
                pyautogui.keyDown('down')
                time.sleep(0.25)
                pyautogui.keyUp('down')
                return True
                 
    return False    
time.sleep(2)    
while True:  
   image=ImageGrab.grab().convert("L")
   data=image.load()  
   collision(data)
    
    
  

  

               

                       
    
       