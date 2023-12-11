# Una empresa dedica gran parte de su tiempo a saber cuántos: mujeres hay, hombres
# solteros con un hijo, hombres solteros con más de un hijo, hombres casados sin hijos,
# hombres casados con más de 2 hijos, hombres viudos con más de 2 hijos, mujeres solteras
# con dos hijos, mujeres viudas sin hijos, mujeres divorciadas sin hijos. Sabemos que en la
# empresa hay 20 empleados, para cada una de las 3 sucursales.

mujeres=0
hombresSolterosConUnHijo=0
hombresSolterosConMasDeUnHijo=0
hombreCasadosSinHijos=0
hombresCasadosConMasDeDosHijos=0
hombresViudosConMasDeDosHijos=0
mujeresSolterasConDosHijos=0
mujeresViudasSinHijos=0
mujeresDivorciadasSinHijos=0

for sucursales in range(1, 4):
    for empleados in range(1, 21):
        sexo=input(f"Digite el sexo del empleado {empleados}: ")
        estadoCivil=input(f"Digite el estado civil del empleado {empleados}: ")
        cantidadHijos = int(input(f"Digite la cantidad de hijos del empleado {empleados}: "))
        
        if sexo == "mujer":
            mujeres+=1

        elif sexo == "hombre" and estadoCivil == "soltero" and cantidadHijos == 1:
            hombresSolterosConUnHijo+=1

        elif sexo == "hombre" and estadoCivil == "soltero" and cantidadHijos > 1:
            hombresSolterosConMasDeUnHijo+=1

        elif sexo == "hombre" and estadoCivil == "casado" and cantidadHijos == 0:
            hombreCasadosSinHijos+=1

        elif sexo == "hombre" and estadoCivil == "casado" and cantidadHijos > 2:
            hombresCasadosConMasDeDosHijos+=1

        elif sexo == "hombre" and estadoCivil == "viudo" and cantidadHijos > 2:
            hombresViudosConMasDeDosHijos+=1

        elif sexo == "mujer" and estadoCivil == "soltera" and cantidadHijos == 2:
            mujeres+=1
            mujeresSolterasConDosHijos+=1

        elif sexo == "mujer" and estadoCivil == "viuda" and cantidadHijos == 0:
            mujeres+=1
            mujeresViudasSinHijos+=1

        elif sexo == "mujer" and estadoCivil == "divorciada" and cantidadHijos == 0:
            mujeres+=1
            mujeresDivorciadasSinHijos+=1

print(f"cantidad de mujeres: {mujeres}")
print(f"cantidad de hombresSolterosConUnHijo: {hombresSolterosConUnHijo}")
print(f"cantidad de hombresSolterosConMasDeUnHijo: {hombresSolterosConMasDeUnHijo}")
print(f"cantidad de hombreCasadosSinHijos: {hombreCasadosSinHijos}")
print(f"cantidad de hombresCasadosConMasDeDosHijos: {hombresCasadosConMasDeDosHijos}")
print(f"cantidad de hombresViudosConMasDeDosHijos: {hombresViudosConMasDeDosHijos}")
print(f"cantidad de mujeresSolterasConDosHijos: {mujeresSolterasConDosHijos}")
print(f"cantidad de mujeresViudasSinHijos: {mujeresViudasSinHijos}")
print(f"cantidad de mujeresDivorciadasSinHijos: {mujeresDivorciadasSinHijos}")