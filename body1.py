from logic1 import *
from db import *

start = int(
    input("Выберите действие:\n1.Продолжить со старой таблицой;\n2.Перезаписать таблицу;\n3.Завершение программы;\n-"))
if start == 1:
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

        sql.execute(f"SELECT width FROM users WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
        sql.execute("INSERT INTO users VALUES (?, ?, ?)", (None, x, y))  # запись данных в таблицу
        con.commit()  # подтверждение действий с БД
        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

    print("Ответ", m1.full_formul_calc())

    start = int(input(
        "Выберите действие:\n1.Продолжить со старой таблицой;\n2.Перезаписать таблицу;\n3.Завершение программы;\n-"))

    for value in sql.execute("SELECT * FROM users"):  # просмотр записаных данных
        print(value)

try:
    if start == 2:
        sql.execute("DROP TABLE users")
except sq.OperationalError:
    print("Таблица уже существует")

con.commit()

con.close()