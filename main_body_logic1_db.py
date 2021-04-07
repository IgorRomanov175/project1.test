from main_body_db import *
from result_db import *


def data_dase_1_1(x, y):
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


def data_base_1_2(ans):
    sql_result.execute(f"SELECT width FROM thermal_calculation_condition_inside_wall "
                       f"WHERE width = '{ans}'")  # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


# ----------------------------------------------------------------------------------------------------------------------

def data_base_2_1(x, y):
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


def data_base_2_2(ans):
    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_inside_wall_zero WHERE width = '{ans}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


# -----------------------------------------------------------------------------------------------------------------------

def data_base_3_1(x, y):
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


def data_base_3_2(ans):
    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_inside_wall_zero WHERE width = '{ans}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД
