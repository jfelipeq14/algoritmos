#  Escriba un programa que pregunte al usuario el valor de un producto y, en función de su valorproducto, le aplique el siguiente descuento:

# Si el valorproducto es inferior a 10 euros, el descuento es del 10 %.
# Si el valorproducto es igual o superior a 10 euros y menor que 100 euros, el descuento es del 5 %.
# Si el valorproducto es igual o superior a 100 euros, el descuento es del 2 %.

#  Analisis:
#  Entrada => ValorProducto
#  Proceso => Validacion para los descuentos
#  Salida => Descuento y Total a pagar

valorProducto = int(input("Ingrese el valor del producto"))

if valorProducto < 10:
    descuento = valorProducto * 0.10
elif valorProducto >= 10 and valorProducto < 100:
    descuento = valorProducto * 0.05
elif valorProducto >= 100:
    descuento = valorProducto * 0.02
total = valorProducto - descuento

print(f"El total a pagar es {total} con un descuento ({descuento})")
