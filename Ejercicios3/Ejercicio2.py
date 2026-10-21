#Datos iniciales

num_a = int(input("Numero A: "))
num_d = int(input("Numero D: "))
cantidad = int(input("Cantidad: "))

suma = 0
termino_actual = num_a

for veces in range(cantidad):
    suma += termino_actual
    termino_actual += num_d

print("Suma:", suma)

