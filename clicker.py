import pyautogui as ag
from time import sleep

initial_x = 385
initial_y = 347

def movingUpdate(positions):
    for x,y in positions.items():
        ag.moveTo(x,y,3,ag.easeInQuad)
        ag.click()
        sleep(3)
    sleep(45)

    ag.moveTo(20,243,2,ag.easeInQuad)
    ag.click()
    sleep(3)

ag.moveTo(initial_x,initial_y,2,ag.easeInQuad)
ag.click()

while True:
    movingUpdate({
        initial_x:initial_y,
        986:377,
        802:445 ,
    })