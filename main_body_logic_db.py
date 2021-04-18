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


# ----------------------------------------------------------------------------------------------------------------------

def data_base_3_1_1(x, y):
    sql.execute(
        f"SELECT width FROM thermal_calculation_basement_underground_1 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql.execute("INSERT INTO thermal_calculation_basement_underground_1 VALUES (?, ?, ?)",
                (None, x, y))  # запись данных в таблицу
    con.commit()  # подтверждение действий с БД

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_basement_underground_1 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_condition_basement_underground_1 VALUES (?, ?, ?)",
                       (None, x, y))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_3_1_2(x, y):
    sql.execute(
        f"SELECT width FROM thermal_calculation_basement_underground_2 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql.execute("INSERT INTO thermal_calculation_basement_underground_2 VALUES (?, ?, ?)",
                (None, x, y))  # запись данных в таблицу
    con.commit()  # подтверждение действий с БД

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_basement_underground_2 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_condition_basement_underground_2 VALUES (?, ?, ?)",
                       (None, x, y))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_3_1_3(x, y):
    sql.execute(
        f"SELECT width FROM thermal_calculation_basement_underground_3 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql.execute("INSERT INTO thermal_calculation_basement_underground_3 VALUES (?, ?, ?)",
                (None, x, y))  # запись данных в таблицу
    con.commit()  # подтверждение действий с БД

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_basement_underground_3 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_condition_basement_underground_3 VALUES (?, ?, ?)",
                       (None, x, y))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_3_1_4(x, y):
    sql.execute(
        f"SELECT width FROM thermal_calculation_basement_underground_4 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql.execute("INSERT INTO thermal_calculation_basement_underground_4 VALUES (?, ?, ?)",
                (None, x, y))  # запись данных в таблицу
    con.commit()  # подтверждение действий с БД

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_basement_underground_4 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_condition_basement_underground_4 VALUES (?, ?, ?)",
                       (None, x, y))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_3_2_1(ans):
    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_basement_underground_1 WHERE width = '{ans}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_3_2_2(ans):
    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_basement_underground_2 WHERE width = '{ans}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_3_2_3(ans):
    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_basement_underground_3 WHERE width = '{ans}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_3_2_4(ans):
    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_basement_underground_4 WHERE width = '{ans}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_1 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


# ----------------------------------------------------------------------------------------------------------------------

def data_base_4_1(x, y):
    sql.execute(f"SELECT width FROM thermal_calculation_overlap_over_the_underground WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql.execute("INSERT INTO thermal_calculation_overlap_over_the_underground VALUES (?, ?, ?)",
                (None, x, y))  # запись данных в таблицу
    con.commit()  # подтверждение действий с БД

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_overlap_over_the_underground WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_condition_overlap_over_the_underground VALUES (?, ?, ?)",
                       (None, x, y))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_4_2(ans):
    sql_result.execute(f"SELECT width FROM thermal_calculation_condition_overlap_over_the_underground "
                       f"WHERE width = '{ans}'")  # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_2 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


# ----------------------------------------------------------------------------------------------------------------------

def data_base_5_1_1(x, y):
    sql.execute(f"SELECT width FROM thermal_calculation_of_the_basement_floor_1 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql.execute("INSERT INTO thermal_calculation_of_the_basement_floor_1 VALUES (?, ?, ?)",
                (None, x, y))  # запись данных в таблицу
    con.commit()  # подтверждение действий с БД

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_of_the_basement_floor_1 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_condition_of_the_basement_floor_1 VALUES (?, ?, ?)",
                       (None, x, y))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_5_1_2(x, y):
    sql.execute(f"SELECT width FROM thermal_calculation_of_the_basement_floor_2 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql.execute("INSERT INTO thermal_calculation_of_the_basement_floor_2 VALUES (?, ?, ?)",
                (None, x, y))  # запись данных в таблицу
    con.commit()  # подтверждение действий с БД

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_of_the_basement_floor_2 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_condition_of_the_basement_floor_2 VALUES (?, ?, ?)",
                       (None, x, y))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_5_1_3(x, y):
    sql.execute(f"SELECT width FROM thermal_calculation_of_the_basement_floor_3 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql.execute("INSERT INTO thermal_calculation_of_the_basement_floor_3 VALUES (?, ?, ?)",
                (None, x, y))  # запись данных в таблицу
    con.commit()  # подтверждение действий с БД

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_of_the_basement_floor_3 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_condition_of_the_basement_floor_3 VALUES (?, ?, ?)",
                       (None, x, y))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_5_1_4(x, y):
    sql.execute(f"SELECT width FROM thermal_calculation_of_the_basement_floor_4 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql.execute("INSERT INTO thermal_calculation_of_the_basement_floor_4 VALUES (?, ?, ?)",
                (None, x, y))  # запись данных в таблицу
    con.commit()  # подтверждение действий с БД

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_of_the_basement_floor_4 WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_condition_of_the_basement_floor_4 VALUES (?, ?, ?)",
                       (None, x, y))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_5_2_1(ans):
    sql_result.execute(f"SELECT width FROM thermal_calculation_condition_of_the_basement_floor_1 "
                       f"WHERE width = '{ans}'")  # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_2 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_5_2_2(ans):
    sql_result.execute(f"SELECT width FROM thermal_calculation_condition_of_the_basement_floor_2 "
                       f"WHERE width = '{ans}'")  # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_2 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_5_2_3(ans):
    sql_result.execute(f"SELECT width FROM thermal_calculation_condition_of_the_basement_floor_3 "
                       f"WHERE width = '{ans}'")  # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_2 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_5_2_4(ans):
    sql_result.execute(f"SELECT width FROM thermal_calculation_condition_of_the_basement_floor_4 "
                       f"WHERE width = '{ans}'")  # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_2 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


# ----------------------------------------------------------------------------------------------------------------------

def data_base_6_1(x, y):
    sql.execute(f"SELECT width FROM thermal_calculation_of_the_attic_floor WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql.execute("INSERT INTO thermal_calculation_of_the_attic_floor VALUES (?, ?, ?)",
                (None, x, y))  # запись данных в таблицу
    con.commit()  # подтверждение действий с БД

    sql_result.execute(
        f"SELECT width FROM thermal_calculation_condition_of_the_attic_floor WHERE width = '{x}'")
    # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_condition_of_the_attic_floor VALUES (?, ?, ?)",
                       (None, x, y))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


def data_base_6_2(ans):
    sql_result.execute(f"SELECT width FROM thermal_calculation_condition_of_the_attic_floor "
                       f"WHERE width = '{ans}'")  # выбор столбца для записи данных в таблицу
    sql_result.execute("INSERT INTO thermal_calculation_result_1_2 VALUES (?, ?)",
                       (None, ans))  # запись данных в таблицу
    con_result.commit()  # подтверждение действий с БД


# ----------------------------------------------------------------------------------------------------------------------

