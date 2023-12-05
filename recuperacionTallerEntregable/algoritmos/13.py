# 13. La empresa Coca-Cola lo contrata para que elabore un algoritmo que muestre las
# ventas mensuales de cada una de las 5 sucursales que tiene en la ciudad de medellin.
# Se sabe que cada sucursal tiene 6 secciones y cada sección tiene 12 vendedores y que
# cada vendedor entrega 12 facturas y cada factura tiene 4 productos. (cantidad * valor)

totalf=0
for sucursal in range(1, 6):
    for seccion in range(1, 7):
        for vendedores in range(1, 13):
            for facturas in range(1, 13):
                valorf=0
                for productos in range(1, 5):
                    precio=int(input(f"Digite el precio del producto {productos} de la factura {facturas}: "))
                    cantidad=int(input(f"Digite la cantidad del producto {productos} de la factura {facturas}: "))
                    valorp=cantidad*precio
                    valorf=valorf+valorp
                totalf=totalf+valorf
print("El total de facturas mensuales es de: " , totalf)