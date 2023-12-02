# Un grupo de 35 estudiantes del primer trimestre reciben 5 competencias en el Sena y
# presentan 3 exámenes de cada competencia con los diferentes instructores. Diseñe un
# algoritmo que lea por cada estudiante las calificaciones obtenidas y calcule e imprima:

# A.- La cantidad de aprendices que obtuvieron una calificación menor a 2.
# B.- La cantidad de aprendices que obtuvieron una calificación de 2 y menos que 3
# C.- La cantidad de aprendices que obtuvieron una calificación de 3 y menos de 4
# D. La cantidad de aprendices que obtuvieron una calificación de 4 o más.
# H. Calcular el promedio de todos los aprendices.

notasAprendiz=0
acumPromAprendices=0
acumPromedios=0
sumaDePromedios=0

countMenosDe2=0
countMasDe2MenosDe3=0
countMasDe3MenosDe4=0
countMasDe4=0

for aprendiz in range(1, 36):
    print(f"Aprendiz {aprendiz}")

    for competencia in range(1, 6):
        print(f"Competencia {competencia}")

        for examen in range(1, 4):
            nota = float(input(f"Digite la nota del examen {examen}: "))
            notasAprendiz += nota

        promedioAprendiz=notasAprendiz/3
        acumPromAprendices += promedioAprendiz
        print(f"Promedio {promedioAprendiz}")
        print(f"Acum {acumPromAprendices}")
        print()
        notasAprendiz = 0

    if acumPromAprendices < 2.0:
        countMenosDe2 += 1

    elif acumPromAprendices >= 2.0 and acumPromAprendices < 3.0:
        countMasDe2MenosDe3 += 1

    elif acumPromAprendices >= 3.0 and acumPromAprendices < 4.0:
        countMasDe3MenosDe4 += 1

    elif acumPromAprendices >= 4.0:
        countMasDe4 += 1
    
    acumPromedios += acumPromAprendices
    promedioTotal = acumPromedios / 5
    sumaDePromedios += promedioTotal
    acumPromAprendices = 0
    acumPromedios = 0

total = sumaDePromedios / 35

print(f"obtuvieron una calificación menor a 2: {countMenosDe2}")
print(f"obtuvieron una calificación de 2 y menos que 3: {countMasDe2MenosDe3}")
print(f"obtuvieron una calificación de 3 y menos de 4: {countMasDe3MenosDe4}")
print(f"obtuvieron una calificación de 4 o más: {countMasDe4}")

print(f"Promedios: {total}")