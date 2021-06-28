from Funciones import *
import os
import pyautogui
import time
import win32api, win32con
clear = lambda: os.system('cls')
os.chdir(r'C:\Users\calic\Desktop\Proyectos Python\Imagenes')

Receta=""

Receta=input("\nIngrese nombre de la receta\n>")
time.sleep(3)
limpiar()
foodCHECK("BuffFood.png","PruebaFood.png","Use.png","Inventario.png")
BuscarReceta("RecipeSearch.png","RecipeSearchText.png",Receta,"CraftingLog.png")
SeleccionarMateriales("CraftingLog.png","HQMaterials.png","HQ.png",0,0,1,0,0,0)
