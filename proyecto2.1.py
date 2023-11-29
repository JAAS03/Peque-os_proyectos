print('*** CALCULADORA EN PYTHON ***')
salir = False
while not salir:

    print('''Operaciones que puede realizar:
        1. SUMA
        2. RESTA
        3. MULTIPLICACION
        4. DIVISION
        5. SALIR''')
    opcion = int(input('Escoje una opcion: '))
    if opcion <= 4:
        valor1 = float(input(f'Dame el valor 1: '))
        valor2 = float(input(f'Dame el valor 2: '))
    if opcion == 1:
        resultado_sum = valor1 + valor2
        print(f'El resultado de la suma es: {resultado_sum}')
    elif opcion == 2:
        resultado_res = valor1 - valor2
        print(f'El resultado de la resta es: {resultado_res}')
    elif opcion == 3:
        resultado_mul = valor1 * valor2
        print(f'El resultado de la multiplicacion es: {resultado_mul}')
    elif opcion == 4:
        resultado_div = valor1 / valor2
        print(f'El resultado de la division es: {resultado_div}')
    elif opcion == 5:
        salir = True
        print('Saliendo del sistema.')
    else:
        print('Opcion invalida, vuelva a escoger una.')