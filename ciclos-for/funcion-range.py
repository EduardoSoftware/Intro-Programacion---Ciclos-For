"""
Sintaxis de la funcion range()

range([inicio], fin, [paso])

- El inicio es 0 por defecto, si no se indica
- El paso es 1 por defecto si no lo indica

- La funcion range genera una serie de numeros int entre inicio y fin-1, con incremento dado por el paso

"""

# caso 1: range(fin)
print(list(range(10))) #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
## El paso e incremento por defecto es 1, el fin va hasta el -1
print(list(range(101)))
## Va del 0 hasta el 100, porque no se definio un inicio y su paso por defecto es 1, hasta el -1
print(list(range(32)))
## Va desde el 0 hasta el 31 porque le resta -1 al dato que le dimos es decir (32-1 = 31)



# caso 2: range(inicio, fin)
print(list(range(3, 10)))
## Esto imprime 3, 4, 5, 6, 7, 8, 9
print(list(range(11, 13)))
## Esto imprime 11, 12
print(list(range(1001, 1002)))
## Esto imprime 1001



# caso 3: range(inicio, fin, paso)
print(list(range(3, 20, 2)))
## Esto imprime 3, 5, 7, 9, 11, 13, 15, 17, 19. Porque el paso marcado es de 2 en 2, debido al paso establecido 2
print(list(range(3, 21, 2)))
## Esto imprime 3, 5, 7, 9 ....., 17, 19. Porque va de paso 2 y se meve dentro de impares porque el inicio fue impar
print(list(range(5, 51, 5)))
## Los 10 primeros multiplos de 5
print(list(range(15, 25, 2)))
# Los primeros 5 pares desde el 15
print(list(range(21, 0, -2)))
# Esto imprime los impares del 21 hasta el 1


