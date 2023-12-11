# Una empresa dedica gran parte de su tiempo a saber cuantos: Solteros hay, cuantos casados, cuantos viudos, cuantos unión libre y cuantos separados sabiendo que son 100 empleados.

solteros=0
casados=0
viudos=0
unionLibre=0
separados=0
for empleado in range(1, 101):
    estadoCivil=input(f"Digite el estado civil del empleado {empleado}: ")
    if estadoCivil == "soltero":
        solteros+=1
    elif estadoCivil == "casado":
        casados+=1
    elif estadoCivil == "viudo":
        viudos+=1
    elif estadoCivil == "union libre":
        unionLibre+=1
    elif estadoCivil == "separado":
        separados+=1
print(f"La cantidad de solteros es: {solteros}")
print(f"La cantidad de casados es: {casados}")
print(f"La cantidad de viudos es: {viudos}")
print(f"La cantidad de unionLibre es: {unionLibre}")
print(f"La cantidad de separados es: {separados}")