# 20.Una empresa dedica gran parte de su tiempo a saber cuántos: mujeres hay,
# hombres solteros con un hijo, hombres solteros con más de un hijo, hombres
# casados sin hijos, hombres casados con más de 2 hijos, hombres viudos con
# más de 2 hijos, mujeres solteras con dos hijos, mujeres viudas sin hijos,
# mujeres divorciadas sin hijos. Sabemos que en la empresa hay 99 empleados.

hombresSolterosCon1Hijo = 0
hombresSolterosConMasDe1Hijo = 0
hombresCasadosSinHijos = 0
hombresCasadosConMasDe2Hijos = 0
hombresViudosConMasDe2Hijos = 0
mujeresSolterasConDosHijos = 0
mujeresViudasSinHijos = 0

for i in range(99):
    sexo = input(f"Digite el sexo del empleado {i+1}")
    estadoCivil = input(f"Digite el estado civil del empleado {i+1}")
    hijos = int(input(f"Digite la cantidad de hijos del empleado {i+1}"))

    if sexo == "hombre" and estadoCivil == "soltero" and hijos == 1:
        hombresSolterosCon1Hijo += 1

    elif sexo == "hombre" and estadoCivil == "soltero" and hijos > 1:
        hombresSolterosConMasDe1Hijo += 1

    elif sexo == "hombre" and estadoCivil == "casado" and hijos <= 0:
        hombresCasadosSinHijos += 1

    elif sexo == "hombre" and estadoCivil == "casado" and hijos > 2:
        hombresCasadosConMasDe2Hijos += 1

    elif sexo == "hombre" and estadoCivil == "viudo" and hijos > 2:
        hombresViudosConMasDe2Hijos += 1

    elif sexo == "mujer" and estadoCivil == "soltera" and hijos == 2:
        mujeresSolterasConDosHijos += 1

    elif sexo == "mujer" and estadoCivil == "viuda" and hijos == 2:
        mujeresViudasSinHijos += 1