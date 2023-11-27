#PROYECTO 2

print('*** Bienvenido al sistema de generación de emails ***')

nombre = input('¿Cual es tu Nombre?: ')
apellido = input('¿Cual es tu Apellido?: ')
an_nacimiento = input('¿Cual es tu Año de nacimiento?: ')

gen_email = f'{nombre.lower()}.{apellido.lower()}{an_nacimiento}@gmail.com'

print(f'''Hola {nombre}, tu nuevo email generado por el sistema es:
        \t{gen_email}
        \t*** BIENVENIDO ***''')