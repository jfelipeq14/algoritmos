# 5. En su empresa le solicitan que desarrolle un algoritmo que calcule el iva que
# pagaron durante el año sabiendo que se paga cada dos meses. (iva =valorfactura *
# 19%.). 

totaliva = 0
totalfactura = 0

for mes in range(6):
    valorfactura = float(input("Ingrese el valor de la factura: "))
    iva = valorfactura * 0.19
    totaliva = totaliva + iva
    totalfactura = totalfactura + valorfactura
print(f"El total de iva pagado es: {totaliva}")