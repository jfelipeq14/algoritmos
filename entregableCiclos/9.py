# Una empresa dedica gran parte de su tiempo a saber cuántos: mujeres hay, hombres
# solteros con un hijo, hombres solteros con más de un hijo, hombres casados sin hijos,
# hombres casados con más de 2 hijos, hombres viudos con más de 2 hijos, mujeres solteras
# con dos hijos, mujeres viudas sin hijos, mujeres divorciadas sin hijos. Sabemos que en la
# empresa hay 20 empleados, para cada una de las 3 sucursales. 

for sucursales in range(1, 4):
    for empleados in range(1, 21):
        sexo=input(f"Digite el sexo del empleado {empleados}: ")
        estadoCivil=input(f"Digite el estado civil del empleado {empleados}: ")
        cantidadHijos = int(input(f"Digite la cantidad de hijos del empleado {empleados}: "))

        
