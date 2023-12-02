# El Sena lo contrata a Ud., para elaborar un algoritmo que muestre el número de 
# soltero(a)s, casado(a)s, separado(a)s, viudo(a)s y en unión libre que tiene sus empleados a 
# nivel nacional, por regional y por centro de formación, si conoce que son 32 regionales y 
# cada regional tiene 8 centros de formación (cada centro tiene 10 empleados).

sumasolteros=0
sumacasados=0
sumaseparado=0
sumaviudo=0
sumaunionl=0

sumasolterosre=0
sumacasadosre=0
sumaseparadore=0
sumaviudore=0
sumaunionlre=0

sumasolterosce=0
sumacasadosce=0
sumaseparadoce=0
sumaviudoce=0
sumaunionlce=0
for regional in range(2):
    for centro in range(3):
        solteros=0
        casados=0
        separados=0
        viudos=0
        unionL=0
        print("Digite estado civil (Soltero, Casado, Separado, Viudo, Union libre): ")
        for empleados in range(4):
            estadoCivil=input("ingrese su estado civil: ")
            if estadoCivil == "soltero":
                solteros+=1
            elif estadoCivil == "casado":
                casados+=1
            elif estadoCivil == "separado":
                separados+=1
            elif estadoCivil == "viudo":
                viudos+=1
            elif estadoCivil == "union libre":
                unionL+=1
        print("El numero de empleados solteros es: ",solteros)
        print("El numero de empleados casados es: ",casados)
        print("El numero de empleados separados es: ",separados)
        print("El numero de empleados viudos es: ",viudos)
        print("El numero de empleados union libre es: ",unionL)
        print("\n")
        sumasolterosce=sumasolterosce+solteros
        sumacasadosce=sumacasadosce+casados
        sumaseparadoce=sumaseparadoce+separados
        sumaviudoce=sumaviudoce+viudos
        sumaunionlce=sumaunionlce+unionL
        solteros=0
        casados=0
        separados=0
        viudos=0
        unionL=0
        
    
    print("El numero de empleados solteros en el centro es: ",sumasolterosce)
    print("El numero de empleados casados en el centro es: ",sumacasadosce)
    print("El numero de empleados separados en el centro es: ",sumaseparadoce)
    print("El numero de empleados viudos en el centro es: ",sumaviudoce)
    print("El numero de empleados union libre en el centro es: ",sumaunionlce)
    print("\n") 
    sumasolterosre=sumasolterosre+sumasolterosce
    sumacasadosre=sumacasadosre+sumacasadosce
    sumaseparadore=sumaseparadore+sumaseparadoce
    sumaviudore=sumaviudore+sumaviudoce
    sumaunionlre=sumaunionlre+sumaunionlce    
    sumasolterosce=0
    sumacasadosce=0
    sumaseparadoce=0
    sumaviudoce=0
    sumaunionlce=0
    
print("El numero de empleados solteros en la regional es: ",sumasolterosre)
print("El numero de empleados casados en la regional es: ",sumacasadosre)
print("El numero de empleados separados en la regional es: ",sumaseparadore)
print("El numero de empleados viudos en la regional  es: ",sumaviudore)
print("El numero de empleados union libre en la regional es: ",sumaunionlre)
sumasolterosre=0
sumacasadosre=0
sumaseparadore=0
sumaviudore=0
sumaunionlre=0 