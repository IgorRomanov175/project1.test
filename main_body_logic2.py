from logic.logic1 import *
from main_body_db import *
from result_db import *


def thermal_calculation_of_the_attic_floor():
    print("Теплотехнічний розрахунок горищного покриття")

    z1 = heat_transfer_coefficient3_1()
    z2 = heat_transfer_coefficient3_2()

    m1 = Therm1_Logic(z1, z2)  # создание объекта для расчёта термического оперения шаров стены

    flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
    while flag == 1:  # создание цикла
        x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
        y = float(input("Теплопроводимость: "))

        m1.therm_calc(x, y)  # метод для расчёта термического оперения шаров стены

        sql.execute(f"SELECT width FROM thermal_calculation_of_the_attic_floor "
                    f"WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
        sql.execute("INSERT INTO thermal_calculation_of_the_attic_floor VALUES (?, ?, ?)",
                    (None, x, y))  # запись данных в таблицу
        con.commit()  # подтверждение действий с БД

        sql_result.execute(f"SELECT width FROM thermal_calculation_condition_of_the_attic_floor "
                           f"WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
        sql_result.execute("INSERT INTO thermal_calculation_condition_of_the_attic_floor VALUES (?, ?, ?)",
                           (None, x, y))  # запись данных в таблицу
        con_result.commit()  # подтверждение действий с БД

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m1.full_formul_calc())
    ans = m1.full_formul_calc()

    sql_result.execute(f"SELECT width FROM thermal_calculation_condition_of_the_attic_floor "
                       f"WHERE width = '{ans}'")  # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_2 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


# -----------------------------------------------------------------------------------------------------------------------

def thermal_calculation_overlap_over_the_underground():
    print("Теплотехнічний розрахунок над підвалом та техпідпіллям")

    z1 = heat_transfer_coefficient3_1()
    z2 = heat_transfer_coefficient3_2()

    m1 = Therm1_Logic(z1, z2)  # создание объекта для расчёта термического оперения шаров стены

    flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
    while flag == 1:  # создание цикла
        x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
        y = float(input("Теплопроводимость: "))

        m1.therm_calc(x, y)  # метод для расчёта термического оперения шаров стены

        sql.execute(f"SELECT width FROM thermal_calculation_of_the_attic_floor "
                    f"WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
        sql.execute("INSERT INTO thermal_calculation_of_the_attic_floor VALUES (?, ?, ?)",
                    (None, x, y))  # запись данных в таблицу
        con.commit()  # подтверждение действий с БД

        sql_result.execute(f"SELECT width FROM thermal_calculation_condition_of_the_attic_floor "
                           f"WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
        sql_result.execute("INSERT INTO thermal_calculation_condition_of_the_attic_floor VALUES (?, ?, ?)",
                           (None, x, y))  # запись данных в таблицу
        con_result.commit()  # подтверждение действий с БД

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m1.full_formul_calc())
    ans = m1.full_formul_calc()

    sql_result.execute(f"SELECT width FROM thermal_calculation_condition_of_the_attic_floor "
                       f"WHERE width = '{ans}'")  # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_2 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД
