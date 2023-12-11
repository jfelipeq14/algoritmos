# Pedir al usuario un día de la semana. Si el día es lunes o martes, imprimir "Es día laborable". Si el día es miércoles, jueves, viernes o sábado, imprimir "Es día entre semana". Si el día es domingo, imprimir "Es fin de semana".

print("Seleccion un dia de la semana")
print("1 => Lunes")
print("2 => Martes")
print("3 => Miercoles")
print("4 => Jueves")
print("5 => Viernes")
print("6 => Sabado")
print("7 => Domingo")

diaDeLaSemana = int(input("Ingrese un dia de la semana: "))

if diaDeLaSemana == 1 or diaDeLaSemana == 2:
    print("Es día laborable")
elif diaDeLaSemana == 3 or diaDeLaSemana == 4 or diaDeLaSemana == 5 or diaDeLaSemana == 6:
    print("Es día entre semana")
elif diaDeLaSemana == 7:
    print("En fin de semana")
else:
    print("Digite un numero entre 1-7")
