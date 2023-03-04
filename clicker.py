import pyautogui as ag
from time import sleep

# ag.moveTo(339,294,2,ag.easeInQuad)

def movingUpdate(positions):
    for x,y in positions.items():
        ag.moveTo(x,y,3,ag.easeInQuad)
        ag.click()
        sleep(3)
    sleep(45)

    ag.moveTo(19,231,2,ag.easeInQuad)
    ag.click()
    sleep(3)

initial_x = 404
initial_y = 333

ag.moveTo(initial_x,initial_y,2,ag.easeInQuad)
ag.click()

while True:
    movingUpdate({
        initial_x:initial_y,
        683:372,
        871:476,
    })