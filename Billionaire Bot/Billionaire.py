from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

def printMousePos(): #974 564
    while True:
        time.sleep(1)
        print(pyautogui.position())

def pressMouseDown():
    pyautogui.mouseDown()

def imageGrab(): #Ekran çözünürlüklerine göre burası değişebilir.Kendi ekranınıza göre ayarlayınız yoksa hatayla karşılaşabilirsiniz.
    box = (974,564,1067,739)
    image = ImageGrab.grab(box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    return arr.sum()

def main():
   while True:
       
       if(imageGrab() == 33216):
           pressMouseDown()        


main()
