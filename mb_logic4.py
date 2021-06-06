from result_db import heat_consumption_and_supply_of_heating_period_condition


def energy_efficiency_class():
    print("\n#######################################################################################################\n")
    ep_max = 30
    q_bud = heat_consumption_and_supply_of_heating_period_condition()

    coef = ((q_bud - ep_max) / ep_max) * 100
    print(coef)

    if coef <= -50:
        name = "Клас енергоефективності - А"
    elif -50 < coef <= -10:
        name = "Клас енергоефективності - B"
    elif -10 < coef <= 0:
        name = "Клас енергоефективності - C"
    elif 1 < coef <= 25:
        name = "Клас енергоефективності - D"
    elif 25 < coef <= 75:
        name = "Клас енергоефективності - E"
    elif coef > 75:
        name = "Клас енергоефективності - F"

    print(name)

