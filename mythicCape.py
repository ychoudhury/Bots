# This program is intended to create a myth cape mount, remove it, and repeat
# 8 times before calling the butler to fetch more planks.

from pyclick import HumanClicker
import pyautogui
import time
import pyperclip
import random
import decimal

# initialize HumanClicker object
hc = HumanClicker()
iterations = 93 # how many times the script should loop and make 8 cape mounts
for i in range(iterations):
        for i in range(8):
                xpos = random.randrange(-50,20,1)
                ypos = random.randrange(-3,3,1) # two ypos values so avoid one discrete value applied to all
                ypos2 = random.randrange(-3,3,1) 
                xSettings = random.randrange(-10,5,1) # x and y settings to simulate randomness and avoid detection
                ySettings = random.randrange(-2,2,1)

                hc.move((1000+xpos, 290+ypos),1)
                pyautogui.click(button='right')
                pyautogui.moveTo(1000+xpos, 340+ypos, duration = 0.5)
                hc.click()
                time.sleep(1)
                for i in range(3): # random press interval to evade bot detection
                        pyautogui.press('4')
                        time.sleep(float(random.randrange(52, 120))/100)
                time.sleep(1)
                hc.move((976+xpos, 290+ypos2),1)
                pyautogui.click(button='right')
                pyautogui.moveTo(976+xpos, 365+ypos2, duration=0.5)
                hc.click()
                time.sleep(1)
                for i in range(3):
                        pyautogui.press('1')
                        time.sleep(float(random.randrange(52, 120))/100)
        hc.move((1831+xSettings, 1016+ySettings, 1))
        hc.click()
        hc.move((1823+xSettings, 975+random.randrange(0,3,1), 1))
        hc.click()
        time.sleep(2)
        hc.click()
        time.sleep(2)
        pyautogui.press('1')
        time.sleep(float(random.randrange(52, 120))/100)
        pyautogui.press('1')
        time.sleep(7+random.randrange(0,2,1))




