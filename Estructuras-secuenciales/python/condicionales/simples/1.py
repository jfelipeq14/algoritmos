# Pedir al usuario su nombre y edad. Si el usuario es mayor de edad, imprimir "Eres mayor de edad". Si no, imprimir "Eres menor de edad".

nombreUsuario = input("Digite el carechimba nombre suyo: ")
edadUsuario = int(input(f'Ingrese la edad del {nombreUsuario}: '))

if edadUsuario >= 18:
    print(f'El usuario {nombreUsuario} es mayor de edad y tiene {edadUsuario} anhos')
else:
    print(f'El usuario {nombreUsuario} es menor de edad y tiene {edadUsuario} anhos')