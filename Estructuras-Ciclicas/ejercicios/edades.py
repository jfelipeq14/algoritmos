acumEdades = 0

for i in range(6):
    edad = int(input(f"Digite la edad {i+1}: "))
    acumEdades = acumEdades + edad
promedio = acumEdades / 6
print(f"El promedio de edades es {promedio}")
