# La Cía. Automovilística YOYO, S.A. Premia anualmente a sus mejores vendedores de acuerdo
# a la siguiente tabla:
# Si vendió Le corresponde de Comisión sobre ventas totales
# 10,000,000 < 3%
# 10,000,000 y MENOR A 50,000,000 4%
# 50,000,000 y MENOR A 70,000,000 5%
# 70,000,000 o MAS 6%

ventas=0

empleados = int(input("¿Cuantos empleados hay?: "))
for empleado in range(empleados):
    vendio = int(input(f"¿Cuantas ventas hizo el empleado {empleado+1}?: "))
    for venta in range(vendio):
        precioVenta=int(input(f"Cuanto vendio en la venta {venta+1}: "))
        ventas += precioVenta

    if ventas < 10000000:
        comision = ventas * 0.03
    elif ventas >= 10000000 and ventas < 50000000:
        comision = ventas * 0.04
    elif ventas >= 50000000 and ventas < 70000000:
        comision = ventas * 0.05
    elif ventas >= 70000000:
        comision = ventas * 0.06

    print(f"La comision del empleado {empleado+1}: {comision}")