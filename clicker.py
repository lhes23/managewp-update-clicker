import pyautogui as pg
from time import sleep
import keyboard

pg.click(339,294)

def movingUpdate(positions):
    for x,y in positions.items():
        pg.moveTo(x,y,1,pg.easeInQuad)
        pg.click()
        sleep(1)

while True:
    if keyboard.is_pressed('esc'):
        break
    movingUpdate({
        339:294,
        674:324,
        817:469,
    })
    sleep(30)

    pg.moveTo(28,245,2,pg.easeInQuad)
    pg.click()
    sleep(1)