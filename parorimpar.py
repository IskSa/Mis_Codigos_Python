from random import randint as num1
num = num1(1, 100)
n = input("Elige es impar o par: ")
if (num % 2 == 0 and n == "par"):
    print(f"El {num} es PAR ganaste")
elif (num % 2 == 1 and n == "impar"):
    print(f"El {num} es impar ganaste")
else:
    print(f"el {num} perdiste")