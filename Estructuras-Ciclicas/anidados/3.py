# 3. El Sena lo contrata a Ud., para elaborar un algoritmo que muestre el número de
# soltero(a)s, casado(a)s, separado(a)s, viudo(a)s y en unión libre que tiene sus
# empleados a nivel nacional, regional y por centro de formación, si conoce que son
# 32 regionales y cada regional tiene 8 centros de formación (cada centro tiene 10
# empleados).

#Acumuladores
totalSolteros = 0
totalCasados = 0
totalViudos = 0
totalUnionLibre = 0
totalSeparados = 0

solteros = 0
casados = 0
viudos = 0
unionLibre = 0
separados = 0

for regional in range(1, 33):
    for centroDeFormacion in range(1,9):
        for empleado in range(1, 11):
            estadoCivil = input(f"Digite el estado civil del empleado {empleado}").lower()

            if estadoCivil == "soltero":
                solteros += 1
            elif estadoCivil == "casado":
                casados += 1
            elif estadoCivil == "viudo":
                viudos += 1
            elif estadoCivil == "union libre":
                unionLibre += 1
            elif estadoCivil == "separado":
                separados += 1

            totalSolteros += solteros
            totalCasados += casados
            totalViudos += viudos
            totalUnionLibre += unionLibre
            totalSeparados += separados
