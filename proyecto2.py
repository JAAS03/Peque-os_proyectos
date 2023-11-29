print('*** CAJERO AUTOMATICO ***')
dinero = 1000
salir = False

while not salir:
    print('''Operaciones que puedes realizar:
        1. Consultar saldo
        2. Retirar
        3. Depositar
        4. Salir''')

    opcion = int(input('Seleccione una opcion: '))

    if opcion == 1:
        print(f'Tu saldo disponible es: ${dinero:.2f}')
    elif opcion == 2:
            retiro = float(input('El monto a retirar es: '))
            if dinero >= retiro:
                dinero -= retiro
                print(f'Tu saldo actual es: ${dinero:.2f}')
            else:
                print('No tiene el dinero suficiente para retirar')
    elif opcion == 3:
        depositar = float(input('El monto a depositar es: '))
        dinero += depositar
        print(f'Tu saldo actual es: ${dinero:.2f}')
    elif opcion == 4:
        print('Saliendo del sistema. Muchas gracias por su preferencia.')
        salir = True
    else:
        print('Opcion invalida, vuelve a elegir una opcion.')