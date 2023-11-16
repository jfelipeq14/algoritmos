# elabore un algoritmo que lea el sexo de 10 empleados y muestre cuantos son hombres y cuantos son mujeres.
hombres = 0
mujeres = 0

for i in range(10):
    sexo = input(f"Digite el sexo de la persona {i+1}: ")
    if sexo == "hombre":
        hombres = hombres + 1
    elif sexo == "mujer":
        mujeres = mujeres + 1

print(f"La cantidad de hombres es {hombres}")
print(f"La cantidad de mujeres es {mujeres}")
