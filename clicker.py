import pyautogui as ag
from time import sleep

ag.click(339,294)

def movingUpdate(positions):
    for x,y in positions.items():
        ag.moveTo(x,y,1,ag.easeInQuad)
        ag.click()
        sleep(1)

while True:
    movingUpdate({
        339:294,
        674:324,
        817:469,
    })
    sleep(15)

    ag.moveTo(28,245,2,ag.easeInQuad)
    ag.click()
    sleep(1)