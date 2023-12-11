# 2. Elabore un algoritmo que lea y muestre 10 nombres de aprendices.

nombres = []
for i in range(10):
    nombre = input(f"Digite el nombre del aprendiz {i+1}")
    nombres.append(nombre)

print(f"Los nombres de los aprendices son {nombres}")
