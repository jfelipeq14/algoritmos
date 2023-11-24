# Pedir al usuario su nombre y edad. Si el usuario es mayor de edad, imprimir "Eres mayor de edad".

# entradas
# nombre y edad

# proceso
# validar la edad

# salida
# Mayor de edad o no

nombreUsuario = input("Digite el carechimba nombre suyo: ")
edadUsuario = float(input(f"Ingrese la edad del {nombreUsuario}: "))

if edadUsuario >= 18:
    print(f"El usuario {nombreUsuario} es mayor de edad y tiene {
          edadUsuario} anhos")
