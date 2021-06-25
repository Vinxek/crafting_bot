from pyautogui import *
import os
import pyautogui
import time
import win32api, win32con
clear = lambda: os.system('cls')
n=0
con = 0
dir = (os.getcwd())
"""my_path = os.path.join(f"{dir}", "images")
os.chdir(rf'{my_path}')"""
counterHQ = 0
recipe = str("Nada")
recipes = ['', 'Grade 4 Tincture of intelligence', 'Smoked Chicken', 'Chili Crab', 'Grade 4 Tincture of mind']

def craftingMacroL(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def craftingMacroR(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def foodCheck():
    if pyautogui.locateOnScreen('buff.png', confidence=0.6) == None:
        if pyautogui.locateOnScreen('craftinglog.png', confidence = 0.6) != None:
            pyautogui.hotkey('ctrl','n')
            time.sleep(3)
        pyautogui.hotkey('alt', 'i') #abre el inventario
        time.sleep(0.5)
        locateclickR('craftingBuff.png') #selecciona la comida
        time.sleep(0.5)
        locateclickL('use.png') #usa la comida
        time.sleep(0.5)
        pyautogui.hotkey('alt', 'i')
        time.sleep(0.5)

def locateclickL(image):
    if pyautogui.locateOnScreen(image, confidence=0.8) != None:
        posB = pyautogui.locateOnScreen(image, confidence=0.8)
        pyautogui.moveTo(posB)
        posC = str(pyautogui.position())
        posA = re.findall(r'\d+', posC)
        posInt1 = map(int, posA)
        posInt2 = list(posInt1)
        craftingMacroL(posInt2[0], posInt2[1])
        time.sleep(0.7)

def locateclickLAjsutable(image,x,y):
    if pyautogui.locateOnScreen(image, confidence=0.8) != None:
        posB = pyautogui.locateOnScreen(image, confidence=0.8)
        pyautogui.moveTo(posB)
        posC = str(pyautogui.position())
        posA = re.findall(r'\d+', posC)
        posInt1 = map(int, posA)
        posInt2 = list(posInt1)
        craftingMacroL(posInt2[0] + x, posInt2[1] + y)
        time.sleep(0.7)

def locateclickR(image):
    if pyautogui.locateOnScreen(image, confidence=0.8) != None:
        posB = pyautogui.locateOnScreen(image, confidence=0.6)
        pyautogui.moveTo(posB)
        posC = str(pyautogui.position())
        posA = re.findall(r'\d+', posC)
        posInt1 = map(int, posA)
        posInt2 = list(posInt1)
        craftingMacroR(posInt2[0], posInt2[1])
        time.sleep(0.7)

def inputRecipe(recipe):
    if pyautogui.locateOnScreen('search.png', confidence=0.8) != None:
        posB = pyautogui.locateOnScreen('search.png', confidence=0.6)
        pyautogui.moveTo(posB)
        posC = str(pyautogui.position())
        posA = re.findall(r'\d+', posC)
        posInt1 = map(int, posA)
        posInt2 = list(posInt1)
        time.sleep(0.5)
        craftingMacroL(posInt2[0], posInt2[1])
        time.sleep(0.5)
        inputEnter(f"{recipe}")
        time.sleep(1)

def inputEnter(text):
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write(text)
    time.sleep(0.5)
    pyautogui.press('enter')

def openClose():
        inputEnter("")
        time.sleep(0.2)
        inputEnter("/clearlog")
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(4)
        pyautogui.press('esc')
        time.sleep(0.5)


print('\nChoose the recipe to craft using the list below')
print("")
for i in range(1,len(recipes)):
    print(f"{n+1}-{recipes[i]}")
    n+=1
    
while True:
    try:
        choose = input("\nEnter the number of the recipe to craft\n>")
        choose = int(choose)
        if choose == 1:
            recipe = recipes[1]
        elif choose ==2:
            recipe = recipes[2]
        elif choose == 3:
            recipe = recipes[3]
        elif choose == 4:
            recipe = recipes[4]
        number = input("\nEnter the number of time to craft, enter 0 to craft until mats are exausted\n:>")
        number = int(number)
        break
    except:
        print("\nOnly numbers are accepted")
        time.sleep(1)
clear()
print(f"\ncrafting {number} -{recipe}")

time.sleep(5)
inputEnter("/gs change 23") #add dictionaries and keys

while con < number:
        time.sleep(1)
        inputEnter("/clearlog") #limpia el log
        foodCheck()
        time.sleep(1)
        if pyautogui.locateOnScreen('synthezise.png', confidence=0.7) == None:
            pyautogui.hotkey('ctrl','n') #abre el craftinglog
            inputRecipe(recipe)
        if pyautogui.locateOnScreen("ingredient#3.png", confidence = 0.7) != None:   
            locateclickLAjsutable("ingredient#3.png",-20,0)
            time.sleep(0.5)  
            locateclickL('synthezise.png')
            time.sleep(1.2)
            if pyautogui.locateOnScreen("unabletocraft.png", confidence = 0.65) != None: 
                print("Not enough items for this recipe")
                print(f"Total Crafted {counterHQ} {recipe} HQ \n Total Crafted {counterNQ} {recipe} NQ\n Exiting the program now")
                exit()
            else:
                pyautogui.hotkey('ctrl','1')
                time.sleep(1)
                inputEnter("")
                while True:
                    time.sleep(1)
                    if pyautogui.locateOnScreen('macro1.png', confidence=0.8) != None:
                        break
                time.sleep(0.5)
                pyautogui.hotkey('ctrl','2')
                while True:
                    time.sleep(1)
                    if pyautogui.locateOnScreen('macro2.png', confidence=0.8) != None:
                        time.sleep(1)
                    else:
                        continue
                    time.sleep(1)
                    if pyautogui.locateOnScreen('HQ.png', confidence=0.68) != None:
                        counterHQ = counterHQ + 3
                    else:
                        counterNQ = counterNQ + 3
                    if number > 0:
                        con = con+1
                    break
clear()

print(f"Crafted {counterHQ} {recipe} HQ \n Total Crafted {counterNQ} {recipe} NQ\n Exiting the program now")
fin = print('Press any key to exit')
exit()




