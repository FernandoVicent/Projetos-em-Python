import sqlite3
from tkinter import *



banco = sqlite3.connect('Users.db')

cursor = banco.cursor()

# cursor.execute("CREATE TABLE pessoas (nome text,idade integer, email text)")

# cursor.execute("INSERT INTO pessoas VALUES('fernando',22,'fernando@gmail.com')")

#banco.commit()

# cursor.execute("SELECT email FROM pessoas")
#
# print(cursor.fetchall())
# # --------------------------------------------------------------------------------------

def logado():
    logado = Tk()
    logado.geometry("800x1200")
    logado.title('Bem Vindo')


login = Tk()
login.geometry("1200x700")
login.resizable(width=False, height=False)
login.title('Python_Book')

esconde_senha = StringVar()
image_fundo = PhotoImage(file="imgs/E-mail.png")
image_btn_reg = PhotoImage(file="imgs/Reg.png")
image_btn_con = PhotoImage(file="imgs/connect.png")

lab_fundo = Label(login, image=image_fundo)
lab_fundo.pack()

en_mail = Entry(login,bg="#41C1BA", font=("Calibri", 15), justify=CENTER)
en_mail.place(width=385,height=37,y=152,x=715,)

en_pass = Entry(login,textvariable=esconde_senha,show="*", bg="#41C1BA", font=("Calibri", 15), justify=CENTER)
en_pass.place(width=385,height=37,y=255,x=715,)

bt_reg = Button(login, bd=0,image=image_btn_reg,)
bt_reg.place(width=195,height=44,y=500,x=690,)

bt_log = Button(login, bd=0,image=image_btn_con,command=logado)
bt_log.place(width=195,height=44,y=500,x=940,)

login.mainloop()