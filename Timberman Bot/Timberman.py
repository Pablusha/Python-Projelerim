#Game Link:https://games.cdn.famobi.com/html5games/t/timber-man/v030/?fg_domain=play.famobi.com&fg_aid=A1000-1&fg_uid=a25e37b9-1550-49c9-b383-92ad51b4ecc2&fg_pid=4638e320-4444-4514-81c4-d80a8c662371&fg_beat=896&original_ref=https%3A%2F%2Fwww.google.com%2F
from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class kordinatlar():
    replaybtn = (472,774)
    
def restartGame():
    pyautogui.click(kordinatlar.replaybtn)

restartGame()

def pressLeft():
    pyautogui.press('left')

def pressRight():
    pyautogui.press('right')

def imageGrab(): #Kutuyu kendi ekran çözünürlüğünüze göre ayarlayınız aksi takdirda bir hata ile karşılaşabilirsiniz.
    box = (195,594,342,688)
    image = ImageGrab.grab(box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    return arr.sum()

def main():
    print("Game Starting...")
    while True:
        print(imageGrab())
        if(imageGrab() == 22062): #İmageGrab hesaplaması
            pressLeft()
        elif(imageGrab() == 34442):
            pressLeft()
        else:
            pressRight()
        
        

main()
