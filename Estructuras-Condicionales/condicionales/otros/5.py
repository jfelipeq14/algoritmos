# 5) Que lea dos números y los imprima en forma ascendente

# DE: n1, n2
# P: si (n1 > n2) => n1, n2
#    sino
#     si (n1 < n2) => n2, n1
# DS: "El orden ascendente es nX, nX"

n1 = int(input("Digite un numero: "))
n2 = int(input("Digite otro numero: "))

if n1 > n2:
    print(n2, n1)
elif n1 < n2:
    print(n1, n2)
