# 4) Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig. Manera:
# Si trabaja 40 horas o menos se le paga $25 por hora
# Si trabaja más de 40 horas se le paga $25 por cada una de las primeras 40 horas y $30 por cada hora extra.

# DE: hT
# P: si (hT <= 40) => sS=hT*25
#     sino
#      si (hT > 40) => sS = (hT-40)*30 + 40*25
# DS: sS

# Entrada
hT = int(input("Digite la cantidad de horas trabajadas: "))

# Proceso
if hT <= 40:
    sS = hT*25
elif hT > 40:
    sS = (hT-40)*30 + 40*25

# Salida
print(sS)
