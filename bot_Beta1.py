from pyautogui import *
from datetime import datetime
import os
import pyautogui
import time
import crafting_functions as cf
import pandas as pd

now =datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
clear = lambda: os.system('cls')
n, tries, con = 0,0,0

dir = (os.getcwd())
my_path = os.path.join(f"{dir}","images")
os.chdir(rf"{my_path}")

column_names = ["Alchemist","Culinarian","Armorer","BlackSmith","Carpenter","GoldSmith","LeatherWorker","Weaver"]
df = pd.read_csv(rf'{dir}\CSV\recetas.csv', names=column_names)

counterHQ = 0
counterNQ = 0
recipe = str("Nada")
alquemistRecipes = df.Alchemist.to_list()
culinarianRecipes = df.Culinarian.to_list()
armorerRecipes = df.Armorer.to_list()
blacksmithRecipes = df.BlackSmith.to_list()
carpenterRecipes = df.Carpenter.to_list()
goldsmithRecipes = df.GoldSmith.to_list()
leatherworkerRecipes = df.LeatherWorker.to_list()
weaverRecipes = df.Weaver.to_list()

print('\nChoose a list of recipes using the numbers below:\n\n1-Alquemist Recipes\n2-Culinarian Recipes\n3-Armorer\n4-Black Smith\n5-Carpenter\n6-Gold Smith\n7-Leatherworker\n8-Weaver')
job = int(input('\n>'))
if job == 1:
    recipes = alquemistRecipes
elif job == 2:
    recipes = culinarianRecipes
elif job == 3:
    recipes = armorerRecipes
elif job == 4:
    recipes = blacksmithRecipes
elif job == 5:
    recipes = carpenterRecipes
elif job == 6:
    recipes = goldsmithRecipes
elif job == 7:
    recipes = leatherworkerRecipes
elif job == 8:
    recipes = weaverRecipes
clear()

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
        elif choose == 5:
            recipe = recipes[5]
        clear()
        number = input("\nEnter the amount to creaft, or 0 to craft until no more mats are available\n>")
        if number == 0:
            number = 9999
        else: 
            number = int(number)
        break
    except:
        print("\nOnly numbers from 1 to 5 are accepted")
        time.sleep(1)
clear()
print(f'\nCrafting... {number}  "{recipe}"')

time.sleep(5)
if job == 1:
    pyautogui.hotkey('alt','5', interval = 0.2)
elif job == 2:
    pyautogui.hotkey('alt','6', interval = 0.2)
elif job == 3:
    pyautogui.hotkey('alt','7', interval = 0.2)
elif job == 4:
    pyautogui.hotkey('alt','8', interval = 0.2)
elif job == 5:
    pyautogui.hotkey('alt','9', interval = 0.2)
elif job == 6:
    pyautogui.hotkey('alt','0', interval = 0.2)
elif job == 7:
    pyautogui.hotkey('alt','-', interval = 0.2)
elif job == 8:
    pyautogui.hotkey('alt',"'", interval = 0.2)


while con < number:
        time.sleep(1)
        cf.inputEnter("/clearlog") 
        cf.foodCheck()
        time.sleep(1)
        if pyautogui.locateOnScreen('synthezise.png', confidence=0.7) == None:
            pyautogui.hotkey('ctrl','n') 
            time.sleep(0.5)
            cf.inputRecipe(recipe,0,10)
            time.sleep(0.5)  
        cf.locateclickLAjsutable('synthezise.png',0, 0)
        time.sleep(1)
        if pyautogui.locateOnScreen("unabletocraft.png", confidence = 0.65) != None: 
            print("Not enough items for this recipe")
            print(f"Total Crafted {counterHQ} {recipe} HQ \n Total Crafted {counterNQ} {recipe} NQ\n Exiting the program now")
            exit()
        else:
            if pyautogui.locateOnScreen("35.png", confidence = 8) != None:
                pyautogui.hotkey('alt','3', interval=0.2)
                time.sleep(1)
                cf.inputEnter("")
            else:
                pyautogui.hotkey('alt','1', interval=0.2)
                time.sleep(1)
                cf.inputEnter("")
            while True:
                time.sleep(1)
                if pyautogui.locateOnScreen('macro1.png', confidence=0.8) != None:
                    break
            time.sleep(0.5)
            if pyautogui.locateOnScreen("35.png", confidence = 8) != None:
                pyautogui.hotkey('alt','4', interval=0.2)
                time.sleep(1)
            else:
                pyautogui.hotkey('alt','2', interval=0.2)
                time.sleep(1)
            while True:
                if pyautogui.locateOnScreen('macro2.png', confidence=0.8) != None:
                    time.sleep(1)
                    if pyautogui.locateOnScreen('progress.png', confidence=0.8) == None:
                        pass
                    else:
                        cf.inputEnter("/echo <se.6>")
                        time.sleep(0.5)
                        cf.locateclickL("quit.png")
                        time.sleep(2.5)
                        pyautogui.hotkey("ctrl","n", interval=0.1)
                        print(f"Craft has failed successfully at {dt_string}, check gear status before trying again. Press enter to exit. ¯\_(ツ)_/¯")
                        input()
                        exit()
                else:
                    continue
                time.sleep(1)
                if pyautogui.locateOnScreen('HQ.png', confidence=0.75) != None:
                    counterHQ = counterHQ + 3
                else:
                    counterNQ = counterNQ + 3
                if number > 0:
                    con = con+1
                break
clear()

print(f"Crafted {counterHQ} {recipe} HQ \nTotal Crafted {counterNQ} {recipe} NQ")
fin = input('Press Enter to exit\n >')
exit()




#/hotbar item "Chili Crab " 