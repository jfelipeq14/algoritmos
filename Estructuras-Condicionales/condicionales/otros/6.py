# 6) Una persona enferma, que pesa 70 kg, se encuentra en reposo y desea saber cuántas calorías consume su cuerpo durante todo el tiempo que realice una misma actividad. Las actividades que tiene permitido realizar son únicamente dormir o estar sentado en reposo. Los datos que tiene son que estando dormido consume 1.08 calorías por minuto y estando sentado en reposo consume 1.66 calorías por minuto

# DE: actividad, tiempoEnMinutos

# P: si (actividad == "dormido") => calorias = 1.08 * tiempoEnMinutos
#    sino
#     si (actividad == "sentado") => calorias = 1.66 * tiempoEnMinutos

# DS: calorias

print("Lista de actividades:")
print("dormido")
print("sentado")
actividad = input("Digite la actividad: ")
tiempoEnMinutos = int(
    input("Digite la cantidad de tiempo que realizo la actividad en minutos: "))

if actividad == "dormido":
    calorias = 1.08 * tiempoEnMinutos
elif actividad == "sentado":
    calorias = 1.66 * tiempoEnMinutos
print(calorias)
