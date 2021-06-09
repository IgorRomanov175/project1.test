from initial_pack.linar_heat_transfer_coefficient import *
from logic.logic3 import *
from logic.logic3_1 import *
from mb_initial_data import *
from mb_logic_template import *

with open("C:\Python_project\project1.test\json\init_main_data_1.json", "r") as json_file:
    a_json = json.load(json_file)


# пункт 3.1.1
def thermal_calculation_inside_wall():
    thermal_calculation_template_1(
        x1="Теплотехнічний розрахунок зовнішніх стін",
        x2=heat_transfer_coefficient1_1(),
        x3=heat_transfer_coefficient1_2(),
        x4=thermal_calculation_inside_wall_array
    )


# -----------------------------------------------------------------------------------------------------------------------

# пункт 3.1.2
def thermal_calculation_inside_wall_zero():
    thermal_calculation_template_1(
        x1="Теплотехнічний розрахунок зовнішньої стіни нижче відмітки 0.00",
        x2=heat_transfer_coefficient2_1(),
        x3=heat_transfer_coefficient2_2(),
        x4=thermal_calculation_inside_wall_zero_array
    )


# -----------------------------------------------------------------------------------------------------------------------

# пункт 3.1.3

def thermal_calculation_basement_underground_1():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок стін підвалу нижче поверхні землі для I зони",
        x2=thermal_calculation_basement_underground_array
    )


def thermal_calculation_basement_underground_2():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок стін підвалу нижче поверхні землі для II зони",
        x2=thermal_calculation_basement_underground_array
    )


def thermal_calculation_basement_underground_3():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок стін підвалу нижче поверхні землі для III зони",
        x2=thermal_calculation_basement_underground_array
    )


def thermal_calculation_basement_underground_4():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок стін підвалу нижче поверхні землі для IV зони",
        x2=thermal_calculation_basement_underground_array
    )


# -----------------------------------------------------------------------------------------------------------------------

