from array1.linar_heat_transfer_coefficient import *
from logic.logic1 import *
from logic.logic2 import *
from logic.logic3 import *
from main_body_logic1_db import *


def thermal_calculation_inside_wall():
    print("Теплотехнічний розрахунок зовнішньої стіни")

    z1 = heat_transfer_coefficient1_1()
    z2 = heat_transfer_coefficient1_2()

    m1 = Therm1_Logic(z1, z2)  # создание объекта для расчёта термического оперения шаров стены

    flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
    while flag == 1:  # создание цикла
        x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
        y = float(input("Теплопроводимость: "))

        m1.therm_calc(x, y)  # метод для расчёта термического оперения шаров стены

        data_dase_1_1(x, y)

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m1.full_formul_calc())
    ans = m1.full_formul_calc()

    data_base_1_2(ans)


# -----------------------------------------------------------------------------------------------------------------------

def thermal_calculation_inside_wall_zero():
    print("Теплотехнічний розрахунок зовнішньої стіни нижче відмітки 0.00")

    z1 = heat_transfer_coefficient2_1()
    z2 = heat_transfer_coefficient2_2()

    m2 = Therm1_Logic(z1, z2)  # создание объекта для расчёта термического оперения шаров стены

    flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
    while flag == 1:  # создание цикла
        x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
        y = float(input("Теплопроводимость: "))

        m2.therm_calc(x, y)  # метод для расчёта термического оперения шаров стены

        data_base_2_1(x, y)

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m2.full_formul_calc())
    ans = m2.full_formul_calc()

    data_base_2_2(ans)


# -----------------------------------------------------------------------------------------------------------------------

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

        data_base_3_1(x, y)

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m3.full_therm2_calc())
    ans = m3.full_therm2_calc()

    data_base_3_2(ans)


# -----------------------------------------------------------------------------------------------------------------------

def heat_transfer_resistance_of_external_walls():
    print("\nРозрахунок приведеного опору теплопередачі зовнішніх стін\n")
    calc_area1 = float(input("Площа зовнішніх стін: "))
    # calc_val1 = input("\nТеплотехнічний розрахунок зовнішньої стіни: ")
    calc_values1 = float(thermal_calculation_condition_inside_wall())
    print(calc_values1)

    calc_area2 = float(input("\nПлоща зовнішніх стін нижче відмітки 0.00: "))
    # calc_val2 = input("\nТеплотехнічний розрахунок зовнішньої стіни нижче відмітки 0.00: ")
    calc_values2 = float(thermal_calculation_condition_inside_wall_zero())
    print(calc_values2)

    calc_area3 = float(input("\nПлоща стін підвалу нижче поверхні землі: "))
    # calc_val3 = input("\nТеплотехнічний розрахунок стін підвалу нижче поверхні землі: ")
    calc_values3 = float(thermal_calculation_condition_basement_underground())
    print(calc_values3)

    area = calc_area1 + calc_area2 + calc_area3

    m4 = Therm3_logic(area)
    m4.therm_calc1(calc_values1, calc_area1)
    m4.therm_calc1(calc_values2, calc_area2)
    m4.therm_calc1(calc_values3, calc_area3)
    print("Ответ", m4.therm_calc_all1())

    print("\nРозрахунок лінійних вузлів\n")
    flag_1 = int(input("Додати розрахунок на лінійний вузол\n1 - ДА;\n2 - НЕТ;\n-"))
    while flag_1 == 1:
        linear_coeff_values = int(input("""Оберіть лінійний коефіцієнт теплопередачі теплопровідного включення:
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

        print(linear_coeff)

        linear_lenth = float(input("Лінійний розмір включення: "))

        flag_1 = int(input("\nДодати розрахунок на лінійний вузол\n1 - ДА;\n2 - НЕТ;\n-"))

        m4.therm_calc2(linear_coeff, linear_lenth)
        print("Ответ", m4.therm_calc_all2())

    print("\nРозрахунок точкових вузлів\n")
    flag_2 = int(input("\nДодати розрахунок точкового вузла\n1 - ДА;\n2 - НЕТ;\n-"))
    while flag_2 == 1:
        point_coeff_values = int(input("""Оберіть точковий коефіцієнт теплопередачі теплопровідного включення:
        1. Вузол улаштування несучого кронштейна фасадної системи з вентильованим повітряним прошарком
        2. Вузол улаштування анкера на основі металевого гнучкого Z-подібного елемента фасадної системи
з опорядженням цеглою
        3. Вузол улаштування пластикового дюбеля з металевим стрижнем для кріплення теплоізоляційного шару
в фасадній системі з опорядженням штукатурками
        4. Вузол улаштування пластикового дюбеля з пластиковим стрижнем для кріплення теплоізоляційного шару
в фасадній системі з опорядженням штукатурками
        Оберіть номер вузла: """))

        if point_coeff_values == 1:
            point_coeff = float(node_1_1())

        if point_coeff_values == 2:
            point_coeff = float(node_1_2())

        if point_coeff_values == 3:
            point_coeff = float(node_1_3())

        if point_coeff_values == 4:
            point_coeff = float(node_1_4())

        point_num = float(input("\nКількість точкових включень: "))

        flag_2 = int(input("\nДодати розрахунок точкового вузла\n1 - ДА;\n2 - НЕТ;\n-"))

    m4.therm_calc3(point_coeff, point_num)
    print("Ответ", m4.therm_calc_all3())
    print("\nПовна відповідь", m4.therm_calc_all4())
