# elabore un algoritmo que muestre los minutos y los segundos y las horas de un dia
for semana in range(4):
    for dia in range(7):
        for horas in range(24):
            for minutos in range(60):
                for segundos in range(60):
                    print(f"Semana {semana}, dia {dia} => {
                          horas} : {minutos} : {segundos}")
