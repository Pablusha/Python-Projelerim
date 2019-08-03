#Game Link:http://www.4j.com/Piano-Tiles-2-Online
import pyautogui
from mss import mss
import time
#135 Interval Tiles
#505 Height

x_baslangic = 185
y_baslangic = 542

box = (x_baslangic,y_baslangic,x_baslangic + 438,y_baslangic + 1)

x_kordinatlar = [0,135,271,406] #135 = İkinci bloğun xiyle birinci bloğun x kordinatı çıkar. 
                                #271 = İntervalle bir fazlasının toplamı
                                #406 = 271'un intervalle toplamı

def printMousePos():
    while True:
        print(pyautogui.position()) #Kordinatları almak için kullandığım komut.

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
                if(img.pixel(kordinat,0)[0] < 120): #120'nin altı siyah olduğu için 120 yazıyor.RGB'den geliyor.
                    print("Tile Detected")
                    pyautogui.click(x_baslangic+kordinat,y_baslangic)
                    break

time.sleep(3)
startClicking()
