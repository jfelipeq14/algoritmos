# En su proyecto formativo se pide que calcule las comisiones de cada uno de los
# vendedores de la empresa y el total de comisiones. Se conoce que la empresa tiene 6
# vendedores y cada vendedor trae las facturas(5) del mes que vendió.

porcentajeComision = float(input("Ingrese el porcentaje de la comision : "))
totalComision=0

for vendedor in range (1, 7) :
    totalFactVendedor=0

    for factura in range (1, 6) :
        valorFactura= int(input("Ingrese el valor de la factura: "))
        totalFactVendedor+=valorFactura

    comisionVendedor=(totalFactVendedor*porcentajeComision)/100

    totalComision += comisionVendedor

    print("Comision para vendedor No. ", vendedor+1, " es igual a ", comisionVendedor)

print("Total comisiones : ",totalComision)