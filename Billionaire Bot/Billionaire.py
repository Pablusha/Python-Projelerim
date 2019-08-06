#Where can you get the game?
#You can get game in the AppStore or GooglePlayStore.
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

def imageGrab(): #Create the box according to your own screen resolutions, otherwise you may encounter an error.
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
