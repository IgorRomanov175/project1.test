from result_db import *
from main_body_db import *


def data_base_1(name, ans):
    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?, ?)",
                       (None, name, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_2(name, ans):
    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?, ?)",
                       (None, name, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_3(name, ans):
    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?, ?)",
                       (None, name, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


