#1. La empresa “Salome lujos” lo contrata para hacer un algoritmo que imprima el total de facturación de un día. Sabiendo que cada día se hacen 3 facturas y cada  factura tiene 2 artículos, la factura debe tener el nombre del artículo, precio y su cantidad. El descuento se basa en una balota (la factura tiene un solo descuento), si la balota es blanca es del 10%, si la balota es azul del 12%, si la balota es roja del 14%, si la balota es verde del 16%, si la balota es rosa es del 18%.

# variables (contadores, acumuladores)
subTotal = 0
valorFactura = 0
valorDia = 0
# for de las 3 facturas para pedir los producto
for factura in range(1,4):
    #for para los productos, que en este caso son 2
    for producto in range(1, 3):
        nombreArticulo=input(f"Digite el nombre del articulo {producto}: ")
        precioArticulo=int(input(f"Digite el precio de {nombreArticulo}: "))
        cantidadArticulo=int(input(f"Digite la cantidad de {nombreArticulo}: "))
        #sacar el total de cada uno de los productos
        totalArticulo = precioArticulo*cantidadArticulo
        #acumular los productos en el subtotal de la factura
        subTotal += totalArticulo

    balota=input("Digite el color de la balota (blanca, azul, roja, verde, rosa): ").lower()

    # validar la balota para el descuento    
    if balota == "blanca":
        descuento = subTotal * 0.10
    elif balota == "azul":
        descuento = subTotal * 0.12
    elif balota == "roja":
        descuento = subTotal * 0.14
    elif balota == "verde":
        descuento = subTotal * 0.16
    elif balota == "rosa":
        descuento = subTotal * 0.18

    # sacar el valor total de la factura con su respectivo descuento
    valorFactura = subTotal - descuento
    #mostrar la factura
    print(f"Valor de la factura: {valorFactura}")
    #acumular el valor de las facturas
    valorDia += valorFactura
    #reinicializar las variablse para sacar otra facturas
    valorFactura = 0
    subTotal = 0
#mostrar el valor total del dia
print(f"Valor del dia: {valorDia}")