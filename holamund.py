def Multipicador():
    print("Multiplicador")
    print("presiona enter para continuar...")
    input()
    numeros = []
    resultado = 1

    while True:

        numero = input("Número (salir para terminar): ")

        if numero == "salir":
           break

        numero = int(numero)

        numeros.append(numero)

        resultado = resultado * numero

        print("Resultado acumulado:", resultado)

def menu():
    while True:
        print("\nMENU")
        print("1 - Multiplicador")
        print("2 - Salir")
        
        opcion = input("elige una opcion: ")

        if opcion == "1":
            Multipicador()
        elif opcion == "2":
            print ("cerrando programa")
            break
        else:
            print("opcion invalida")

menu()