from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class kordinatlar():
    replayBtn = (959, 359)
    dinazor = (243, 375)
    
def pressSpace():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')

def restartGame():
    pyautogui.click(kordinatlar.replayBtn)

def imageGrab():
    box = (195,372,234,403)                                  
    image = ImageGrab.grab(box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    return arr.sum()
      
def main():
    
    print("Starting Game...")                
    while True:
        if(imageGrab() != 1456):
           pressSpace()
        

main()