# Calcular el promedio de las notas (3 notas) de ALGORITMOS de los 17 alumnos y mostrar
# un mensaje por cada alumno si aprobó o reprobó la clase (se gana con 3,5 o mas).
calificaciones=0
for alumno in range(1, 18):
    print(f"Alumno {alumno}")
    for notas in range(1, 4):
        nota=float(input(f"Digite la nota {notas}: "))
        calificaciones += nota
    totalCalificaciones = calificaciones / 3
    print(f"Nota final: {totalCalificaciones}")
    if totalCalificaciones < 3.5:
        print(f"Uy no. Mejor cancele! ")
        print("\n")
    else:
        print(f"Excelente. Goleador!")
        print("\n")
    calificaciones = 0