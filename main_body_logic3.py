from main_body_logic_template import *


def min_ht_resistance_of_external_enclosing_structures():
    calc_area_1 = float(input("Площа зовнішніх стін: "))
    calc_value_1 = float(heat_transfer_resistance_of_external_walls_condition())
    print("Приведений опір зовнішніх стін: ", calc_value_1)

    t_v = float(input("Температура 1: "))
    t_n = float(input("Температура 2: "))
    t_z = float(input("Температура 3: "))

    n = (t_v - t_n) / (t_v - t_z)
    r_q_min = 3.75

    r_q_1 = n * r_q_min
    print(r_q_1)

    calc_area_2 = float(input("Площа перекриття над пдвалом, техпідпіллям: "))
    a = thermal_calculation_condition_overlap_over_the_underground()
    calc_value_2 = a * r_q_1
    print("Приведений опір перекриття над пдвалом, техпідпіллям: ", calc_value_2)

    calc_area_3 = float(input("Площа підлоги по грунту: "))
    calc_value_3 = heat_transfer_resistance_of_the_basement_floors_condition()
    print("Приведений опір підлоги по грунту: ", calc_value_3)

    calc_area_4 = float(input("Площа горищного перекриття: "))
    calc_value_4 = thermal_calculation_condition_of_the_attic_floor()
    print("Приведений опір горищного перекриття: ", calc_value_4)

    calc_area_5 = float(input("Площа світлопрозорих конструкцій: "))
    calc_value_5 = float(input("Приведений опір світлопрозорих конструкцій: "))

    calc_area_6 = float(input("Площа вхідних дверей: "))
    calc_value_6 = float(input("Приведений опір вхідних дверей: "))

    coef_e = int(input("Коефіцієнт додаткових тепловтрат:\n1-для житлових будинків\n2-інше\n-"))
    if coef_e == 1:
        e = 1.13
    elif coef_e == 2:
        e = 1.1

    calc_area_all = calc_area_1 + calc_area_2 + calc_area_3 + calc_area_4 + calc_area_5 + calc_area_6
    print(calc_area_all)
    calc_value_all = e * ((calc_area_1 / calc_value_1) + (calc_area_2 / calc_value_2) + (calc_area_3 / calc_value_3) +
                          (calc_area_4 / calc_value_4) + (calc_area_5 / calc_value_5) + (calc_area_6 / calc_value_6))
    print(calc_value_all)
    calc = calc_value_all / calc_area_all
    print(calc)


min_ht_resistance_of_external_enclosing_structures()
