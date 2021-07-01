from pyautogui import *
import os
import pyautogui
import time
import win32api, win32con
clear = lambda: os.system('cls')


def craftingMacroL(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.2)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.2)

def craftingMacroR(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    time.sleep(0.2)

def foodCheck():
    if pyautogui.locateOnScreen('buff.png', confidence=0.8) == None:
        if pyautogui.locateOnScreen('craftinglog.png', confidence = 0.6) != None:
            pyautogui.hotkey('ctrl','n')
            time.sleep(3)
        pyautogui.hotkey('ctrl','1', interval=0.2)
        time.sleep(1)

def locateclickL(image):
    conf=0
    while pyautogui.locateOnScreen(image, confidence=0.8) != None and conf<=0.4:
        if conf>=0.4:
            pass
        else:
            pos=pyautogui.locateCenterOnScreen(image, confidence=1-conf)
            craftingMacroL(pos[0], pos[1])
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

def inputRecipe(recipe,x,y):
    if pyautogui.locateOnScreen('search.png', confidence=0.8) != None:
        posB = pyautogui.locateOnScreen('search.png', confidence=0.6)
        pyautogui.moveTo(posB)
        posC = str(pyautogui.position())
        posA = re.findall(r'\d+', posC)
        posInt1 = map(int, posA)
        posInt2 = list(posInt1)
        time.sleep(0.5)
        craftingMacroL(posInt2[0] + x, posInt2[1] + y)
        time.sleep(0.5)
        inputEnter(f"{recipe}")
        time.sleep(1)
        hqMats("materials.png")
        time.sleep(0.5)

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

def hqMats (search):
    des = 26
    mats = 0
    if pyautogui.locateOnScreen(search, confidence=0.7) != None:
        posB = pyautogui.locateOnScreen(search, confidence=0.8)
        pyautogui.moveTo(posB)
        posC = str(pyautogui.position())
        posA = re.findall(r'\d+', posC)
        posInt1 = map(int, posA)
        posInt2 = list(posInt1)
        craftingMacroL(posInt2[0] + 50, posInt2[1] + des)
        while mats < 6:
            craftingMacroL(posInt2[0] + 50, posInt2[1] + des)
            craftingMacroL(posInt2[0] + 50, posInt2[1] + des)
            des = des+35
            mats = mats+1
