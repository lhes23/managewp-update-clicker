import pyautogui as ag
from time import sleep

initial_x = 496
initial_y = 350

def movingUpdate(positions):
    for x,y in positions.items():
        ag.moveTo(x,y,3,ag.easeInQuad)
        ag.click()
        sleep(3)
    sleep(45)

    ag.moveTo(19,231,2,ag.easeInQuad)
    ag.click()
    sleep(3)

ag.moveTo(initial_x,initial_y,2,ag.easeInQuad)
ag.click()

while True:
    movingUpdate({
        initial_x:initial_y,
        683:372,
        871:476,
    })