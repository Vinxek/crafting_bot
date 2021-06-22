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
        time.sleep(0.5)
        craftingMacroL(posInt2[0], posInt2[1])
        time.sleep(0.5)

def locateclickR(image):
    if pyautogui.locateOnScreen(image, confidence=0.6) != None:
        posB = pyautogui.locateOnScreen(image, confidence=0.6)
        pyautogui.moveTo(posB)
        posC = str(pyautogui.position())
        posA = re.findall(r'\d+', posC)
        posInt1 = map(int, posA)
        posInt2 = list(posInt1)
        time.sleep(0.5)
        craftingMacroR(posInt2[0], posInt2[1])
        time.sleep(0.5)

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

time.sleep(2)

while True:
    if pyautogui.locateOnScreen('buff.png', confidence=0.5) == None:
        inputEnter("")
        time.sleep(0.2)
        inputEnter("/clearlog")
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(2.5)
        pyautogui.press('esc')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','n')
        pyautogui.hotkey('alt', 'i')
        locateclickR('craftingBuff.png')
        locateclickL('use.png')
        input()
        time.sleep(1)
        locateclickL('synthezise.png')
        time.sleep(1)
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
    else:
        inputEnter("")
        time.sleep(0.2)
        inputEnter("/clearlog")
        time.sleep(0.5)
        time.sleep(0.5)
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



#pyautogui.displayMousePosition()
#pyautogui.click(x=905, y=837) slow