# пункт 3.1.4
def heat_transfer_resistance_of_external_walls():
    print("\n#######################################################################################################\n")
    print("\nРозрахунок приведеного опору теплопередачі зовнішніх стін\n")
    print("Площа зовнішніх стін: ", calc_area_1)
    calc_values1 = float(thermal_calculation_condition_inside_wall())
    print("Розрахунок приведеного опору теплопередачі зовнішніх стін: ", calc_values1)

    print("\nПлоща зовнішніх стін нижче відмітки 0.00: ", calc_area_1_1)
    calc_values2 = float(thermal_calculation_condition_inside_wall_zero())
    print("Теплотехнічний розрахунок зовнішньої стіни нижче відмітки 0.00: ", calc_values2)

    print("\nПлоща стін підвалу нижче поверхні землі: ", calc_area_1_2)
    calc_values3 = float(thermal_calculation_condition_basement_underground_1())
    print("Теплотехнічний розрахунок стін підвалу нижче поверхні землі: ", calc_values3)

    area = calc_area_1 + calc_area_1_1 + calc_area_1_2

    m4 = Therm3_logic(area)
    m4.therm_calc1(calc_values1, calc_area_1)
    m4.therm_calc1(calc_values2, calc_area_1_1)
    m4.therm_calc1(calc_values3, calc_area_1_2)
    print("Ответ", m4.therm_calc_all1())

    print("\nРозрахунок лінійних вузлів\n")

    if a_json["paragraph 3.1.4"]["linear_coeff_values_1"]["active"] == 1:
        linear_coeff = node_1()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_1"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_2"]["active"] == 1:
        linear_coeff = node_2()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_2"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_3"]["active"] == 1:
        linear_coeff = node_3()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_3"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_4"]["active"] == 1:
        linear_coeff = node_4()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_4"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_5"]["active"] == 1:
        linear_coeff = node_5()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_5"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_6"]["active"] == 1:
        linear_coeff = node_6()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_6"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_7"]["active"] == 1:
        linear_coeff = node_7()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_7"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_8"]["active"] == 1:
        linear_coeff = node_8()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_8"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_9"]["active"] == 1:
        linear_coeff = node_9()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_9"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_10"]["active"] == 1:
        linear_coeff = node_10()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_10"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_11"]["active"] == 1:
        linear_coeff = node_11()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_11"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_12"]["active"] == 1:
        linear_coeff = node_12()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_12"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_13"]["active"] == 1:
        linear_coeff = node_13()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_13"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_14"]["active"] == 1:
        linear_coeff = node_14()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_14"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_15"]["active"] == 1:
        linear_coeff = node_15()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_15"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_16"]["active"] == 1:
        linear_coeff = node_16()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_16"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_17"]["active"] == 1:
        linear_coeff = node_17()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_17"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_18"]["active"] == 1:
        linear_coeff = node_18()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_18"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_19"]["active"] == 1:
        linear_coeff = node_19()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_19"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_20"]["active"] == 1:
        linear_coeff = node_20()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_20"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_21"]["active"] == 1:
        linear_coeff = node_21()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_21"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_22"]["active"] == 1:
        linear_coeff = node_22()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_22"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_23"]["active"] == 1:
        linear_coeff = node_23()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_23"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_24"]["active"] == 1:
        linear_coeff = node_24()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_24"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_25"]["active"] == 1:
        linear_coeff = node_25()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_25"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_26"]["active"] == 1:
        linear_coeff = node_26()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_26"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_27"]["active"] == 1:
        linear_coeff = node_27()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_27"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_28"]["active"] == 1:
        linear_coeff = node_28()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_28"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_29"]["active"] == 1:
        linear_coeff = node_29()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_29"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_30"]["active"] == 1:
        linear_coeff = node_30()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_30"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_31"]["active"] == 1:
        linear_coeff = node_31()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_31"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_32"]["active"] == 1:
        linear_coeff = node_32()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_32"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_33"]["active"] == 1:
        linear_coeff = node_33()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_33"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_34"]["active"] == 1:
        linear_coeff = node_34()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_34"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_35"]["active"] == 1:
        linear_coeff = node_35()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_35"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_36"]["active"] == 1:
        linear_coeff = node_36()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_36"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    if a_json["paragraph 3.1.4"]["linear_coeff_values_37"]["active"] == 1:
        linear_coeff = node_37()
        linear_lenth = a_json["paragraph 3.1.4"]["linear_coeff_values_37"]["value"]
        m4.therm_calc2(linear_coeff, linear_lenth)

    print("Ответ", m4.therm_calc_all2())

    print("\nРозрахунок точкових вузлів\n")

    if a_json["paragraph 3.1.4"]["point_coeff_values_1"]["active"] == 1:
        point_coeff = node_1_1()
        point_num = a_json["paragraph 3.1.4"]["point_coeff_values_1"]["value"]
        m4.therm_calc3(point_coeff, point_num)

    if a_json["paragraph 3.1.4"]["point_coeff_values_2"]["active"] == 1:
        point_coeff = node_1_2()
        point_num = a_json["paragraph 3.1.4"]["point_coeff_values_2"]["value"]
        m4.therm_calc3(point_coeff, point_num)

    if a_json["paragraph 3.1.4"]["point_coeff_values_3"]["active"] == 1:
        point_coeff = node_1_3()
        point_num = a_json["paragraph 3.1.4"]["point_coeff_values_3"]["value"]
        m4.therm_calc3(point_coeff, point_num)

    if a_json["paragraph 3.1.4"]["point_coeff_values_4"]["active"] == 1:
        point_coeff = node_1_4()
        point_num = a_json["paragraph 3.1.4"]["point_coeff_values_4"]["value"]
        m4.therm_calc3(point_coeff, point_num)



    print("Ответ", m4.therm_calc_all3())
    ans = m4.therm_calc_all4()
    print("\nПовна відповідь", ans)
    name = "Розрахунок приведеного опору теплопередачі зовнішніх стін"

    data_base_1(name, ans)


# -----------------------------------------------------------------------------------------------------------------------

# пункт 3.2
def thermal_calculation_of_the_attic_floor():
    thermal_calculation_template_1(
        x1="Теплотехнічний розрахунок горищного покриття",
        x2=heat_transfer_coefficient3_1(),
        x3=heat_transfer_coefficient3_2(),
        x4=thermal_calculation_of_the_attic_floor_array
    )


# -----------------------------------------------------------------------------------------------------------------------

# пункт 3.3
def thermal_calculation_overlap_over_the_underground():
    thermal_calculation_template_1(
        x1="Теплотехнічний розрахунок над підвалом та техпідпіллям",
        x2=heat_transfer_coefficient4_1(),
        x3=heat_transfer_coefficient4_2(),
        x4=thermal_calculation_overlap_over_the_underground_array
    )
    thermal_calculation_template_3(
        name="calculation_coefficient_1"
    )


# -----------------------------------------------------------------------------------------------------------------------

# пункт 3.4
def thermal_calculation_of_the_basement_floor_1():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для I зони",
        x2=thermal_calculation_of_the_basement_floor_array
    )


def thermal_calculation_of_the_basement_floor_2():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для II зони",
        x2=thermal_calculation_of_the_basement_floor_array
    )


def thermal_calculation_of_the_basement_floor_3():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для III зони",
        x2=thermal_calculation_of_the_basement_floor_array
    )


