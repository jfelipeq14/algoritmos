# La empresa “salome style” lo contrata para que muestre la facturación de un día sabiendo que en
# el día hay 2 facturas y cada factura tiene 2 productos (cantidad y valor). Cada factura tiene un
# descuento dependiendo del valor de dicha factura. Si la factura es menor o igual a 50.000 tiene un
# descuento del 3%, si la factura es menor o igual a 100.000 tiene un descuento del 5% y si es mayor
# el descuento es del 9%.

dia = 0
subtotal = 0

for factura in range(1, 3):

    for producto in range(1, 3):
        precio = int(input(f"Digite el precio del producto {producto}: "))
        cantidad = int(input(f"Digite la cantidad del producto {producto}: "))
        valorProducto = precio*cantidad
        subtotal += valorProducto

    if subtotal <= 50000:
        descuento = subtotal * 0.03
    elif subtotal <= 100000:
        descuento = subtotal * 0.05
    elif subtotal > 100000:
        descuento = subtotal * 0.09
        
    neto = subtotal - descuento
    dia += neto
    print()
    print(f"Valor factura: {subtotal}")
    print(f"Valor descuento: {descuento}")
    print(f"Valor neto: {neto}")
    print(f"Valor dia: {dia}")
    print()
    subtotal = 0

#Completed