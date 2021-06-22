from pyautogui import *
import os
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Key, Controller
keyboard = Controller()
os.chdir(r'C:\Users\Vinxe\Documents\Python\Projectos')

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

def inputEnter(recepi):
    keyboard.type(recepi)
    time.sleep(1)
    pyautogui.press('enter')

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
    if pyautogui.locateOnScreen(image, confidence=0.6) != None:
        posB = pyautogui.locateOnScreen(image, confidence=0.6)
        pyautogui.moveTo(posB)
        posC = str(pyautogui.position())
        posA = re.findall(r'\d+', posC)
        posInt1 = map(int, posA)
        posInt2 = list(posInt1)
        craftingMacroR(posInt2[0], posInt2[1])
        time.sleep(0.7)

def input():
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
        inputEnter("Grade 4 Tincture of intelligence")

def openClose():
        inputEnter("")
        time.sleep(0.2)
        inputEnter("/clearlog")
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(4)
        pyautogui.press('esc')
        time.sleep(0.5)

time.sleep(2)

while True:
    if pyautogui.locateOnScreen('buff.png', confidence=0.6) == None:
        openClose() #cierra 2 ventanas abiertas
        pyautogui.hotkey('ctrl','n') #abre el craftinglog
        pyautogui.hotkey('alt', 'i') #abre el inventario
        locateclickR('craftingBuff.png') #selecciona la comida
        locateclickL('use.png') #usa la comida
        input() #busca la receta
        time.sleep(1)
        if pyautogui.locateOnScreen("ingredient#3.png", confidence = 0.8) != None:   
            locateclickLAjsutable("ingredient#3.png",-20,0)
            time.sleep(0.5)  
        locateclickL('synthezise.png') #empieza la sintesis
        time.sleep(1)
        craftingMacroL(676, 618) #click izquierdo en el boton de crafteo
        while True: #Espera a que la sintesis complete el prime macro
            time.sleep(1)
            if pyautogui.locateOnScreen('macro1.png', confidence=0.8) != None:
                break
        time.sleep(0.5)
        craftingMacroL(649, 631) #click izquierda en el segundo macro
        while True: #Espera a que el segundo macro se complete
            time.sleep(1)
            if pyautogui.locateOnScreen('macro2.png', confidence=0.8) != None:
                break
    else:
        inputEnter("")
        time.sleep(0.2)
        inputEnter("/clearlog") #limpia el log
        time.sleep(1)
        locateclickL('synthezise.png')
        craftingMacroL(676, 618)
        while True:
            time.sleep(1)
            if pyautogui.locateOnScreen('macro1.png', confidence=0.8) != None:
                break
        time.sleep(0.5)
        craftingMacroL(649, 631)
        while True:
            time.sleep(1)
            if pyautogui.locateOnScreen('macro2.png', confidence=0.8) != None:
                break
    continue