def thermal_calculation_of_the_basement_floor_4():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для IV зони",
        x2=thermal_calculation_of_the_basement_floor_array
    )


# -----------------------------------------------------------------------------------------------------------------------
# пункт 3.5
def heat_transfer_resistance_of_the_basement_floors():
    print("\nТеплотехнічний розрахунок підлоги підвалу\n")
    print("\nПлоща підлоги підвалу (підлога по грунту) I зони: ", calc_area_3_1)
    calc_values1 = float(thermal_calculation_condition_of_the_basement_floor_1())
    print("Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для I зони: ", calc_values1)

    print("\nПлоща підлоги підвалу (підлога по грунту) II зони: ", calc_area_3_2)
    calc_values2 = float(thermal_calculation_condition_of_the_basement_floor_2())
    print("Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для II зони: ", calc_values2)

    print("\nПлоща підлоги підвалу (підлога по грунту) III зони: ", calc_area_3_3)
    calc_values3 = float(thermal_calculation_condition_of_the_basement_floor_3())
    print("Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для III зони: ", calc_values3)

    print("\nПлоща підлоги підвалу (підлога по грунту) IV зони: ", calc_area_3_4)
    calc_values4 = float(thermal_calculation_condition_of_the_basement_floor_4())
    print("Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для IV зони: ", calc_values4)

    m1 = Therm3_1_logic(calc_area_3)
    m1.therm_calc1(calc_values1, calc_area_3_1)
    m1.therm_calc1(calc_values2, calc_area_3_2)
    m1.therm_calc1(calc_values3, calc_area_3_3)
    m1.therm_calc1(calc_values4, calc_area_3_4)
    print("Відповідь", m1.therm_calc_all1())

    ans = m1.therm_calc_all2()
    print("Повна відповідь", ans)
    name = "Теплотехнічний розрахунок підлоги підвалу"

    data_base_1(name, ans)


# -----------------------------------------------------------------------------------------------------------------------
# пункт 3.7
def min_ht_resistance_of_external_enclosing_structures():
    print("Площа зовнішніх стін: ", calc_area_1)
    calc_value_1 = float(heat_transfer_resistance_of_external_walls_condition())
    print("Приведений опір зовнішніх стін: ", calc_value_1)
    n = calculation_coefficient_1()
    print("Площа перекриття над пдвалом, техпідпіллям: ", calc_area_2)
    a_therm = thermal_calculation_condition_overlap_over_the_underground()
    calc_value_2 = a_therm * n
    print("Приведений опір перекриття над пдвалом, техпідпіллям: ", calc_value_2)

    print("Площа підлоги по грунту: ", calc_area_3)
    calc_value_3 = heat_transfer_resistance_of_the_basement_floors_condition()
    print("Приведений опір підлоги по грунту: ", calc_value_3)

    print("Площа горищного перекриття: ", calc_area_4)
    calc_value_4 = thermal_calculation_condition_of_the_attic_floor()
    print("Приведений опір горищного перекриття: ", calc_value_4)

    print("Площа світлопрозорих конструкцій: ", calc_area_5)
    calc_value_5 = r_t_s

    print("Площа вхідних дверей: ", calc_area_6)
    calc_value_6 = r_d

    calc_value_all = e * ((calc_area_1 / calc_value_1) + (calc_area_2 / calc_value_2) + (calc_area_3 / calc_value_3) +
                          (calc_area_4 / calc_value_4) + (calc_area_5 / calc_value_5) + (calc_area_6 / calc_value_6))
    k_sum = calc_value_all / calc_all_initial
    print("Приведений коефіцієнт теплопередачі теплоізоляційної оболонки повітря: ", k_sum)

    y_z = 353 / (273 + 0.5 * (t_v - t_op))
    print("Розрахунок середньої густини повітря, що надходить до приміщення за рахунок інфільтрації та вентиляції: ",
          y_z)

    print("Середня кратність повітрообміну для школи за опалюванльний період")

    coef_1 = l_v * n_v / 168
    coef_2 = p_inf * nu * n_inf / 168 * y_z
    coef_3 = v_v * calc_volume_1

    n_ob = (coef_1 + coef_2) / coef_3
    print("Середня кратність повітрообміну для школи за опалювальний період", n_ob)

    print("Умовний коефіцієнт теплопередачі будинку, що враховує тепловитрати за рахунок інфільтрації та вентиляції")
    k_inf = x2 * c * n_ob * v_v * calc_volume_1 * y_z * nu / calc_all_initial
    print("Відповідь: ", k_inf)
    name = "Загальний коефіцієнт теплопередачі"
    print(name)
    k_bud = k_sum + k_inf
    print("Загальний коефіцієнт теплопередачі: ", k_bud)

    data_base_1(name, k_bud)
