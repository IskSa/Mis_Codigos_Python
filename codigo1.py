import random

numero_secreto = random.randint(1, 10)

numero = 0

while numero != numero_secreto:

    numero = int(input("Adivina el número entre 1 y 10: "))

    if numero == numero_secreto:
        print("🎉 ¡Correcto! Adivinaste el número")

    elif numero > numero_secreto:
        print("❌ Incorrecto")
        print("El número secreto es menor")

    else:
        print("❌ Incorrecto")
        print("El número secreto es mayor")