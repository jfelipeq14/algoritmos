# 4. En su proyecto formativo se pide que calcule las comisiones de cada uno de los
# vendedores de la empresa y el total de comisiones. Se conoce que la empresa
# tiene 6 vendedores y cada vendedor trae las facturas(3) del mes que vendió.

for vendedores in range(1, 7):
    for factura in range(1, 4):
        valorFactura = int(input(f"Digite el valor de la factura {factura}"))
        