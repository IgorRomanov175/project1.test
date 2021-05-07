from result_db import heat_consumption_and_supply_of_heating_period_condition


def energy_efficiency_class():
    ep_max = 30
    q_bud = heat_consumption_and_supply_of_heating_period_condition()

    coef = ((q_bud - ep_max) / ep_max) * 100

    if coef <= -50:
        name = "Клас А"
    elif -50 < coef <= -10:
        name = "Клас B"
    elif -10 < coef <= 0:
        name = "Клас C"
    elif 1 < coef <= 25:
        name = "Клас D"
    elif 25 < coef <= 75:
        name = "Клас E"
    elif coef > 75:
        name = "Клас F"

    print(name)

