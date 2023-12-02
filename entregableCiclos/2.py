# El supermercado “Todo hay” lo contrata a Ud. joven aprendiz para realizar un algoritmo
# que calcule las ventas anuales, ventas semestrales y mensuales de la empresa. Cada mes
# se generan 5 facturas y cada factura (cantidad * precio unitario) tiene 5 artículos.

subtotal = 0
facturas=0
meses=0
semestral=0
anuales=0

for semestre in range(0, 12, 6):

    for mes in range(1, 13):

        for factura in range(1, 6):

            for producto in range(1, 6):
                precio=int(input(f"Digite el precio del producto {producto}: "))
                cantidad=int(input(f"Digite la cantidad del producto {producto}: "))
                valorProducto = cantidad * precio
                subtotal += valorProducto
                facturas += subtotal
                print(f"producto {producto}")
                print(f"subtotal {subtotal}")
                print(f"factura {facturas}")
                print()
                subtotal = 0
            mes += facturas
            print(f"mes {mes}")
            print()
            facturas = 0
        semestre += mes
        print(f"semestre {semestre}")
        print()
        mes = 0
    anuales += semestre
    print(f"anuales {anuales}")
    print()
    semestre = 0