from funçoes import *
from tkinter import *

login = Tk()
login.geometry("1200x700")
login.title('Python_Book')

image_fundo = PhotoImage(file="imgs/E-mail.png")


login.mainloop()
#rede Social V:0.0.1




# name = input("digite o seu nome completo: ")
# birth = input("digite a data do seu nascimento: ")
# email = input("digite seu e-mail: ")
# passwd = input("digite uma senha: ")




def cria_usuario(name, birth, email, password):

    conta = {"name": name, "birth": birth, "email": email, "password": password}
    return conta
# def add_friend():
#
# def view_friends():
#
# def mutual_friends():