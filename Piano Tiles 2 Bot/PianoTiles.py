#Game Link:http://www.4j.com/Piano-Tiles-2-Online
import pyautogui
from mss import mss
import time
#135 Interval Tiles
#505 Height

x_baslangic = 185
y_baslangic = 542

box = (x_baslangic,y_baslangic,x_baslangic + 438,y_baslangic + 1)

x_kordinatlar = [0,135,271,406] #135 = The x coordinate of the first block - The x of the second block 
                                #271 = Interval + Interval + 1(that means 135+136)
                                #406 = 271 + Interval

def printMousePos():
    while True:
        print(pyautogui.position()) #We use this line of code to find coordinates

def ScreenShotTime():
    with mss() as sct:
        t1 = time.time()
        for i in range(100):
            img = sct.grab(box)
        t2 = time.time()
        print(t1 - t2)

def startClicking():
    with mss() as sct:
        while True:
            img = sct.grab(box)
            for kordinat in x_kordinatlar:
                if(img.pixel(kordinat,0)[0] < 120): #120 comes from rgb(Red,Green,Blue)
                    print("Tile Detected")
                    pyautogui.click(x_baslangic+kordinat,y_baslangic)
                    break

time.sleep(3)
startClicking()
