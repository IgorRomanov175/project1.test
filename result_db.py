import sqlite3 as sq

with sq.connect('result.db') as con_result:
    sql_result = con_result.cursor()

    # -----------------------------------------------------------------------------------------------------------------------

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_result_1_1 (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           thermal_calculation_name STRING,
                           thermal_calculation_result FLOAT
                           )""")

    con_result.commit()


# -----------------------------------------------------------------------------------------------------------------------

def thermal_calculation_condition_inside_wall():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_inside_wall" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_inside_wall_zero():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_inside_wall_zero" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_basement_underground_1():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_basement_underground_1" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_basement_underground_2():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_basement_underground_2" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_basement_underground_3():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_basement_underground_3" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_basement_underground_4():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_basement_underground_4" """)
    for result in sql_result:
        return result[0]


def heat_transfer_resistance_of_external_walls_condition():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "heat_transfer_resistance_of_external_walls" """)
    for result in sql_result:
        return result[0]

# -----------------------------------------------------------------------------------------------------------------------

def thermal_calculation_condition_of_the_attic_floor():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_of_the_attic_floor" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_overlap_over_the_underground():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_overlap_over_the_underground" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_of_the_basement_floor_1():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_of_the_basement_floor_1" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_of_the_basement_floor_2():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_of_the_basement_floor_2" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_of_the_basement_floor_3():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_of_the_basement_floor_3" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_of_the_basement_floor_4():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_of_the_basement_floor_4" """)
    for result in sql_result:
        return result[0]


def heat_transfer_resistance_of_the_basement_floors_condition():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "heat_transfer_resistance_of_the_basement_floors" """)
    for result in sql_result:
        return result[0]


# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
