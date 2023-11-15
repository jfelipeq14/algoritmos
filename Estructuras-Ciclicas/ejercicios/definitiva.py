# elabore un algoritmo que permita al profesor de etica calcular la definitiva de 6 notas que planeo realizar. debe mostrar las 6 notas ingresdas y el promedio y untexto que diga debes mejorar, bien o excelente. el criterio para determinar el mensaje es: <3 debes mejorar, 3 - 4 bien y mayor a 4 excelente

contador = 1
sumaNotas = 0
while contador <= 6:
    nota = int(input(f"Digite la nota {contador}: "))
    print(f"La primera nota es {nota}")
    print(f"\n")
    sumaNotas = sumaNotas + nota
    contador += 1

promedio = sumaNotas / 6

if promedio < 3:
    print(f"La nota es {promedio} y debes mejorar")
elif promedio >= 3 and promedio <= 4:
    print(f"La nota es {promedio} y estas bien")
elif promedio > 4:
    print(f"La nota es {promedio} y estas excelente")
