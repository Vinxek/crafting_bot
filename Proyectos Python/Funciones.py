from typing import Text
from pyautogui import *
import os
import pyautogui
import time
import win32api, win32con
clear = lambda: os.system('cls')
os.chdir(r'C:\Users\calic\Desktop\Proyectos Python\Imagenes')


def localizarIMAGEN(image):
    n=0
    while pyautogui.locateOnScreen(image, confidence=1-n) == None and n<=0.4:
        n=n+0.1
    if n>=0.4:
        print("No se encuentra la imagen");return False
    else:
        pos=pyautogui.locateCenterOnScreen(image, confidence=1-n)
        x=int(pos[0])
        y=int(pos[1])
        win32api.SetCursorPos((x,y));return True

def localizarIMAGEN2(image1,image2):
    n=0
    while pyautogui.locateOnScreen(image1, confidence=1-n) == None and n<=0.4:
        n=n+0.1
    if n>=0.4:
        print("No se encuentra la imagen");return False
    else:
        pos1=pyautogui.locateOnScreen(image1, confidence=1-n)
        pos2=pyautogui.locateCenterOnScreen(image2, confidence=1-n, region=(pos1))
        x=int(pos2[0])
        y=int(pos2[1])
        win32api.SetCursorPos((x,y));return True

def MoverCursor(x0,y0):
    x,y=win32api.GetCursorPos()
    win32api.SetCursorPos((x+x0,y+y0))

def noIMAGEN(image,limite):
    limite=1-limite
    n=0
    while pyautogui.locateOnScreen(image, confidence=0.7) == None and n<=limite:
        n=n+0.1
    if n>=limite:
        print("No se encuentra la imagen");return False
    else:
        print("Imagen encontrada");return True

def foodCHECK(Buff,Comida,Use,Inventario):
    if noIMAGEN(Buff,0.7) == False:
        if noIMAGEN(Inventario,0.7) == False:
            pyautogui.hotkey('alt', 'i'),time.sleep(0.3)
        localizarIMAGEN(Comida),time.sleep(0.3)
        pyautogui.rightClick(),time.sleep(0.3)
        localizarIMAGEN(Use),time.sleep(0.3)
        pyautogui.leftClick(),time.sleep(0.3)
        pyautogui.leftClick(),time.sleep(0.3)

def BuscarReceta(RecipeSearch,RecipeText,Text,CraftingLog):
    if noIMAGEN(CraftingLog,0.7) == False:
        pyautogui.hotkey('ctrl','n'),time.sleep(0.3)
    localizarIMAGEN2(RecipeSearch,RecipeText),time.sleep(0.3)
    pyautogui.leftClick(),time.sleep(0.3)
    pyautogui.write(Text),time.sleep(0.3)
    pyautogui.press('enter'),time.sleep(0.3)

def SeleccionarMateriales(CraftingLog,HQMaterials,HQ,Ingrediente1,Ingrediente2,Ingrediente3,Ingrediente4,Ingrediente5,Ingrediente6):
    i1=0;i2=0;i3=0;i4=0;i5=0;i6=0
    if noIMAGEN(CraftingLog,0.7) == True:
        localizarIMAGEN2(HQMaterials,HQ),time.sleep(1)
        while i1<=Ingrediente1:
            pyautogui.leftClick(),time.sleep(0.3)
            i1=i1+1
        MoverCursor(0,60)
        while i2<=Ingrediente2:
            pyautogui.leftClick(),time.sleep(0.3)
            i2=i2+1
        MoverCursor(0,60)
        while i3<=Ingrediente3:
            pyautogui.leftClick(),time.sleep(0.3)
            i3=i3+1
        MoverCursor(0,60)
        while i4<=Ingrediente4:
            pyautogui.leftClick(),time.sleep(0.3)
            i4=i4+1
        MoverCursor(0,60)
        while i5<=Ingrediente5:
            pyautogui.leftClick(),time.sleep(0.3)
            i5=i5+1
        MoverCursor(0,60)
        while i6<=Ingrediente6:
            pyautogui.leftClick(),time.sleep(0.3)
            i6=i6+1
    else:
        return False


def limpiar():
    pyautogui.press('esc'),time.sleep(0.3)
    pyautogui.press('esc'),time.sleep(0.3)
    pyautogui.press('enter'),time.sleep(0.3)
    pyautogui.write('/clearlog'),time.sleep(0.3)
    pyautogui.press('enter'),time.sleep(0.3)


time.sleep(2)
#BuscarReceta("RecipeSearch.png","RecipeSearchText.png","Grade 4 Tincture of Mind","CraftingLog.png")
SeleccionarMateriales("CraftingLog.png","HQMaterials.png","HQ.png",0,0,1,0,0,0)