from pyclick import HumanClicker
import pyautogui
import random

# initialize HumanClicker object
hc = HumanClicker()
iterations = 600 # how many times the script should loop and produce molten glass


for i in range(iterations):
    # establish random coordinates to avoid bot detection
    pos = random.randrange(-10,10,1)
    seaweedhor = random.randrange(-37,37,1)
    seaweedver = random.randrange(-26,26,1)
    deposithor = random.randrange(-44,44,1)
    depositver = random.randrange(-36,36,1)

    # establish random times to avoid bot detection
    spelltime = random.randrange(0,2,1)
    banktime = random.randrange(0,1,1)
    allothertime = random.randrange(0,2,1)

    # banking
    hc.move((929+pos,459+pos),3+spelltime)
    hc.click()
    hc.move((1115+deposithor,659+depositver),1+banktime)
    hc.click()
   
    # withdraw 18 buckets of sand
    hc.move((219+pos,222+pos),1+allothertime)
    pyautogui.click(button='right')
    hc.move((203+pos,366+pos),1+allothertime)
    hc.click()
    
    # withdraw 3 seaweed
    hc.move((344+seaweedhor,220+seaweedver),1+allothertime)
    pyautogui.click()
    pyautogui.sleep(1+allothertime)
    pyautogui.click()
    pyautogui.sleep(1+allothertime)
    pyautogui.click()
    pyautogui.sleep(1+allothertime)
    pyautogui.press('esc')

    # casting the spell
    hc.move((1411+pos,680+pos),1+allothertime)
    hc.click()
