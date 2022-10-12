import os
import time

horario = time.localtime()

while horario[3] != 00:

    hora = time.localtime()
    print(hora[3],hora[4])
    comando = 'shutdown -a'
    os.system(comando)