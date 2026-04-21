n1 = int(input("ingrese su Quintil: "))
n2 = input("ingrese su situacion laboral(empleado o desempleado): ")
n3 = int(input("ingrese su edad: "))
plata = 0
if ((n1 == 1) or (n1 == 2)) and (n2 == "empleado"):
    plata = 8000
    print("recibe 8.000")
elif ((n1 == 1) or (n1 == 2)) and (n2 == "desempleado"):
    plata = 10000
    print("recibe 10.000")
elif ((n1 == 3) and (n2 == "empleado")):
    plata = 4000
    print("recibe 4.000")
elif ((n1 == 3) and (n2 == "desempleado")):
    plata = 6000
    print("recibe 6.000")
elif ((n1 == 4) or (n1 == 5)):
    plata = 1500
    print("recibe 1.500")

if ((n1 == 1) or (n1 == 2)) and (n3 > 65):
    plata = plata + 5000
    print(f"usted recibio los 2 bonos extra de 5000 su total es: {plata} ")
elif ((n3 > 65)):
    plata = plata + 3000
    print(f"print usted por se mayor de 65 recibio un bono extra de 3000 su total es: {plata} ")
elif ((n1 == 1) or (n1 == 2)):
    plata = plata + 2000
    print(f"print usted por ser del quintil 1 o 2 recibio un bono extra de 2000 su total es: {plata} ")
