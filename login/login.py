from main import *
import sqlite3
from tkinter import *
#----------------------------------registro-----------------------------------------------------
def sigin():
 name = input("digite seu nome: ")
 birth = input("digite sua data de nascimento: ")
 email = input("digite seu email: ")
 password = input("digite uma senha: ")
 cursor.execute(f"INSERT INTO pessoas VALUES('{name}','{birth}','{email}','{password}')")

 #-------------------------------------validação---------------------------------------------------

 if(birth > '31/12/2001'):
   print("so é possivel se registrar maiores de 18 anos")
 else:
  banco.commit()
  cursor.execute("SELECT * FROM pessoas")

def login():
    try:
        id = input("digte o email: ")
        l_senha = input("digite a senha")
        cursor = banco.cursor()
        cursor.execute(f"SELECT password FROM pessoas WHERE email ='{id}'")
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
        banco.close()
    except:
        print('errro')
    if l_senha == senha_bd[0][0]:
        print("Voce logou")
    else:
        print("voce nao logou")

menu = input("logar ou registrar")

if(menu == "registrar"):
    sigin()
else:
    login()