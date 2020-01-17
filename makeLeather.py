from pyclick import HumanClicker
import pyautogui
import random
import time
import decimal

# initialize HumanClicker object
hc = HumanClicker()
iterations = 600 # how many times the script should loop and cast make leather

# initialize function to generate random time dleay

for i in range(iterations):
    # establish random coordinates to avoid bot detection
    pos = random.randrange(-50,50,1)
    dhidehor = random.randrange(-30,30,1)
    dhidever = random.randrange(-25,30,1)
    spellhor = random.randrange(-23,23,1)
    spellver = random.randrange(-23,23,1)
    deposithor = random.randrange(-40,40,1)
    depositver = random.randrange(-30,30,1)

    # establish random times to avoid bot detection
    spellTime = random.randrange(0,1,1)
    bankTime = random.randrange(0,1,1)
    allOtherTime = random.randrange(0,2,1)
   # movementTime = 

    # banking
    hc.move((929+pos,459+pos),3+spellTime)
    hc.click()
    hc.move((1113+deposithor,659+depositver),1+bankTime)
    hc.click()
   
    # withdraw 25 black dragonhide
    hc.move((827+dhidehor,377+dhidever),1+allOtherTime)
    hc.click()
    time.sleep(float(random.randrange(52, 120))/100)
    pyautogui.press('esc')

    # casting the spell
    hc.move((1512+spellhor,682+spellver),1+allOtherTime)
    hc.click()
    for i in range(10):
        time.sleep(float(random.randrange(52, 120))/100)
        hc.click()
    time.sleep(float(random.randrange(52, 120))/100)
    
