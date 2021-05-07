from mb_logic_template import *
from mb_initial_data import *


def heat_consumption_of_the_house_through_the_enclosure():
    # Тепловитрати будинку через огороджувальну оболонку
    k_bud = total_heat_transfer_coefficient_of_the_house_condition()

    q_k = x1 * k_bud * d_d * calc_all_initial
    name = "Тепловитрати будинку через огороджувальну оболонку"
    print(name, ": ", q_k)

    data_base_4(name, q_k)


def domestic_heat_during_the_heating_season():
    # Побутове надходження тепла протягом опалювального сезону
    q_t_1 = float(input("Кількість віділеного тепла на 1 людину: "))
    n_1 = int(input("Кількість людей: "))
    t_t_1 = int(input("Кількість годин на тиждень: "))
    t_m_1 = int(input("Кількість годин на місяць: "))
    q_1 = (q_t_1 * n_1 * (t_t_1 / t_m_1)) / 1000
    print("Тепловиділення від людей протягом тижня: ", q_1)

    q_t_2 = float(input("Кількість віділеного тепла на 1 техніку: "))
    n_2 = int(input("Кількість техніки: "))
    t_t_2 = int(input("Кількість годин на тиждень: "))
    t_m_2 = int(input("Кількість годин на місяць: "))

    q_2 = (q_t_2 * n_2 * (t_t_2 / t_m_2) * 0.95) / 1000
    print("Тепловиділення від техніки протягом тижня: ", q_2)

    q_vnp_coeff = (q_1 + q_2) * 1000 / calc_area_7
    print("Величина побутових теплонадходжень: ", q_vnp_coeff)

    q_vnp = x1 * q_vnp_coeff * z_op * calc_area_7
    name = "Побутове надходження тепла протягом опалювального сезону"
    print(name, ": ", q_vnp)

    data_base_4(name, q_vnp)



def heat_flow_through_the_windows():
    print("Площа світлових прорізів фасадів будинку")
    f_n = float(input("Площа світлових прорізів фасадів - північ: "))
    f_e = float(input("Площа світлових прорізів фасадів - схід: "))
    f_s = float(input("Площа світлових прорізів фасадів - південь: "))
    f_w = float(input("Площа світлових прорізів фасадів - захід: "))

    print("Суми сумарної сонячної радіації")
    i_n = float(input("Суми сумарної сонячної радіації - північ: "))
    i_e = float(input("Суми сумарної сонячної радіації - схід: "))
    i_s = float(input("Суми сумарної сонячної радіації - південь: "))
    i_w = float(input("Суми сумарної сонячної радіації - захід: "))

    q_s_m = e_v_in * e_v_out * (f_n * i_n + f_e * i_e + f_s * i_s + f_w * i_w)
    q_s = (q_s_m * 2.778) / 10
    name = "Площа світлових прорізів фасадів будинку"
    print(name, ": ", q_s)

    data_base_4(name, q_s)


def heat_consumption_for_heating_the_building():
    # Розрахункові витрати теплової енергії
    q_k = heat_consumption_of_the_house_through_the_enclosure_condition()
    q_vnp = domestic_heat_during_the_heating_season_condition()
    q_s = heat_flow_through_the_windows_condition()

    q_rik = (q_k - (q_vnp + q_s) * v_coef * eps_coef) * beta_h_coef
    name = "Розрахункові витрати теплової енергії"
    print(name, ": ", q_rik)

    data_base_4(name, q_rik)


def heat_consumption_and_supply_of_heating_period():
    # розрахункове значення питомих тепловитрат і теплонадходжень будинку за опалювальний період
    q_rik = heat_consumption_for_heating_the_building_condition()

    q_bud = q_rik / calc_volume_1
    name = "Розрахункове значення питомих тепловитрат і теплонадходжень будинку"
    print(name, ": ", q_bud)

    data_base_4(name, q_bud)
