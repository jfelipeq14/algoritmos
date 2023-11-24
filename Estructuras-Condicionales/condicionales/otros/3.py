# 3) En un almacén se hace un 20% de descuento a los clientes cuya compra supere los $10000 ¿Cuál será la cantidad que pagara una persona por su compra?

valorCompra = int(input("Digite el valor de la compra: "))

if valorCompra > 10000:
    descuento = valorCompra*0.20
    total = valorCompra-descuento
    print(total)
else:
    print(valorCompra)
