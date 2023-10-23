e1, e2, e3, e4, e5, e6, e7, e8, e9, e10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 #se debe asignar un valor inicial a cada variable

e1 = int(input("Ingrese el valor de e1: "))
e2 = int(input("Ingrese el valor de e2: "))
e3 = int(input("Ingrese el valor de e3: "))
e4 = int(input("Ingrese el valor de e4: "))
e5 = int(input("Ingrese el valor de e5: "))
e6 = int(input("Ingrese el valor de e6: "))
e7 = int(input("Ingrese el valor de e7: "))
e7 = int(input("Ingrese el valor de e8: ")) # Error: e7 se lee 2 veces
e9 = int(input("Ingrese el valor de e9: "))
e10 = int(input("Ingrese el valor de e10: "))

suma = e1 + e2 + e3 + e4 + e5 + e6 + e7 + e8 + e9 + e10
promedio = suma / 10 #4.8

print(f'El promedio de las edades es: {promedio}')