# 3) En un almacén se hace un 20% de descuento a los clientes cuya compra supere los $10000 ¿Cuál será la cantidad que pagara una persona por su compra?

#region analisis
#DE: compra
#P: si (compra > 10000) => descuento = compra*0.20
#    sino => descuento = 0
#   total = compra - descuento
# DS: compra, descuento, total
#endregion

#Variable que recibe datos por consola (datos que el usuario me ingresa)
#input: entrada (funcion que recibe un dato)
#int: tipo de dato (convierte el dato en entero para realizar operaciones)
#compra: nombre de la variable (lo que yo indico que recibo)
compra = int(input("Digite la compra: "))

# preguntar si algo se cumple (validacion)
# if: si
# compra (nombre de la variable que necesito validar)
# operador (> mayor que)
# valor que se debe exceder para cumplir la condicion del enunciado
if compra > 10000:
    # sacar el 20% que dice el enunciado
    # descuento: nombre de una variable
    # le asigno (va ser igual) a la multiplicacion de compra (variable) por 0.20 (20%)
    descuento = compra*0.20
# sino: si la condicion del IF no se cumple...
else:
    #descuento no tiene
    descuento = 0

# saber el total
# total: nombre de la variable
# le asigno la resta de compra (dato ingresado) menos el descuento (multiplicacion: el 20% si es mas de 10000 la compra)
total = compra-descuento

#los datos que voy a mostrar
#print: funcion, que muestra lo que yo le indique
#f: indica que puedo usar variables en el texto
#"": se escribe el texto que quiero mostrar
#{}: le indico que variables debo mostrar en el mensaje
print(f"La compra fue: {compra}")
print(f"El descuento fue: {descuento}")
#sin llaves y sin la f
print("El total fue: ", total)