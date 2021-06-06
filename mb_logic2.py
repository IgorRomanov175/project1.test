from mb_initial_data import *
from mb_logic_db import *


def coefficient_glazing_of_the_facade():
    print("\n#######################################################################################################\n")

    m_sk = calc_area_5 / (calc_area_5 + calc_area_6 + calc_area_1)
    name_1 = "Коефіцієнт скління фасаду"
    print("Коефіцієнт скління фасаду: ", m_sk)
    data_base_3(name_1, m_sk)

    print("\n#######################################################################################################\n")

    a_kbud = (calc_area_1 + calc_area_2 + calc_area_3 + calc_area_4 + calc_area_5 + calc_area_6) / calc_volume_1
    name_2 = "Показник компактності будинку"
    print("Показник компактності будинку: ", a_kbud)
    data_base_3(name_2, a_kbud)



