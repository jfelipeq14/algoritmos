# El supermercado “Todo hay” lo contrata a Ud. joven aprendiz para realizar un algoritmo
# que calcule las ventas anuales, ventas semestrales y mensuales de la empresa. Cada mes
# se generan 5 facturas y cada factura (cantidad * precio unitario) tiene 5 artículos.
subtotal = 0
factura = 0
mes = 0

for mes in range(1, 13):
    for factura in range(1, 6):
        for producto in range(1, 5):
            precio = int(input(f"Digite el precio del producto {producto}: "))
            cantidad = int(input(f"Digite la cantidad del producto {producto}: "))
            valorProducto = precio * cantidad
            subtotal += valorProducto
            