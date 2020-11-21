from logic1 import *
from logicDBN import  *
from db import *

start = int(
    input("Выберите действие:\n1.Продолжить со старой таблицой;\n2.Перезаписать таблицу;\n3.Завершение программы;\n-"))
if start == 1:
    flag = int(input("Добавить расчётный слой?\n1 - ДА;\n2 - НЕТ;\n-"))  # запуск цикла с сбором информации
    while flag == 1:  # создание цикла
        x = float(input("Толщина: "))  # сбор данных: толщина и теплопроводимость
        y = float(input("Теплопроводимость: "))

        m1 = Therm1_Logic(x, y)  # создание объекта для расчёта термического оперения шаров стены
        m1.therm_calc(x, y)  # метод для расчёта термического оперения шаров стены
        sql.execute(f"SELECT width FROM users WHERE width = '{x}'")  # выбор столбца для записи данных в таблицу
        sql.execute("INSERT INTO users VALUES (?, ?, ?)", (None, x, y))  # запись данных в таблицу
        con.commit()  # подтверждение действий с БД

        # z1 =
        # z2 =

        flag = int(input("Добавить расчётный слой?\n-"))  # зацикливание процесса

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

#  Таск: придумать как внести выборочные значения z1 и z2 из таблици heat_transfer_coefficient
