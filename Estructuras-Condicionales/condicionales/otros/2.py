# 2) Determinar si un alumno aprueba a reprueba un curso, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario.

calificacion1 = int(input("Digite la primera calificacion (de 1 a 100): "))
calificacion2 = int(input("Digite la segunda calificacion (de 1 a 100): "))
calificacion3 = int(input("Digite la tercera calificacion (de 1 a 100): "))

promedio = (calificacion1+calificacion2+calificacion3) / 3

if promedio >= 70:
    print('Aprueba')
else:
    print('Reprueba')
