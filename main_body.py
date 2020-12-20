from logic1 import *
from main_body_db import *
from result_db import *


class Menu:
    def __init__(self, choose_action):
        self.choose_action = choose_action
        if self.choose_action == 1:
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
                sql.execute("INSERT INTO thermal_calculation_inside_wall VALUES (?, ?, ?)", (None, x, y))  # запись данных в таблицу
                con.commit()  # подтверждение действий с БД

                sql_result.execute(f"SELECT width FROM thermal_calculation_condition_inside_wall "
                                   f"WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
                sql_result.execute("INSERT INTO thermal_calculation_condition_inside_wall VALUES (?, ?, ?)", (None, x, y))  # запись данных в таблицу
                con_result.commit()  # подтверждение действий с БД

                flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

            print("Ответ", m1.full_formul_calc())
            ansv = m1.full_formul_calc()

            sql_result.execute(f"SELECT width FROM thermal_calculation_condition_inside_wall "
                               f"WHERE width = '{ansv}'")  # выбор столбца для записи данных в таблицу
            sql_result.execute("INSERT INTO thermal_calculation_result VALUES (?, ?)", (None, ansv))  # запись данных в таблицу
            con_result.commit()  # подтверждение действий с БД


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

            m1 = Therm1_Logic(z1, z2)  # создание объекта для расчёта термического оперения шаров стены

            flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
            while flag == 1:  # создание цикла
                x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
                y = float(input("Теплопроводимость: "))

                m1.therm_calc(x, y)  # метод для расчёта термического оперения шаров стены

                sql.execute(f"SELECT width FROM thermal_calculation_inside_wall_zero WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
                sql.execute("INSERT INTO thermal_calculation_inside_wall_zero VALUES (?, ?, ?)", (None, x, y))  # запись данных в таблицу
                con.commit()  # подтверждение действий с БД

                sql_result.execute(f"SELECT width FROM thermal_calculation_condition_inside_wall_zero WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
                sql_result.execute("INSERT INTO thermal_calculation_condition_inside_wall_zero VALUES (?, ?, ?)", (None, x, y))  # запись данных в таблицу
                con_result.commit()  # подтверждение действий с БД

                flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

            print("Ответ", m1.full_formul_calc())
            ansv = m1.full_formul_calc()

            sql_result.execute(f"SELECT width FROM thermal_calculation_condition_inside_wall_zero WHERE width = '{ansv}'")  # выбор столбца для записи данных в таблицу
            sql_result.execute("INSERT INTO thermal_calculation_result VALUES (?, ?)", (None, ansv))  # запись данных в таблицу
            con_result.commit()  # подтверждение действий с БД


            con.commit()
            con_result.commit()

            con.close()
            con_result.close()

        if self.choose_action == 2:
            sql.execute("DROP TABLE thermal_calculation_inside_wall")
            sql.execute("DROP TABLE thermal_calculation_inside_wall_zero")
            sql_result.execute("DROP TABLE thermal_calculation_condition_inside_wall")
            sql_result.execute("DROP TABLE thermal_calculation_condition_inside_wall_zero")
            sql_result.execute("DROP TABLE thermal_calculation_result")

        if self.choose_action == 3:
            return


if __name__ == '__main__':
    start = int(input("""
    Выберите действие:
    1.Продолжить со старой таблицой;
    2.Перезаписать таблицу;
    3.Завершение программы;
    - """))
    main_body_project = Menu(start)