# La Cía. Automovilística YOYO, S.A. Premia anualmente a sus mejores vendedores de acuerdo
# a la siguiente tabla:
# Si vendió Le corresponde de Comisión sobre facturas totales
# 10,000,000 < 3%
# 10,000,000 y MENOR A 50,000,000 4%
# 50,000,000 y MENOR A 70,000,000 5%
# 70,000,000 o MAS 6%
# Diseñar un algoritmo que lea las facturas de 100 vendedores y que escriba la comisión anual que le corresponda a cada vendedor. Suponga que vende 5 facturas por mes.

comisionesAnual=0

for empleado in range(1, 101):
    comisiones=0
    for mes in range(1, 13):
        comision=0
        facturas=0
        for factura in range(1, 6):
            preciofactura=int(input(f"Cuanto vendio en la factura {factura}: "))
            facturas += preciofactura

        if facturas < 10000000:
            comision = facturas * 0.03
        elif facturas >= 10000000 and facturas < 50000000:
            comision = facturas * 0.04
        elif facturas >= 50000000 and facturas < 70000000:
            comision = facturas * 0.05
        elif facturas >= 70000000:
            comision = facturas * 0.06
        comisiones += comision
        print("\n")
        
    comisionesAnual += comisiones
    print(f"Comisiones anuales: {comisionesAnual}")
    print("\n")