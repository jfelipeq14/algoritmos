# Escriba un programa que pregunte al usuario su edad y, en función de su respuesta, le muestre el siguiente mensaje:

# Si el usuario tiene menos de 18 años, el mensaje debe ser "Eres menor de edad".
# Si el usuario tiene entre 18 y 65 años, el mensaje debe ser "Eres mayor de edad".
# Si el usuario tiene más de 65 años, el mensaje debe ser "Eres jubilado".

# analisis:
# entradas => Edad del usuario ✔
# proceso => validar la edad ✔
# salida => Mensajes predeterminados por validaciones ✔

edadUsuario = int(input("Digite su edad"))

if edadUsuario < 18:
    print("Eres menor de edad")
elif edadUsuario >= 18 and edadUsuario <= 65:
    print("Eres mayor de edad")
elif edadUsuario > 65:
    print("Eres jubilado")
