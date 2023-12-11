# Solome lujos tiene clasificados a sus clientes: Tipo A (Bono de 10.000), Tipo B (Bono de 15.000), Tipo C (Bono de 20.000), Tipo D (Bono de 25.000), Tipo E (Bono de 30.000). La empresa John Sadder Styls quiere hacer una compra de varias piezas de la misma clase a una fabrica de refacciones Salome Lujos. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede de $500 000 la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagara solicitando un crédito al fabricante. Si el monto total de la compra no excede de $500 000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagara solicitando crédito al fabricante. El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito. 

cantidadPiezas = int(input("Digite la cantidad de piezas a comprar: ")) # 4320 
precioPieza = int(input("Digite el precio de la pieza: ")) # 1002
tipoCliente = input("Digite el tipo de cliente: ") # d

subtotal = cantidadPiezas * precioPieza

dineroPropio = 0
dineroBanco = 0
dineroFabricante = 0
bono = 0

if tipoCliente == "a":
    bono = 10000
elif tipoCliente == "b":
    bono = 15000
elif tipoCliente == "c":
    bono = 20000
elif tipoCliente == "d":
    bono = 25000
elif tipoCliente == "e":
    bono = 30000

neto = subtotal - bono

if neto > 500000:
    dineroPropio = neto * 0.55
    dineroBanco = neto * 0.30
    dineroFabricante = neto * 0.15
elif neto <= 500000:
    dineroPropio = neto * 0.70
    dineroFabricante = neto * 0.30

intereses = dineroFabricante * 0.20
credito = dineroFabricante + intereses

print("\n")
print(f"El subtotal es: ${subtotal}")
print(f"El bono es: ${bono}")
print(f"El neto es: ${neto}")
print(f"El dinero propio a invertir es: ${dineroPropio}")
print(f"El dinero del banco para el prestamo es: ${dineroBanco}")
print(f"El dinero del fabricante para el credito es: ${dineroFabricante}")
print(f"El interes del fabricante (20%) es: ${intereses}")
print(f"El dinero del credito al fabricante es: ${credito}")