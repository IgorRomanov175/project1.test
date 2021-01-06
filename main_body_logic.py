from logic1 import *
from logic2 import *
from logic3 import *
from result_db import *
from main_body_db import *
from linar_heat_transfer_coefficient import *


def thermal_calculation_inside_wall():
    print("Теплотехнічний розрахунок зовнішньої стіни")

    m2_value = int(input("Выберите значение из таблици ДБН: "))
    if m2_value == 1:
        z1 = heat_transfer_coefficient1_1()
        z2 = heat_transfer_coefficient1_2()

    if m2_value == 2:
        z1 = heat_transfer_coefficient2_1()
        z2 = heat_transfer_coefficient2_2()

    if m2_value == 3:
        z1 = heat_transfer_coefficient3_1()
        z2 = heat_transfer_coefficient3_2()

    if m2_value == 4:
        z1 = heat_transfer_coefficient4_1()
        z2 = heat_transfer_coefficient4_2()

    if m2_value == 5:
        z1 = heat_transfer_coefficient5_1()
        z2 = heat_transfer_coefficient5_2()

    if m2_value == 6:
        z1 = heat_transfer_coefficient6_1()
        z2 = heat_transfer_coefficient6_2()

    m1 = Therm1_Logic(z1, z2)  # создание объекта для расчёта термического оперения шаров стены

    flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
    while flag == 1:  # создание цикла
        x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
        y = float(input("Теплопроводимость: "))

        m1.therm_calc(x, y)  # метод для расчёта термического оперения шаров стены

        sql.execute(f"SELECT width FROM thermal_calculation_inside_wall "
                    f"WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
        sql.execute("INSERT INTO thermal_calculation_inside_wall VALUES (?, ?, ?)",
                    (None, x, y))  # запись данных в таблицу
        con.commit()  # подтверждение действий с БД

        sql_result.execute(f"SELECT width FROM thermal_calculation_condition_inside_wall "
                           f"WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
        sql_result.execute("INSERT INTO thermal_calculation_condition_inside_wall VALUES (?, ?, ?)",
                           (None, x, y))  # запись данных в таблицу
        con_result.commit()  # подтверждение действий с БД

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m1.full_formul_calc())
    ans = m1.full_formul_calc()

    sql_result.execute(f"SELECT width FROM thermal_calculation_condition_inside_wall "
                       f"WHERE width = '{ans}'")  # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def thermal_calculation_inside_wall_zero():
    print("Теплотехнічний розрахунок зовнішньої стіни нижче відмітки 0.00")

    m2_value = int(input("Выберите значение из таблици ДБН: "))
    if m2_value == 1:
        z1 = heat_transfer_coefficient1_1()
        z2 = heat_transfer_coefficient1_2()

    if m2_value == 2:
        z1 = heat_transfer_coefficient2_1()
        z2 = heat_transfer_coefficient2_2()

    if m2_value == 3:
        z1 = heat_transfer_coefficient3_1()
        z2 = heat_transfer_coefficient3_2()

    if m2_value == 4:
        z1 = heat_transfer_coefficient4_1()
        z2 = heat_transfer_coefficient4_2()

    if m2_value == 5:
        z1 = heat_transfer_coefficient5_1()
        z2 = heat_transfer_coefficient5_2()

    if m2_value == 6:
        z1 = heat_transfer_coefficient6_1()
        z2 = heat_transfer_coefficient6_2()

    m2 = Therm1_Logic(z1, z2)  # создание объекта для расчёта термического оперения шаров стены

    flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
    while flag == 1:  # создание цикла
        x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
        y = float(input("Теплопроводимость: "))

        m2.therm_calc(x, y)  # метод для расчёта термического оперения шаров стены

        sql.execute(f"SELECT width FROM thermal_calculation_inside_wall_zero WHERE width = '{x}'")
        # выбор столбца для записи данных в таблицу
        sql.execute("INSERT INTO thermal_calculation_inside_wall_zero VALUES (?, ?, ?)",
                    (None, x, y))  # запись данных в таблицу
        con.commit()  # подтверждение действий с БД

        sql_result.execute(
            f"SELECT width FROM thermal_calculation_condition_inside_wall_zero WHERE width = '{x}'")
        # выбор столбца для записи данных в таблицу
        sql_result.execute("INSERT INTO thermal_calculation_condition_inside_wall_zero VALUES (?, ?, ?)",
                           (None, x, y))  # запись данных в таблицу
        con_result.commit()  # подтверждение действий с БД

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m2.full_formul_calc())
    ans = m2.full_formul_calc()

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_inside_wall_zero WHERE width = '{ans}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def thermal_calculation_basement_underground():
    print("Теплотехнічний розрахунок стін підвалу нижче поверхні землі")
    m2_value = int(input("Оберіть зону опору теплопередачі: "))
    if m2_value == 1:
        z_zero = 2.1

    if m2_value == 2:
        z_zero = 4.3

    if m2_value == 3:
        z_zero = 8.6

    if m2_value == 4:
        z_zero = 14.2

    m3 = Therm2_Logic(z_zero)

    flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
    while flag == 1:  # создание цикла
        x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
        y = float(input("Теплопроводимость: "))

        m3.therm2_calc(x, y)

        sql.execute(
            f"SELECT width FROM thermal_calculation_basement_underground WHERE width = '{x}'")
        # выбор столбца для записи данных в таблицу
        sql.execute("INSERT INTO thermal_calculation_basement_underground VALUES (?, ?, ?)",
                    (None, x, y))  # запись данных в таблицу
        con.commit()  # подтверждение действий с БД

        sql_result.execute(
            f"SELECT width FROM thermal_calculation_condition_basement_underground WHERE width = '{x}'")
        # выбор столбца для записи данных в таблицу
        sql_result.execute("INSERT INTO thermal_calculation_condition_basement_underground VALUES (?, ?, ?)",
                           (None, x, y))  # запись данных в таблицу
        con_result.commit()  # подтверждение действий с БД

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m3.full_therm2_calc())
    ans = m3.full_therm2_calc()

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_inside_wall_zero WHERE width = '{ans}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def heat_transfer_resistance_of_external_walls():
    print("Розрахунок приведеного опору теплопередачі зовнішніх стін")
    calc_val1 = int(input("Теплотехнічний розрахунок зовнішньої стіни: "))
    if calc_val1 == 1:
        calc_values1 = thermal_calculation_condition_inside_wall()
        print(calc_values1)
    if calc_val1 == 2:
        calc_values1 = 0

    calc_val2 = int(input("Теплотехнічний розрахунок зовнішньої стіни нижче відмітки 0.00: "))
    if calc_val2 == 1:
        calc_values2 = thermal_calculation_condition_inside_wall_zero()
        print(calc_values2)
    if calc_val2 == 2:
        calc_values2 = 0

    calc_val3 = int(input("Теплотехнічний розрахунок стін підвалу нижче поверхні землі: "))
    if calc_val3 == 1:
        calc_values3 = thermal_calculation_condition_basement_underground()
        print(calc_values3)
    if calc_val3 == 2:
        calc_values3 = 0

    calc_val4 = int(input("Теплотехнічний розрахунок зовнішньої стіни: "))
    if calc_val4 == 1:
        calc_values4 = 0

    calc_val5 = int(input("Теплотехнічний розрахунок зовнішньої стіни: "))
    if calc_val5 == 1:
        calc_values5 = 0

    calc_val6 = int(input("Теплотехнічний розрахунок зовнішньої стіни: "))
    if calc_val6 == 1:
        calc_values6 = 0

    calc_val6 = int(input("Теплотехнічний розрахунок зовнішньої стіни: "))
    if calc_val6 == 1:
        calc_values7 = 0

    area = float(input("Загальна площа конструкції: "))

    m4 = Therm3_logic(area)
    m4.therm_calc1(calc_values1, calc_values2, calc_values3, calc_values4, calc_values5, calc_values6, calc_values7)

    print("Розрахунок лінійних вузлів")
    flag_1 = int(input("Додати розрахунок на лінійний вузол\n1 - ДА;\n2 - НЕТ;\n-"))
    while flag_1 == 1:
        linear_coeff_values = float(input("""Оберіть лінійний коефіцієнт теплопередачі теплопровідного включення:
        1. Вузол примикання зовнішніх стін із цегли з опорядженням штукатуркою до міжповерхового перекриття
        2. Вузол примикання зовнішніх стін із залізобетону з опорядженням штукатуркою до міжповерхневого перекриття
        3. Вузол примикання зовнішніх стін із вентильованим повітрянним прошарком з опорядженням штукатуркою 
до міжповерхневого перекриття
        4. Вузол примикання зовнішніх стін із ніздрюватого бетону до міжповерхового перекриття
        5. Вузол примикання зовнішніх стін із цегли з опорядженням штукатуркою до балконного перекриття
        6. Вузол примикання зовнішніх стін із залізобетону з опорядженням штукатуркою до балконного перекриття
        7. Вузол примикання зовнішніх стін із ніздрюватого бетону до балконного перекриття
        8. Вузол кутового сполучення зовнішніх стін із залізобетону та цегли з опорядженням штукатуркою
        9. Вузол кутового сполучення зовнішніх стін із залізобетону та цегли з вентильованим повітряним прошарком
        10. Вузол кутового сполучення зовнішніх стін із залізобетону з утепленням та ніздрюватого бетону
        11. Вузол кутового сполучення зовнішніх стін із цегли з опорядженням штукатуркою
        12. Вузол кутового сполучення зовнішніх стін із цегли з вентильованим повітряним прошарком
        13. Вузол кутового сполучення зовнішніх стін із ніздрюватого бетону
        14. Вузол примикання віконної конструкції до зовнішніх стін із цегли з опорядженням штукатуркою
в зоні перемички
        15. Вузол примикання віконної конструкції до зовнішніх стін із цегли з опорядженням штукатуркою
в зоні підвіконня
        16. Вузол примикання віконної конструкції до зовнішніх стін із цегли з опорядженням штукатуркою
в зоні рядового сполучення
        17. Вузол примикання віконної конструкції до зовнішніх стін із цегли з вентильованим повітряним прошарком 
в зоні перемички
        18. Вузол примикання віконної конструкції до зовнішніх стін із цегли з вентильованим повітряним прошарком 
в зоні підвіконня
        19. Вузол примикання віконної конструкції до зовнішніх стін із цегли з вентильованим повітряним прошарком 
в зоні рядового сполучення
        20. Вузол примикання віконної конструкції до зовнішніх стін із ніздрюватого бетону в зоні перемички
        21. Вузол примикання віконної конструкції до зовнішніх стін із цегли з ніздрюватого бетону
в зоні підвіконня
        22. Вузол примикання віконної конструкції до зовнішніх стін із цегли з ніздрюватого бетону
в зоні рядового сполучення
        23. Вузол примикання зовнішніх стін із тришарових панелей на основі важкого бетону до 
міжповерхового перекриття
        24. Вузол влаштування зовнішніх стін із вентильваним повітряним прошарком на основі дерев'яного каркаса
        25. Вузол примикання конструкції горищного даху з одношаровою теплоізоляцією до дерев'яної крокви
        26. Вузол примикання конструкції горищного даху з двошаровою теплоізоляцією  
до дерев'яної крокви та обрешіткою 50мм
        27. Вузол примикання конструкції горищного даху з двошаровою теплоізоляцією 
до дерев'яної крокви та обрешіткою 100мм
        28. Вузол примикання конструкції горищного даху з двошаровою теплоізоляцією 
до дерев'яної обрешітки товщиною 50мм
        29. Вузол примикання конструкції горищного даху з двошаровою теплоізоляцією 
до дерев'яної обрешітки товщиною 100мм
        30. Вузол примикання конструкції перекриття до внутрішніх стін
        31. Вузол примикання конструкції перекриття до дерев'яної лаги
        32. Вузол примикання конструкції підлоги по грунту до стіни цоколя
        33. Вузол примикання конструкції підлоги по грунту до стіни підвала
        34. Вузол примикання конструкції по грунту до зовнішніх стін з фасадною теплоізоляцією
        35. Вузол примикання конструкції по грунту до зовнішніх стін з блоків з ніздрюватого бетону
        36. Вузол кутового сполучення зовнішніх стін з цегли з додатковою теплоізоляцією та опорядженням штукатуркою
        37. Вузол примикання до металевого несучого елемента каркаса
        Оберіть номер вузла: """))

        if linear_coeff_values == 1:
            linear_coeff = node_1()

        elif linear_coeff_values == 2:
            linear_coeff = node_2()

        elif linear_coeff_values == 3:
            linear_coeff = node_3()

        elif linear_coeff_values == 4:
            linear_coeff = node_4()

        elif linear_coeff_values == 5:
            linear_coeff = node_5()

        elif linear_coeff_values == 6:
            linear_coeff = node_6()

        elif linear_coeff_values == 7:
            linear_coeff = node_7()

        elif linear_coeff_values == 8:
            linear_coeff = node_8()

        elif linear_coeff_values == 9:
            linear_coeff = node_9()

        elif linear_coeff_values == 10:
            linear_coeff = node_10()

        elif linear_coeff_values == 11:
            linear_coeff = node_11()

        elif linear_coeff_values == 12:
            linear_coeff = node_12()

        elif linear_coeff_values == 13:
            linear_coeff = node_13()

        elif linear_coeff_values == 14:
            linear_coeff = node_14()

        elif linear_coeff_values == 15:
            linear_coeff = node_15()

        elif linear_coeff_values == 16:
            linear_coeff = node_16()

        elif linear_coeff_values == 17:
            linear_coeff = node_17()

        elif linear_coeff_values == 18:
            linear_coeff = node_18()

        elif linear_coeff_values == 19:
            linear_coeff = node_19()

        elif linear_coeff_values == 20:
            linear_coeff = node_20()

        elif linear_coeff_values == 21:
            linear_coeff = node_21()

        elif linear_coeff_values == 22:
            linear_coeff = node_22()

        elif linear_coeff_values == 23:
            linear_coeff = node_23()

        elif linear_coeff_values == 24:
            linear_coeff = node_24()

        elif linear_coeff_values == 25:
            linear_coeff = node_25()

        elif linear_coeff_values == 26:
            linear_coeff = node_26()

        elif linear_coeff_values == 27:
            linear_coeff = node_27()

        elif linear_coeff_values == 28:
            linear_coeff = node_28()

        elif linear_coeff_values == 29:
            linear_coeff = node_29()

        elif linear_coeff_values == 30:
            linear_coeff = node_30()

        elif linear_coeff_values == 31:
            linear_coeff = node_31()

        elif linear_coeff_values == 32:
            linear_coeff = node_32()

        elif linear_coeff_values == 33:
            linear_coeff = node_33()

        elif linear_coeff_values == 34:
            linear_coeff = node_34()

        elif linear_coeff_values == 35:
            linear_coeff = node_35()

        elif linear_coeff_values == 36:
            linear_coeff = node_36()

        elif linear_coeff_values == 37:
            linear_coeff = node_37()

        linear_lenth = float(input("Лінійний розмір включення: "))

    m4.therm_calc2(linear_coeff, linear_lenth)

    print("Розрахунок точкових вузлів")
    flag_2 = int(input())
