# 4) Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. Manera:
#Si trabaja 40 horas o menos se le paga $25 por hora
#Si trabaja más de 40 horas se le paga $25 por cada una de las primeras 40 horas y $30 por cada hora extra.

#declarar variable: cantidadHoras (pedirle al ususario la cantidad de hooras que trabajo)
#nombre Variable: cantidadHoras
# asignacion (=)
# tipo de dato a recibir (int:entero) - para que el dato sea un numero
# indicar que es una entrada (input)
cantidadHoras = int(input("Digite la cantidad de horas que trabajo: "))

# empezar a validar - condicion
# si x cosa se cumple entonces haga lo siguiente
# if (si)
# variable a validar (cantidaHoras)
# operador (<= menor o igual)
# lo que debe cumplir la variable con base al operador
if cantidadHoras <= 40:
    salarioSemanal = cantidadHoras * 25
elif cantidadHoras > 40:
    salarioSemanal = ((cantidadHoras - 40) * 30) + (40 * 25)

print(f"Trabajo {cantidadHoras} horas")
print(f"El salario es de {salarioSemanal}")