# Calcular el promedio de un alumno que tiene 7 calificaciones en la materia de Algoritmos

notas=0
for n in range(1,8):
    nota = float(input(f"Digite la nota {n}: "))
    notas = notas + nota
promedio = notas / 7
print(f"Promedio {promedio}")