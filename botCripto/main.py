import pyautogui
import sqlite3
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.write('google')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('luna rush')
pyautogui.press('enter')
time.sleep(2)
abre = pyautogui.locateOnScreen('rush.png')
pyautogui.click(abre)
time.sleep(2)
joga = pyautogui.locateOnScreen('play.png')
pyautogui.click(joga)
time.sleep(30)
loga = pyautogui.locateOnScreen('entrar.png')
pyautogui.click(loga)



