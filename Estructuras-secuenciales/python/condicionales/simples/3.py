# Pedir al usuario una nota. Si la nota es mayor o igual a 7, imprimir "Aprobado". Si la nota es menor a 7, imprimir "Reprobado".

# entrada
# NotaUsuario
# Proceso
# Validar si la nota es mayor o igual a 7
# Salida
# Mostrar mensaje de aproboado o reprobado

notaUsuario = int(input("Favor, ingresar nota: "))

if notaUsuario == 7:
    print(f'A medias, pero goleador! con {notaUsuario}')
if notaUsuario >= 7:
    print(f'Goleaaaaaaaaadoooooooor con {notaUsuario}')
else:
    print(f'Comite! con {notaUsuario}')