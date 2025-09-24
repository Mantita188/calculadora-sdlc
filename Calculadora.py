#Proyecto creacion de una calculadora :D
memoria = 0 #Creada para que la calculadora pueda guardar los resultados de las operaciones y poder reutilizarlas.
while True: 
    print("Menú de la Calculadora:")
    print("a) Sumar")
    print("b) Restar") 
    print("c) Multiplicar") 
    print("d) Dividir")
    print("e) Potencia (^)")
    print("f) Porcentaje (%)") 
    print("h) Limpiar Memoria")
    print("i) Salir")
    opcion = input("Elige la operación que quiere realizar a continuacion: ").lower()
    print("--------------------------------")

    if opcion == 'a': 
        total_suma = 0
        if memoria != 0:
            usar_memoria = input(f"¿Quieres empezar la suma con el número {memoria}? (si/no): ").lower()
            if usar_memoria == 'si':
                total_suma = memoria
        try:
            cantidad_numeros = int(input("¿Cuántos números quieres sumar?: "))
            for i in range(cantidad_numeros):
                numero_str = input(f"Ingresa el número {i + 1} a sumar: ")
                numero = float(numero_str)
                total_suma = total_suma + numero
            print(f"El resultado de la suma es: {total_suma}")
            memoria = total_suma
        except ValueError:
            print("Error: Ingresaste un valor no numérico. Intenta de nuevo.")

    elif opcion == 'b':
        total_resta = 0
        try:
            if memoria != 0:
                usar_memoria = input(f"¿Quieres empezar a restar desde el número {memoria}? (si/no): ").lower()
                if usar_memoria == 'si':
                    total_resta = memoria
                else:
                    primer_numero_str = input("Ingresa el número inicial: ")
                    total_resta = float(primer_numero_str)
            else:
                primer_numero_str = input("Ingresa el número inicial: ")
                total_resta = float(primer_numero_str)
            cantidad_numeros = int(input("¿Cuántos números quieres restar?: "))
            for i in range(cantidad_numeros):
                numero_str = input(f"Ingresa el número {i + 1} a restar: ")
                numero = float(numero_str)
                total_resta = total_resta - numero
            print(f"El resultado de la resta es: {total_resta}")
            memoria = total_resta
        except ValueError:
            print("Error: Ingresaste un valor no numérico. Intenta de nuevo.")

    elif opcion == 'c':
        total_multiplicacion = 1
        try:
            if memoria != 0:
                usar_memoria = input(f"¿Quieres empezar a multiplicar desde el número {memoria}? (si/no): ").lower()
                if usar_memoria == 'si':
                    total_multiplicacion = memoria
                else:
                    primer_numero_str = input("Ingresa el primer número para multiplicar: ")
                    total_multiplicacion = float(primer_numero_str)
            else:
                primer_numero_str = input("Ingresa el primer número para multiplicar: ")
                total_multiplicacion = float(primer_numero_str)
            cantidad_numeros = int(input("¿Cuántos números más quieres multiplicar?: "))
            for i in range(cantidad_numeros):
                numero_str = input(f"Ingresa el número {i + 1} a multiplicar: ")
                numero = float(numero_str)
                total_multiplicacion = total_multiplicacion * numero 
            print(f"El resultado de la multiplicación es: {total_multiplicacion}")
            memoria = total_multiplicacion
        except ValueError:
            print("Error: Ingresaste un valor no numérico. Intenta de nuevo.")
    
    elif opcion == 'd':
        total_division = 0
        try:
            if memoria != 0:
                usar_memoria = input(f"¿Quieres empezar a dividir desde el número {memoria}? (si/no): ").lower()
                if usar_memoria == 'si':
                    total_division = memoria 
                else:
                    primer_numero_str = input("Ingresa el dividendo (número a dividir): ")
                    total_division = float(primer_numero_str)
            else:
                primer_numero_str = input("Ingresa el dividendo (número a dividir): ")
                total_division = float(primer_numero_str)
            cantidad_numeros = int(input("¿Por cuántos números quieres dividir?: "))
            operacion_cancelada = False
            for i in range(cantidad_numeros):
                numero_str = input(f"Ingresa el divisor {i + 1}: ")
                numero = float(numero_str)
                if numero == 0:
                    print("Error: No se puede dividir por cero. Operación cancelada.")
                    operacion_cancelada = True
                    break 
                total_division = total_division / numero
            if not operacion_cancelada:
                 print(f">> El resultado de la división es: {total_division}")
                 memoria = total_division
        except ValueError:
            print("Error: Ingresaste un valor no numérico. Intenta de nuevo.")

    elif opcion == 'e':
        try:
            base = 0
            if memoria != 0:
                usar_memoria = input(f"¿Quieres usar el número en memoria ({memoria}) como base? (si/no): ").lower()
                if usar_memoria == 'si':
                    base = memoria
                else:
                    base = float(input("Ingresa el número base: "))
            else:
                base = float(input("Ingresa el número base: "))
            
            exponente = float(input("Ingresa el exponente: "))
            
            resultado = base ** exponente
            
            print(f" El resultado de {base} elevado a {exponente} es: {resultado}")
            memoria = resultado
        except ValueError:
            print("Error: Ingresaste un valor no numérico. Intenta de nuevo.")

    elif opcion == 'f':
        try:
            total = 0
            if memoria != 0:
                usar_memoria = input(f"¿Quieres calcular el porcentaje del número en memoria ({memoria})? (si/no): ").lower()
                if usar_memoria == 'si':
                    total = memoria
                else:
                    total = float(input("Ingresa el número total para calcularle el porcentaje: "))
            else:
                total = float(input("Ingresa el número total para calcularle el porcentaje: "))
            porcentaje = float(input(f"Ingresa el porcentaje que deseas calcular de {total} (ej: 15 para 15%): "))
            
            resultado = (total * porcentaje) / 100
            
            print(f"El {porcentaje}% de {total} es: {resultado}")
            memoria = resultado
        except ValueError:
            print("Error: Ingresaste un valor no numérico. Intenta de nuevo.")

    elif opcion == 'h':
        memoria = 0
        print("La memoria ha sido limpiada.")

    elif opcion == 'i':
        print("¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Por favor, elige una de las opciones.")

