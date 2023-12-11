# 2. El supermercado “Todo hay” lo contrata a Ud. joven aprendiz para realizar un
# algoritmo que calcule las ventas anuales, ventas semestrales y mensuales de la
# empresa. Cada mes se generan 30 facturas y cada factura (cantidad * precio
# unitario) tiene 5 artículos.

# Variables a usar
totalVentasAnuales = 0
totalVentasSemestrales = 0
totalVentasMensuales = 0

# Ciclo para recorrer los meses
for mes in range(1, 13):
    # Variables a usar
    totalVentasMes = 0
    totalVentasSemestre = 0
    totalVentasAnual = 0

    # Ciclo para recorrer las facturas
    for factura in range(1, 31):
        # Variables a usar
        totalFactura = 0

        # Ciclo para recorrer los articulos
        for articulo in range(1, 6):
            # Variables a usar
            nombreArticulo = input(
                f"Digite el nombre del articulo {articulo}: ")
            precioArticulo = int(
                input(f"Digite el precio de {nombreArticulo}: "))
            cantidadArticulo = int(
                input(f"Digite la cantidad de {nombreArticulo}: "))
            totalArticulo = precioArticulo*cantidadArticulo
            totalFactura += totalArticulo

        totalVentasMes += totalFactura
        totalVentasSemestre += totalFactura
        totalVentasAnual += totalFactura

    totalVentasMensuales += totalVentasMes
    totalVentasSemestrales += totalVentasSemestre
    totalVentasAnuales += totalVentasAnual

    print(f"Total de ventas del mes {mes}: {totalVentasMes}")
    print(f"Total de ventas del semestre {mes}: {totalVentasSemestre}")
    print(f"Total de ventas del año {mes}: {totalVentasAnual}")
