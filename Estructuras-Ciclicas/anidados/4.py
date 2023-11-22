# 4. En su proyecto formativo se pide que calcule las comisiones de cada uno de los
# vendedores de la empresa y el total de comisiones. Se conoce que la empresa
# tiene 6 vendedores y cada vendedor trae las facturas(3) del mes que vendió.

# Variables a usar
totalComisiones = 0

# Ciclo para recorrer los vendedores
for vendedor in range(1, 7):
    # Variables a usar
    totalComisionesVendedor = 0

    # Ciclo para recorrer las facturas
    for factura in range(1, 4):
        # Variables a usar
        valorFactura = float(input(f"Digite el valor de la factura {factura}: "))
        comision = valorFactura*0.10
        totalComisionesVendedor += comision
        totalComisiones += comision
    print(f"Total de comisiones del vendedor {vendedor}: {totalComisionesVendedor}")
print(f"Total de comisiones: {totalComisiones}")
