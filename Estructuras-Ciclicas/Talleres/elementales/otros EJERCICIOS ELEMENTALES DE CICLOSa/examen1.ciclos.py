# “Salome Lujos” tiene clasificados a sus clientes: Tipo A (bono de10.000), tipo B
# (bono de 15.000), tipo C (bono de 20.000), Tipo D (bono de 25.000), tipo E (bono
# de 30.000). La empresa “John Sadder Styls” quiere hacer una compra de 5 piezas
# deferentes a una fábrica de refacciones “Salome Lujos”. La empresa, dependiendo
# del monto total de la compra (costo * nropiezas - bono), decidirá qué hacer para
# pagar al fabricante. Si el monto total de la compra excede de $500 000 la empresa
# tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra,
# pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al
# fabricante. Si el monto total de la compra no excede de $500 000 la empresa tendrá
# capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará
# solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un
# 20% sobre la cantidad que se le pague a crédito.

monto = 0

tipoCliente = input("Ingrese el tipo de cliente: ")

if tipoCliente == "A":
    bono = 10000
elif tipoCliente == "B":
    bono = 15000
elif tipoCliente == "C":
    bono = 20000
elif tipoCliente == "D":
    bono = 25000
elif tipoCliente == "E":
    bono = 30000
else:
    bono = 0

for i in range(5):
    cantidadPieza = int(input(f"Ingrese la cantidad de piezas {i+1}: "))
    costoPieza = int(input(f"Ingrese el costo de la pieza {i+1}: "))

    valorPieza = costoPieza * cantidadPieza
    monto += valorPieza

neto = monto - bono

if neto > 500000:
    inversion = neto * 0.55
    prestamo = neto * 0.30
    credito = neto * 0.15
else:
    inversion = neto * 0.70
    credito = neto * 0.30
    prestamo = 0

interes = credito * 0.20
totalCredito = credito + interes

print(f"El monto total de la compra es: {monto}")
print(f"El monto del bono es: {bono}")
print(f"El monto neto de la compra es: {neto}")
print(f"El monto de la inversion es: {inversion}")
print(f"El monto del prestamo es: {prestamo}")
print(f"El monto del credito es: {credito}")
print(f"El monto del interes es: {interes}")
print(f"El monto total del credito es: {totalCredito}")