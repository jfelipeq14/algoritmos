# 14.Calcular el promedio de un alumno que tiene 7 calificaciones en la materia de Algoritmos

acumNotas = 0
for i in range(7):
    nota = float(input(f"Digite el nota {i+1}: "))
    acumNotas += nota
promedio = acumNotas / 7
print(f"El promedio de las notas es {promedio}")
