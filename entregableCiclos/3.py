# El Sena lo contrata a Ud., para elaborar un algoritmo que muestre el número de 
# soltero(a)s, casado(a)s, separado(a)s, viudo(a)s y en unión libre que tiene sus empleados a 
# nivel nacional, por regional y por centro de formación, si conoce que son 32 regionales y 
# cada regional tiene 8 centros de formación (cada centro tiene 10 empleados).

totalSoltero =0
totalCasados=0
TotalSeparados=0
totalViudos=0
TotalUnionLibre=0

for regional in range (1,33):
    totalSolterosregional=0
    totalCasadosregional=0
    totalSeparadosegional=0
    totalViduosregional=0
    totalUnionlibreregional=0

    for centro in range (1,9):  
        totalsolteroscentro =0
        totalcasadoscentro =0
        totalseparadoscentro =0
        totalviudoscentro =0
        totalunionlibrecentro =0

        for empleados in range (1,11):
            estadocivil =input(f"ingrese el estado civil del empleado {empleados}: ")
            
            if estadocivil == 'soltero':
                totalSoltero +=1
                totalSolterosregional +=1
                totalsolteroscentro +=1
            elif estadocivil == 'casados':
                totalCasados +=1
                totalCasadosregional+=1
                totalcasadoscentro +=1
            elif estadocivil == 'separados':
                TotalSeparados +=1
                totalSeparadosegional +=1
                totalseparadoscentro +=1
            elif estadocivil == 'viudo':
                totalViudos +=1
                totalViduosregional +=1
                totalviudoscentro +=1
            elif estadocivil == 'union libre':
                TotalUnionLibre +=1
                totalUnionlibreregional +=1
                totalunionlibrecentro +=1
               

print(f"el numero de solteros regionales es {totalSolterosregional} y total del solteros en los centros  son{ totalsolteroscentro} y el total de los solteros son {totalSoltero}")
print(f"el numero de casados regionales es {totalCasadosregional} y total del casados en los centros son{ totalcasadoscentro} y el total de los casados son {totalCasados}")
print(f"el numero de separados regionales es {totalSeparadosegional} y total del separados en los centros son{ totalseparadoscentro} y el total de los separados son {TotalSeparados}")
print(f"el numero de viudos regionales es {totalViduosregional} y total del viudos en los centros son { totalviudoscentro} y el total de los viudos son {totalViudos}")
print(f"el numero de union libre regionales es {totalUnionlibreregional} y total del union libre en los centros son { totalunionlibrecentro} y el total de los union libre son {TotalUnionLibre}") 