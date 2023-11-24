# Elabore un algoritmo que muestre el promedio de edad de dos grupos, cada grupo tiene 3 aprendices.
edades = 0
sumaEdadesGrupos = 0
for grupo in range(2):
    for aprendiz in range(3):
        edad = int(input(f"Digite la edad del aprendiz {aprendiz + 1}: "))
        edades += edad
    promedio = edades / 3
    sumaEdadesGrupos = sumaEdadesGrupos + promedio
    edades = 0
    print(f"El promedio de edad del grupo {grupo+1} es: {promedio}")
promedioGeneral = sumaEdadesGrupos / 2
print(f"El promedio de los dos grupos es: {promedioGeneral}")
