from mb_logic_template import *
from mb_initial_data import *


def heat_consumption_of_the_house_through_the_enclosure():
    # Тепловитрати будинку через огороджувальну оболонку
    x1 = 0.024  # розмірний коефіцієнт
    k_bud = total_heat_transfer_coefficient_of_the_house()
    d_d = float(input("Кількість градусо-діб опалювального періоду: "))

    q_x = x1 * k_bud * d_d * calc_all_initial
    name = "Тепловитрати будинку через огороджувальну оболонку"

    data_base_4(name, q_x)


def domestic_heat_during_the_heating_season():
    # Побутове надходження тепла протягом опалювального сезону
    pass


def heat_flow_through_the_windows():
    # Теплові надходження через вікна від сонячної радіації
    pass


def heat_consumption_for_heating_the_building():
    # Розрахункові витрати теплової енергії
    pass

