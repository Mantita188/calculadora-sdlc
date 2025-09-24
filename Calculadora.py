#Proyecto creacion de una calculadora :D
memoria = 0 #Creada para que la calculadora pueda guardar los resultados de las operaciones y poder reutilizarlas.
while True: 
    print("Opciones:")
    print("a) Sumar")
    print("b)Restar (proximamente)")
    print("c)Multiplicar (proximamente)")
    print("d)Dividir (proximamente)")
    print("e) Salir")
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
                numero_str = input(f"Ingresa el número {i + 1}: ")
                numero = float(numero_str)
                total_suma = total_suma + numero

            print(f"\n>> El resultado de la suma es: {total_suma}")
            memoria = total_suma

        except ValueError:
            print("Error: Ingresaste un valor no numérico. Intenta de nuevo.")

    elif opcion == 'e':
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elige 'a' o 'e'.")