from logic.logic3_1 import *
from main_body_logic_template import *


# пункт 3.2
def thermal_calculation_of_the_attic_floor():
    thermal_calculation_template_1(
        x1="Теплотехнічний розрахунок горищного покриття",
        x2=heat_transfer_coefficient3_1(),
        x3=heat_transfer_coefficient3_2(),
        x4="thermal_calculation_of_the_attic_floor"
    )


# пункт 3.3
def thermal_calculation_overlap_over_the_underground():
    thermal_calculation_template_1(
        x1="Теплотехнічний розрахунок над підвалом та техпідпіллям",
        x2=heat_transfer_coefficient4_1(),
        x3=heat_transfer_coefficient4_2(),
        x4="thermal_calculation_overlap_over_the_underground"
    )
    thermal_calculation_template_3(
        name="calculation_coefficient_1"
    )


# пункт 3.4
def thermal_calculation_of_the_basement_floor_1():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для I зони",
        x2="thermal_calculation_of_the_basement_floor_1"
    )


def thermal_calculation_of_the_basement_floor_2():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для II зони",
        x2="thermal_calculation_of_the_basement_floor_2"
    )


def thermal_calculation_of_the_basement_floor_3():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для III зони",
        x2="thermal_calculation_of_the_basement_floor_3"
    )


def thermal_calculation_of_the_basement_floor_4():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для IV зони",
        x2="thermal_calculation_of_the_basement_floor_4"
    )


def heat_transfer_resistance_of_the_basement_floors():
    print("\nТеплотехнічний розрахунок підлоги підвалу\n")
    calc_area1 = float(input("\nПлоща підлоги підвалу (підлога по грунту) I зони: "))
    calc_values1 = float(thermal_calculation_condition_of_the_basement_floor_1())
    print("Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для I зони: ", calc_values1)

    calc_area2 = float(input("\nПлоща підлоги підвалу (підлога по грунту) II зони: "))
    calc_values2 = float(thermal_calculation_condition_of_the_basement_floor_2())
    print("Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для II зони: ", calc_values2)

    calc_area3 = float(input("\nПлоща підлоги підвалу (підлога по грунту) III зони: "))
    calc_values3 = float(thermal_calculation_condition_of_the_basement_floor_3())
    print("Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для III зони: ", calc_values3)

    calc_area4 = float(input("\nПлоща підлоги підвалу (підлога по грунту) IV зони: "))
    calc_values4 = float(thermal_calculation_condition_of_the_basement_floor_4())
    print("Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для IV зони: ", calc_values4)

    area = calc_area1 + calc_area2 + calc_area3 + calc_area4

    m1 = Therm3_logic(area)
    m1.therm_calc1(calc_values1, calc_area1)
    m1.therm_calc1(calc_values2, calc_area2)
    m1.therm_calc1(calc_values3, calc_area3)
    m1.therm_calc1(calc_values4, calc_area4)
    print("Відповідь", m1.therm_calc_all1())
    ans = m1.therm_calc_all2()
    print("Повна відповідь", ans)
    name = "heat_transfer_resistance_of_the_basement_floors"

    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?, ?)",
                       (None, name, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД
