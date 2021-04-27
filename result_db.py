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


def thermal_calculation_condition_basement_underground():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "thermal_calculation_basement_underground_1" """)
    for result in sql_result:
        return result[0]


value1_1 = thermal_calculation_condition_inside_wall()
value1_2 = thermal_calculation_condition_inside_wall_zero()
value1_3 = thermal_calculation_condition_basement_underground()


# -----------------------------------------------------------------------------------------------------------------------

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


value2_1 = thermal_calculation_condition_of_the_basement_floor_1()
value2_2 = thermal_calculation_condition_of_the_basement_floor_2()
value2_3 = thermal_calculation_condition_of_the_basement_floor_3()
value2_4 = thermal_calculation_condition_of_the_basement_floor_4()

# ----------------------------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------------------------
