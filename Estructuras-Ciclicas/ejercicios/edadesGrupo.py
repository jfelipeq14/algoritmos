# Elabore un algoritmo que muestre el promedio de edad de dos grupos, cada grupo tiene 3 aprendices.
edades = 0
promedioGeneral = 0
for grupo in range(2):
    for aprendiz in range(3):
        edad = int(input(f"Digite la edad del aprendiz {aprendiz + 1}: "))
        edades += edad
    promedio = edades / 3
    promedioGeneral = promedioGeneral + promedio
    edades = 0
    print(f"El promedio de edad del grupo {grupo+1} es: {promedio}")
print(f"El promedio de los dos grupos es: {promedioGeneral}")
