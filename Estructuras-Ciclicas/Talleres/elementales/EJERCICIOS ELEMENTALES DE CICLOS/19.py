# 19.Una empresa tiene 3 facturas en un día. La primera factura tiene 4 artículos, la segunda factura tiene 5 artículos, la tercer factura tiene 3 artículos. Mostrar el valor de cada factura (cantidad * precio unitario), y valor facturado del día y el valor del descuento sabiendo que si la venta del día es menos a 2 millones tiene un descuento del 10%, si esta entre 2 millones y menor o igual a 5 millones será del 12% y mayores del 15%.

valorFactura1 = 0
valorFactura2 = 0
valorFactura3 = 0

for i in range(3):
    if i == 0:
        factura = 1
        productos = 4
    elif i == 1:
        factura = 2
        productos = 5
    elif i == 2:
        factura = 3
        productos = 3

    for i in range(productos):
        print(f"\n")
        print(f"Producto {i+1} de la factura {factura}")
        nombre = input(f"Digite el nombre del producto {i+1}: ")
        cantidad = int(input(f"Digite la cantidad de {nombre}: "))
        precio = int(input(f"Digite el precio de {nombre}: "))

        totalProducto = cantidad * precio

        if factura == 1:
            valorFactura1 = valorFactura1 + totalProducto
        elif factura == 2:
            valorFactura2 += totalProducto
        elif factura == 3:
            valorFactura3 += totalProducto

subtotal = valorFactura1 + valorFactura2 + valorFactura3

if subtotal < 2000000:
    descuento = subtotal * 0.10
elif subtotal >= 2000000 and subtotal <= 5000000:
    descuento = subtotal * 0.12
else:
    descuento = subtotal * 0.15

neto = subtotal - descuento

print(f"Factura 1: {valorFactura1}")
print(f"Factura 2: {valorFactura2}")
print(f"Factura 3: {valorFactura3}")
print(f"Dia: {subtotal}")
print(f"Descuento: {descuento}")
print(f"Neto: {neto}")
