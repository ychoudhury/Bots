from pyclick import HumanClicker
import pyautogui
import random
import time
import decimal

# initialize HumanClicker object
hc = HumanClicker()
iterations = 20 # how many times the script should loop

def withdrawCoal():
    checkStamina()
    hc.move(((random.randrange(842,868,1)),(random.randrange(343,367,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    time.sleep(float(random.randrange(52, 100))/100) # sleep enough to allow ore to withdraw
    pyautogui.press('esc')
    hc.move(((random.randrange(1722,1743,1)),(random.randrange(752, 775,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    hc.move(((random.randrange(951,970,1)),(random.randrange(555,571,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    hc.move(((random.randrange(842,868,1)),(random.randrange(343,367,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    time.sleep(float(random.randrange(52, 100))/100) # sleep enough to allow ore to withdraw
    pyautogui.press('esc')

def withdrawAdamantite():
    hc.move(((random.randrange(1178,1204,1)),(random.randrange(915,958,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    time.sleep(5)
    hc.move(((random.randrange(842,868,1)),(random.randrange(343,367,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    time.sleep(float(random.randrange(52, 100))/100) # sleep enough to allow ore to withdraw
    pyautogui.press('esc')
    hc.move(((random.randrange(1722,1743,1)),(random.randrange(752, 775,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    hc.move(((random.randrange(951,970,1)),(random.randrange(555,571,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    hc.move(((random.randrange(890,914,1)),(random.randrange(345,369,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    time.sleep(float(random.randrange(52, 100))/100) # sleep enough to allow ore to withdraw
    pyautogui.press('esc')

def depositOre():
    hc.move(((random.randrange(810,825,1)),(random.randrange(239,274,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    time.sleep(6)
    pyautogui.keyDown('shift')
    hc.move(((random.randrange(1722,1743,1)),(random.randrange(752, 775,1))), (float(random.randrange(50, 100))/400))
    time.sleep(1)
    hc.click()
    time.sleep(1)
    pyautogui.keyUp('shift')
    hc.move(((random.randrange(982,1004,1)),(random.randrange(509,548,1))), (float(random.randrange(50, 100))/400))
    hc.click()

def withdrawBars():
    hc.move(((random.randrange(879,914,1)),(random.randrange(649,675,1))), (float(random.randrange(50, 100))/400))
    time.sleep(2)
    hc.click()
    time.sleep(4)
    pyautogui.press('space')
    hc.move(((random.randrange(1271,1297,1)),(random.randrange(820,833,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    time.sleep(5)

def checkStamina():
    if(pyautogui.pixelMatchesColor(1752, 145, (19, 19, 19))) == True:
        drinkStamina()

def drinkStamina():
    oneHor = random.randrange(798, 818,1)
    oneVer = random.randrange(823, 836,1)

    allHor = random.randrange(899, 914,1)
    allVer = random.randrange(825, 838,1)

    hc.move((oneHor,oneVer), (float(random.randrange(50, 100))/400))
    hc.click()
    hc.move((random.randrange(936, 959,1),(random.randrange(343, 369,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    hc.move((allHor,allVer), (float(random.randrange(50, 100))/400))
    hc.click()
    time.sleep((float(random.randrange(50, 100))/400))
    pyautogui.press('esc')
    hc.move(((random.randrange(1765, 1783,1)),(random.randrange(750, 776,1))), (float(random.randrange(50, 100))/400))
    hc.click()
    hc.move(((random.randrange(951,970,1)),(random.randrange(555,571,1))), (float(random.randrange(50, 100))/400))
    hc.click()

hc.move(((random.randrange(951,970,1)),(random.randrange(555,571,1))), (float(random.randrange(50, 100))/400)) # initialize bank chest open
hc.click()
    
for i in range(iterations):
    
    # main sequence
    withdrawCoal()
    depositOre()
    withdrawAdamantite()
    depositOre()
    withdrawBars()
    hc.move(((random.randrange(1769,1787,1)),(random.randrange(750,765,1))), (float(random.randrange(50, 100))/400))
    hc.click()


#     establish random coordinates to avoid bot detection
#     startHor = random.randrange(951,970,1) # starting bank chest coordinates
#     startVer = random.randrange(555,571,1)
#
#     coalHor = random.randrange(842,868,1)
#     coalVer = random.randrange(343,367,1)
#
#     adamantiteHor = random.randrange(890,914,1)
#     adamantiteVer = random.randrange(345,369,1)
#
#     coalbagHor = random.randrange(1722,1743,1)
#     coalbagVer = random.randrange(752, 775,1)
#
#     boxHor = random.randrange(810,825,1)
#     boxVer = random.randrange(239,274,1)
#
#     rampTopHor = random.randrange(982,1004,1)
#     rampTopVer = random.randrange(509,548,1)
#
#     bankHor = random.randrange(1178,1204,1)
#     bankVer = random.randrange(915,958,1)
#
#     dispenserHor = random.randrange(879,914,1)
#     dispenserVer = random.randrange(649,675,1)
#
#     depositBarsHor = random.randrange(1271,1297,1)
#     depositBarsVer = random.randrange(820,833,1)
#
#     inventoryBarHor = random.randrange(1769,1787,1)
#     inventoryBarVer = random.randrange(750,765,1)
#
#     bankStaminaHor = random.randrange(936, 959,1) # stamina potion bank item
#     bankStaminaVer = random.randrange(343, 369,1)
#
#     drinkStaminaHor = random.randrange(1765, 1783,1)
#     drinkStaminaVer = random.randrange(750, 776,1)
#
#     oneHor = random.randrange(798, 818,1)
#     oneVer = random.randrange(823, 836,1)
#
#     allHor = random.randrange(899, 914,1)
#     allVer = random.randrange(825, 838,1)