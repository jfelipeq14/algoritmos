# Joven aprendiz la empresa “Todo es posible”, lo contrata para que elabore un
# algoritmo que muestre el sueldo de 5 trabajadores incluyendo el bono y el valor del
# bono. Para calcular el bono que el trabajador recibe mensual, se asigna como un
# porcentaje de su salario mensual= (Valor Hora * Número de horas trabajadas) que
# depende de su antigüedad en la empresa de acuerdo con la siguiente tabla:

# Tiempo Utilidad = > Valor bono
# Menos de 1 año 5 % del salario mensual
# 1 año o más y menos de 5 años 7% del salario
# 5 años o más y menos de 10 años 10% del salario
# 10 años o más y menos de 20 años 15% del salario
# 20 años o más 20% del salario

for i in range(5):
    print("\n")
    nombre = input(f"Digite el nombre del trabajador {i+1}: ")
    tiempoEnLaEmpresa = int(
        input(f"Cuanto tiempo lleva en la empresa señore {nombre}: "))
    numeroHorasTrabajadas = int(
        input(f"¿Cuantas horas trabajo {nombre} en este mes? R// "))
    valorHora = int(input("¿Cuanto vale la hora? R// "))

    salarioMensual = valorHora * numeroHorasTrabajadas

    if tiempoEnLaEmpresa < 1:
        bono = salarioMensual * 0.05
    elif tiempoEnLaEmpresa >= 1 and tiempoEnLaEmpresa < 5:
        bono = salarioMensual * 0.07
    elif tiempoEnLaEmpresa >= 5 and tiempoEnLaEmpresa < 10:
        bono = salarioMensual * 0.10
    elif tiempoEnLaEmpresa >= 10 and tiempoEnLaEmpresa < 20:
        bono = salarioMensual * 0.15
    elif tiempoEnLaEmpresa >= 20:
        bono = salarioMensual * 0.20

    pagoTotal = salarioMensual + bono

    print("\n")
    print(f"Salario mensual de {nombre}: {salarioMensual}")
    print(f"Bono de {nombre}: {bono}")
    print(f"Total de {nombre}: {pagoTotal}")
