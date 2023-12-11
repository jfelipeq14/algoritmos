# 9) Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de refacciones. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagara solicitando un crédito al fabricante. Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagara solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.

# DE: cantidadPiezas, valorPiezas

# P: totalCompra = cantidadPiezas * valorPiezas
# si (totalCompra > 500000) => porcentajePropio=0.55, banco = totalCompra * 0.30, porcentajeFabricante=0.15
#   sino
#    si (totalCompra <= 500000) => porcentajePropio=0.70, porcentajeFabricante=0.30
# Fin si

# propio = totalCompra * propio
# fabricante = totalCompra * fabricante
# totalCredito = fabricante + (fabricante * 0.20)

# DS: totalCredito

# entradas

# pedir valores al usuario
cantidadPiezas = int(input("Digite la cantidad de piezas: "))
valorPiezas = int(input("Digite el valor de cada pieza: "))

# proceso

# obtener el valor de la compra
totalCompra = cantidadPiezas * valorPiezas

# validar el valor de la compra
if totalCompra > 500000:
    # asignar porcentajes
    porcentajePropio = 0.55
    banco = totalCompra * 0.30
    porcentajeFabricante = 0.15
elif totalCompra <= 500000:
    # asignar porcentajes
    porcentajePropio = 0.70
    porcentajeFabricante = 0.30

# valores de pago
propio = totalCompra * porcentajePropio
fabricante = totalCompra * porcentajeFabricante

# credito del fabricante
totalCredito = fabricante + (fabricante * 0.20)

# salida
print(totalCredito)
