# la empresa fredy styles lo contrata para que mire cauntos solteros, cuantos casados, cuantos viudos, cuantos en union libre y cuantos separados tiene la empresa sabiendo que cuenta con 10 empleados.

solteros = 0
casados = 0
viudos = 0
unionLibre = 0
separados = 0

for i in range(10):
    estadoCivil = input(f"Digite el estado civil del empleado {i+1}")

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

print(f"La cantidad de solteros es {solteros}")
print(f"La cantidad de casados es {casados}")
print(f"La cantidad de viudos es {viudos}")
print(f"La cantidad de union libre es {unionLibre}")
print(f"La cantidad de separados es {separados}")