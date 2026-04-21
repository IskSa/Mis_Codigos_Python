# Estructuras de Decisión

# edad < 18 -> joven
# edad 18 - 29 -> adulto
# edad 30 - 64 -> adulto mayor
# edad >= 65 - > tercera edad

edad = 80;

if (edad < 18):
    print("Usted es joven.");
elif(edad >= 18 and edad <= 29):
    print("Usted es un adulto.");
elif(edad >= 30 and edad <= 64):
    print("Usted es un adulto mayor.");
else:
    print("Usted es de la tercera edad.");

print("--------------------------")
print("Cualquier cosa!");

# random - randint
from random import randint as aleatorio

numeroAleatorio = aleatorio(10, 20);
print(numeroAleatorio);
