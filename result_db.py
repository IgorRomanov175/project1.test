import sqlite3 as sq

with sq.connect('result.db') as con_result:
    sql_result = con_result.cursor()

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_condition (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           width FLOAT,
                           thermal_conductivity FLOAT
                       )""")

    con_result.commit()

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_result (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           thermal_calculation_result FLOAT
                           )""")

    con_result.commit()