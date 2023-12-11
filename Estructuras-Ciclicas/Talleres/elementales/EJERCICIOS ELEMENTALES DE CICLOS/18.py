# 18.Una empresa dedica gran parte de su tiempo a saber cuantos: Solteros hay, cuantos casados, cuantos viudos, cuantos en unión libre y cuantos separados sabiendo que son 100 empleados.
solteros = 0
casados = 0
viudos = 0
unionLibre = 0
separados = 0
empleados = 0

for i in range(100):
    estadoCivil = input(f"Digite el estado civil del empleado {i+1}: ")

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
    else:
        print(f"¿Usted no sabe escribir? vea lo que puso: {estadoCivil}")
        break
print("\n")
print(f"solteros: {solteros}")
print(f"casados: {casados}")
print(f"viudos: {viudos}")
print(f"union libre: {unionLibre}")
print(f"separados: {separados}")
