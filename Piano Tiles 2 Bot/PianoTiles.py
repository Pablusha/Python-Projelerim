#Game Link:http://www.4j.com/Piano-Tiles-2-Online
import pyautogui
from mss import mss
import time
#135 Interval Tiles
#505 Height

x_start = 185
y_start = 542

box = (x_start,y_start,x_start + 438,y_start + 1)

x_coordinates = [0,135,271,406] #135 = The x coordinate of the first block - The x of the second block 
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
            for coordinate in x_coordinates:
                if(img.pixel(coordinate,0)[0] < 120): #120 comes from rgb(Red,Green,Blue)
                    print("Tile Detected")
                    pyautogui.click(x_start+coordinate,y_start)
                    break

time.sleep(3)
startClicking()
