# algoritmo que cuente el numero de casados, de separados, de viudos, solteros, union libre. sabiendo que en Medellin hay 20 personas, en Bello hay 15 personas y en Itagui 12 personas. Adicionalmente por cada municipio se quiere saber esta misma informacion.

#Contadores
solteros = 0
casados = 0
viudos = 0
unionLibre = 0
separados = 0

#Acumuladores
totalSolteros = 0
totalCasados = 0
totalViudos = 0
totalUnionLibre = 0
totalSeparados = 0

for medellin in range(20):
    estadoCivil = input(f"Digite el estado civil del empleado {medellin+1}: ")

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

#Contadores
solteros = 0
casados = 0
viudos = 0
unionLibre = 0
separados = 0

for bello in range(15):
    estadoCivil = input(f"Digite el estado civil del empleado {bello+1}: ")

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

#Contadores
solteros = 0
casados = 0
viudos = 0
unionLibre = 0
separados = 0

for itagui in range(12):
    estadoCivil = input(f"Digite el estado civil del empleado {itagui+1}: ")

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