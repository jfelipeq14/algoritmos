# la empresa fredy style lo contrata para que elabore un algoritmo en python para que calcule el valor de una factura se sabe que cada factura tiene 3 articulos  si el valor de la factura es menor o igual que 500000 tiene un descuento del 10% si el valor de la factura es menor o igual a 1M tiene un descuento del 12% y si es mayor tiene un descuento del 15%

subtotal = 0

for i in range(3):
    nombreArticulo = input(f"Digite el nombre del articulo {i+1}: ")
    precioArticulo = int(input(f"Digite el precio del articulo {i+1}: "))
    cantidadArticulo = int(input(f"Digite la cantidad del articulo {i+1}: "))
    producto = cantidadArticulo * precioArticulo
    subtotal += producto

if subtotal <= 500000:
    descuento = subtotal * 0.10
elif subtotal <= 1000000:
    descuento = subtotal * 0.12
else:
    descuento = subtotal * 0.15

neto = subtotal - descuento

print(f"El subtotal es {subtotal}")
print(f"El descuento es {descuento}")
print(f"El neto es {neto}")