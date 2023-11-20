# 7) Hacer un algoritmo que imprima el nombre de un artículo, clave, precio original y su precio con descuento. El descuento lo hace en base a la clave, si la clave es 01 el descuento es del 10% y si la clave es 02 el descuento en del 20% (solo existen dos claves).

#DE: nombreArticulo, claveArticulo, precioOriginal

#P: Si (claveArticulo == "01") => descuento = 0.10
#    Sino
#     Si (claveArticulo == "02") => descuento = 0.20
# descuento = precioOriginal * descuento
# precioDescuento = precioOriginal - descuento

#DS: nombreArticulo, claveArticulo, precioOriginal, precioDescuento

nombreArticulo = input("Digite el nombre del articulo: ")
claveArticulo = input("Digite la clave del articulo: ")
precioOriginal = int(input("Digite el precio del articulo: "))

if claveArticulo == "01":
    descuento = 0.10
elif claveArticulo == "02":
    descuento = 0.20

descuento = precioOriginal * descuento
precioDescuento = precioOriginal - descuento

print("\n")
print(nombreArticulo)
print(claveArticulo)
print(precioOriginal)
print(precioDescuento)