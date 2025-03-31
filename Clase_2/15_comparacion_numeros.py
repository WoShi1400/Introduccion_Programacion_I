# 15 Programa de compacion de 2 numeros, si el primero es mayor, menor o igual
# al segundo

oper1 = int(input("Ingrese el primer operando: "))
oper2 = int(input("Ingrese el segundo operando: "))

if oper1 > oper2:
    print(f"El primer operando {oper1} es mayor que el segundo operando {oper2}")
elif oper1 < oper2:
    print(f"El primer operando {oper1} es menor que el segundo operando {oper2}")
else:
    print(f"El primer operando {oper1} es igual que el segundo operando {oper2}")
