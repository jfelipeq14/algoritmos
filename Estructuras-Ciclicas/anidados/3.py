# 3. El Sena lo contrata a Ud., para elaborar un algoritmo que muestre el número de
# soltero(a)s, casado(a)s, separado(a)s, viudo(a)s y en unión libre que tiene sus
# empleados a nivel nacional, regional y por centro de formación, si conoce que son
# 32 regionales y cada regional tiene 8 centros de formación (cada centro tiene 10
# empleados).

# Variables a usar
totalSolteros = 0
totalCasados = 0
totalSeparados = 0
totalViudos = 0
totalUnionLibre = 0

# Ciclo para recorrer las regionales
for regional in range(1, 33):
    # Variables a usar
    totalSolterosRegional = 0
    totalCasadosRegional = 0
    totalSeparadosRegional = 0
    totalViudosRegional = 0
    totalUnionLibreRegional = 0

    # Ciclo para recorrer los centros de formacion
    for centro in range(1, 9):
        # Variables a usar
        totalSolterosCentro = 0
        totalCasadosCentro = 0
        totalSeparadosCentro = 0
        totalViudosCentro = 0
        totalUnionLibreCentro = 0

        # Ciclo para recorrer los empleados
        for empleado in range(1, 11):
            # Variables a usar
            estadoCivil = input(f"Digite el estado civil del empleado {empleado}: ").lower()

            if estadoCivil == "soltero":
                totalSolteros += 1
                totalSolterosRegional += 1
                totalSolterosCentro += 1
            elif estadoCivil == "casado":
                totalCasados += 1
                totalCasadosRegional += 1
                totalCasadosCentro += 1
            elif estadoCivil == "separado":
                totalSeparados += 1
                totalSeparadosRegional += 1
                totalSeparadosCentro += 1
            elif estadoCivil == "viudo":
                totalViudos += 1
                totalViudosRegional += 1
                totalViudosCentro += 1
            elif estadoCivil == "union libre":
                totalUnionLibre += 1
                totalUnionLibreRegional += 1
                totalUnionLibreCentro += 1
        print(f"Total de solteros del centro {centro}: {totalSolterosCentro}")
        print(f"Total de casados del centro {centro}: {totalCasadosCentro}")
        print(f"Total de separados del centro {centro}: {totalSeparadosCentro}")
        print(f"Total de viudos del centro {centro}: {totalViudosCentro}")
        print(f"Total de union libre del centro {centro}: {totalUnionLibreCentro}")
    print(f"Total de solteros de la regional {regional}: {totalSolterosRegional}")