import random;
n = random.randint(1, 10);
n1 = int(input("Elige un numero: "))
if (n == n1):
    print("ganaste")
else:
    n2 = n1 = int(input("Elige un numero 2: "))
    if (n == n1):
        print("ganaste2")
    else:
        print("perdiste2")