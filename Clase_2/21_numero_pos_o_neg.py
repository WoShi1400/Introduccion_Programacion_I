# 21 Program para verificar si el numero ingresado por el usuario es positivo, negativo o cero.

print("Este programa determina si el numero es positivo, negativo ocero")

numero = int(input("Ingresa un numero: "))

if numero > 0:
    print("El numero ingresado es positivo.")
elif numero < 0:
    print("El numero ingresado es negativo")
else:
    print("El numero ingresado es cero")
