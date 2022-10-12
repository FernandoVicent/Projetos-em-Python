# import pyautogui
import time
import sqlite3
from tkinter import *


with sqlite3.connect("database.db") as db:
     cursor =  db.cursor()
# cursor.execute("""CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY AUTOINCREMENT, username text NOT NULL, password text NOT NULL); """)



def Logado():
    primary = Tk()
    primary.geometry("600x600")
    primary.resizable(width=False, height=False)
    primary.title('bot-Cripto')

    ground = PhotoImage(file='img\ground.png')

    lab_back = Label(primary, image=ground)
    lab_back.pack()

    bt_executa = Button(primary, bd=4, text='executa', command= executa)
    bt_executa.place(width=100, height=20, y=15, x=260)

    primary.mainloop()


def Loga():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()

        logUsername = en_mail.get()
        logPassword = en_pass.get()

        find_user = ('SELECT * FROM users WHERE username = ? and password = ?')
        cursor.execute(find_user, [logUsername,logPassword])

        results = cursor.fetchall()

        if results:
            login.destroy()
            Logado()
        else:
            error["text"] = "usuario ou senha invalido"

def executa():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('google')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('https://blog.finxter.com/how-to-convert-a-string-list-to-an-integer-list-in-python/')
    pyautogui.press('enter')
    time.sleep(4)

    time.sleep(2)

    # joga = pyautogui.locateOnScreen('img/play.png')
    # pyautogui.click(joga)
    # time.sleep(30)
    # loga = pyautogui.locateOnScreen('img/entrar.png')
    # pyautogui.click(loga)

def Registra():
    newUsername =en_mail.get()
    newPassword = en_pass.get()
    cursor.execute("SELECT COUNT(*) from users WHERE username = '"+ newUsername + "'")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        error["text"] = "Error: Username already exists"
    else:
        error["text"] = "Added new user"
        cursor.execute("INSERT INTO users(username,password)VALUES(?,?)",(newUsername,newPassword) )
        db.commit()

login = Tk()
login.geometry("300x300")
login.resizable(width=False, height=False)
login.title('bot-Cripto')

imagem = PhotoImage(file="img\multi.png")

lab_fundo = Label(login, image=imagem)
# lab_fundo.place(x=0,y=0)

lab_fundo.pack()


error = Message(text="", width=160)
error.place(x=80,y=10)
error.config(padx=0 )

#------------------------usuario----------------------------------------------------

en_mail = Entry(login,bg="#d4cac9", font=("Calibri", 15), justify=CENTER,)
en_mail.place(width=160,height=27,y=110,x=70,)

#---------------------------------Senha-----------------------------------------------------#

en_pass = Entry(login, show="*", bg="#d4cac9", font=("Calibri", 15), justify=CENTER)
en_pass.place(width=160,height=27,y=180,x=70,)

#------------botão----------------------------------

bt_log = Button(login, bd=1,text='logar', command=Loga)
bt_log.place(width=65,height=20,y=220,x=60,)

bt_reg = Button(login, bd=1,text='reg', command=Registra)
bt_reg.place(width=65,height=20,y=220,x=160,)

login.mainloop()

