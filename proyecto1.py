#PRIMER PROYECTO
from random import randint
print('*** SISTEMA DE GENERADOR ID UNICO ***')
nombre = input('¿Cual es tu Nombre?: ')
nombre_re = nombre[0:2]
apellido = input('¿Cual es tu Apellido?: ')
apellido_re = apellido[0:2]
an_nacimiento = input('¿Cual es tu Año de nacimiento?: ')
an_nacimiento_re = an_nacimiento[2:5]
aleatorio = randint (0,9999)
#gen_ID = nombre[0:2] + apellido[0:2] + an_nacimiento[2:5]

gen_ID = f'{nombre_re}{apellido_re}{an_nacimiento_re}{aleatorio}'
print(f'''¡Hola {nombre}, Bienvenido a la empresa! '
      \tTu numero de identificacion (ID) generado por el sistema es:
      \t{gen_ID.upper()}
      \t¡Felicidades!''')
