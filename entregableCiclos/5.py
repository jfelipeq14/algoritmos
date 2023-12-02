# En su empresa le solicitan que desarrolle un algoritmo que calcule el iva que pagaron
# durante el año sabiendo que se paga cada dos meses. (iva =valorfactura * 19%.). Cada
# factura tiene 4 productos.
totalIva = 0

for mes in range(2, 13, 2):
    totalFactura = 0
    sumaIva = 0
    
    for producto in range(4):
        valorProducto = int(input(f"Ingrese el valor del producto {producto+1}: "))
        totalFactura += valorProducto
        if producto==4 :
            producto=0 
        print(producto)
    sumaIva += totalFactura * 0.19
    totalIva += sumaIva

print("Total IVA:",totalIva)