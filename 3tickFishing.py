from pyclick import HumanClicker
import pyautogui
import random
import time
import decimal

# initialize HumanClicker object
hc = HumanClicker()
iterations = 100 # how many times the script should loop and cast make leather
pos = random.randrange(-20,20,1)

for i in range(iterations):

    hc.move((1454+random.randrange(-20,20,1),487+random.randrange(-20,20,1)), 0.6)
    hc.click()
    hc.move((1454+random.randrange(-20,20,1),562+random.randrange(-20,20,1)), 0.6)
    hc.click()
    
    hc.move((954+random.randrange(-20,20,1),482+random.randrange(-20,20,1)), 0.4)
    hc.click()

    pyautogui.keyDown('shift')
    time.sleep(.6)
    hc.move((1454+random.randrange(-20,20,1),637+random.randrange(-20,20,1)), 0.6)
    hc.click()
    hc.move((1454+random.randrange(-20,20,1),712+random.randrange(-20,20,1)), 0.6)
    hc.click()
    time.sleep(.5)
    pyautogui.keyUp('shift')
    time.sleep(.5)

