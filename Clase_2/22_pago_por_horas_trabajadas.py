# 22 Programa que muestra la paga correspondiente segun la formula del numero de horas trabajadas y el costo por hora.

print("Este programa muestra la paga segun nº hs trabajadas y el costo por hora")

hs_trabajadas = int(input("Cuantas horas trabajas?: "))

costo_hora = int(input("Cuanto ganas por hora?: "))

paga_total = hs_trabajadas * costo_hora

print(f"El pago correspondiente es de: {paga_total}")
