import random;
d = random.randint(1, 6);
d2 = random.randint(1, 6);
print("Elige un dado")
n = input("Elige entre 1 o 2: ")
if ((d > d2 and n == "1") or (d < d2 and n == "2")):
    print("ganaste")
elif((d < d2 and n == "1") or (d > d2 and n == "2")):
    print("perdiste")
else:
    print("empate tu 2 intento")
    d = random.randint(1, 6);
    d2 = random.randint(1, 6);
    print("Elige un dado")
    n = input("Elige entre 1 o 2: ")
    if ((d > d2 and n == "1") or (d < d2 and n == "2")):
        print("ganaste")
    elif((d < d2 and n == "1") or (d > d2 and n == "2")):
        print("perdiste")
    else:
        
        print("empate tu 3 intento")
        d = random.randint(1, 6);
        d2 = random.randint(1, 6);
        print("Elige un dado")
        n = input("Elige entre 1 o 2: ")
        if ((d > d2 and n == "1") or (d < d2 and n == "2")):
            print("ganaste")
        elif((d < d2 and n == "1") or (d > d2 and n == "2")):
            print("perdiste")
        else:
            print("perdiste")
