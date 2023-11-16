# while leer edad de 10 companheros, mostrarlas y tambien la edad menor, mayor, promedio
contador = 1
acumEdades = 0
menor = 100
mayor = 0
edades = []
while contador <= 10:
    edad = int(input(f"Digite la edad {contador}: "))
    if edad <= menor:
        menor = edad
    if edad >= mayor:
        mayor = edad
    edades.append(edad)
    acumEdades = acumEdades + edad
    contador += 1

promedio = acumEdades / 10

print(f"Las edades son {edades}")
print(f"La edad menor es {menor}")
print(f"La edad mayor es {mayor}")
print(f"El promedio de edades es {promedio}")
