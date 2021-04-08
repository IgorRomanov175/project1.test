import sqlite3 as sq

with sq.connect('result.db') as con_result:
    sql_result = con_result.cursor()

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_condition_inside_wall (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           width FLOAT,
                           thermal_conductivity FLOAT
                           )""")

    con_result.commit()

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_condition_inside_wall_zero (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           width FLOAT,
                           thermal_conductivity FLOAT
                           )""")

    con_result.commit()

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_condition_basement_underground (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           width FLOAT,
                           thermal_conductivity FLOAT
                           )""")

    con_result.commit()

#-----------------------------------------------------------------------------------------------------------------------

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_condition_of_the_attic_floor (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           width FLOAT,
                           thermal_conductivity FLOAT
                           )""")

    con_result.commit()

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_condition_overlap_over_the_underground (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           width FLOAT,
                           thermal_conductivity FLOAT
                           )""")

    con_result.commit()

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_condition_of_the_basement_floor (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           width FLOAT,
                           thermal_conductivity FLOAT
                           )""")

    con_result.commit()

#-----------------------------------------------------------------------------------------------------------------------

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_result_1_1 (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           thermal_calculation_result FLOAT
                           )""")

    con_result.commit()

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_result_1_2 (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           thermal_calculation_result FLOAT
                           )""")

    con_result.commit()


#-----------------------------------------------------------------------------------------------------------------------

def thermal_calculation_condition_inside_wall():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE name_id = 1 """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_inside_wall_zero():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE name_id = 2 """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_basement_underground():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE name_id = 3 """)
    for result in sql_result:
        return result[0]


value1_1 = thermal_calculation_condition_inside_wall()
print(value1_1)

value1_2 = thermal_calculation_condition_inside_wall_zero()
print(value1_2)

value1_3 = thermal_calculation_condition_basement_underground()
print(value1_3)


#-----------------------------------------------------------------------------------------------------------------------
