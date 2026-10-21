numero = int(input("Ingrese la cantidad de empleados: "))

total_nomina = 0

for nomina in range(numero):
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    total_nomina += sueldo

print("Nomina:", total_nomina)