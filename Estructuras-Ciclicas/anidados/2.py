# 2. El supermercado “Todo hay” lo contrata a Ud. joven aprendiz para realizar un
# algoritmo que calcule las ventas anuales, ventas semestrales y mensuales de la
# empresa. Cada mes se generan 30 facturas y cada factura (cantidad * precio
# unitario) tiene 5 artículos.

x=0

anuales = 0
semestrales = 0
mensuales = 0

for anuales in range(x):
    for semestrales in range(1,3):
        for mes in range(1, 7):
            for facturas in range(1, 31):
                for productos in range(1, 6):
                    nombre = input(f"Digite el nombre del producto #{productos}: ")
                    cantidad = int(input(f"Digite la cantidad de {nombre}: "))
                    precio = int(input(f"Digite el precio de {nombre}: "))
                    totalProducto = cantidad * precio
                    