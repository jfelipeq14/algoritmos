# 1) Un hombre desea saber cuánto dinero se genera por concepto de intereses sobre la cantidad que tiene en inversión en el banco. El decidirá reinvertir los intereses siempre y cuando estos excedan a $700000, y en ese caso desea saber cuánto dinero tendrá finalmente en su cuenta.

dineroEnElBanco = int(
    input("Digite la cantidad de dinero que tiene en el banco: "))
interesMensual = int(input("Digite el interes mensual: ")) / 100

interes = dineroEnElBanco * interesMensual
total = dineroEnElBanco + interes

if interes > 700000:
    reinvertir = total + interes
    print(reinvertir)
else:
    print(total)
