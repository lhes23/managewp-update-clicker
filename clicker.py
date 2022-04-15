import pyautogui as ag
from time import sleep

ag.moveTo(339,294,2,ag.easeInQuad)
ag.click()

def movingUpdate(positions):
    for x,y in positions.items():
        ag.moveTo(x,y,3,ag.easeInQuad)
        ag.click()
        sleep(3)
    sleep(45)

    ag.moveTo(28,245,2,ag.easeInQuad)
    ag.click()
    sleep(3)

while True:
    movingUpdate({
        339:294,
        674:324,
        817:469,
    })