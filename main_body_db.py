import sqlite3 as sq

with sq.connect('main_body.db') as con:
    sql = con.cursor()
    # con.row_factory = sq.Row
    # sql.execute("DROP TABLE thermal_calculation")

    sql.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_inside_wall (
                    name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    width FLOAT,
                    thermal_conductivity FLOAT
                    )""")

    con.commit()

    sql.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_inside_wall_zero (
                    name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    width FLOAT,
                    thermal_conductivity FLOAT
                    )""")

    con.commit()

    sql.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_basement_underground (
                    name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    width FLOAT,
                    thermal_conductivity FLOAT
                    )""")

    con.commit()

    sql.execute(""" CREATE TABLE IF NOT EXISTS heat_transfer_coefficient (
                    name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name STRING,
                    internal FLOAT,
                    external FLOAT
                    )""")

    con.commit()

    sql.execute("""CREATE TABLE IF NOT EXISTS linear_heat_transfer_coefficient (
                   name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name	STRING,
                   heat_transfer FLOAT,
                   brand_of_concreete TEXT,
                   mm30 FLOAT,
                   mm50 FLOAT,
                   mm80 FLOAT,
                   mm100 FLOAT,
                   mm120 FLOAT,
                   mm150 FLOAT,
                   mm180 FLOAT,
                   mm200 FLOAT,
                   mm250 FLOAT,
                   mm300 FLOAT,
                   mm400 FLOAT,
                   mm500 FLOAT
                   )""")
    con.commit()


    def heat_transfer_coefficient1_1():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient 
            WHERE name_id = 1 """)
        for result in sql:
            return result[1]


    def heat_transfer_coefficient1_2():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient 
            WHERE name_id = 1 """)
        for result in sql:
            return result[0]


    def heat_transfer_coefficient2_1():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient 
            WHERE name_id = 2 """)
        for result in sql:
            return result[1]


    def heat_transfer_coefficient2_2():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient 
            WHERE name_id = 2""")
        for result in sql:
            return result[0]


    def heat_transfer_coefficient3_1():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 3 """)
        for result in sql:
            return result[1]


    def heat_transfer_coefficient3_2():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 3 """)
        for result in sql:
            return result[0]


    def heat_transfer_coefficient4_1():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 4 """)
        for result in sql:
            return result[1]


    def heat_transfer_coefficient4_2():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 4 """)
        for result in sql:
            return result[0]


    def heat_transfer_coefficient5_1():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 6 """)
        for result in sql:
            return result[1]


    def heat_transfer_coefficient5_2():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 6 """)
        for result in sql:
            return result[0]


    def heat_transfer_coefficient6_1():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 6 """)
        for result in sql:
            return result[1]


    def heat_transfer_coefficient6_2():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 6 """)
        for result in sql:
            return result[0]


def linear_heat_transfer_coefficient1_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 1 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient1_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 2 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient1_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 3 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient2_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 4 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient2_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 5 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient2_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 6 """)
    res = int(input("""
        1 -- 120mm
        2 -- 150mm
        3 -- 180mm
        -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient3_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 7 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient3_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 8 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient3_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 9 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient5_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 10 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient5_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 11 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient5_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 12 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient6_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 13 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient6_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 14 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient6_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 15 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient8_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 16 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient8_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 17 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient8_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 18 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient9_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 19 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient9_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 20 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient9_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 21 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient11_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 22 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient11_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 23 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient11_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 24 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient12_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 25 """)
    res = int(input("""
    1 -- 150mm
    2 -- 200mm
    3 -- 250mm
    -"""))
    if res == 1:
        for result in sql:
            return result[8]
    if res == 2:
        for result in sql:
            return result[10]
    if res == 3:
        for result in sql:
            return result[11]


def linear_heat_transfer_coefficient12_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 26 """)
    res = int(input("""
    1 -- 150mm
    2 -- 200mm
    3 -- 250mm
    -"""))
    if res == 1:
        for result in sql:
            return result[8]
    if res == 2:
        for result in sql:
            return result[10]
    if res == 3:
        for result in sql:
            return result[11]


def linear_heat_transfer_coefficient12_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 27 """)
    res = int(input("""
    1 -- 150mm
    2 -- 200mm
    3 -- 250mm
    -"""))
    if res == 1:
        for result in sql:
            return result[8]
    if res == 2:
        for result in sql:
            return result[10]
    if res == 3:
        for result in sql:
            return result[11]


def linear_heat_transfer_coefficient14():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 28 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient15():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 29 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient16():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 30 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient4_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 31 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient4_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 32 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient4_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 33 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient7_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 34 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient7_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 35 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient7_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 36 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient10_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 37 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient10_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 38 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient10_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 39 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient13_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 40 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient13_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 41 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient13_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 42 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient17():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 43 """)
    res = int(input("""
    1 -- 150mm
    2 -- 200mm
    3 -- 250mm
    -"""))
    if res == 1:
        for result in sql:
            return result[8]
    if res == 2:
        for result in sql:
            return result[10]
    if res == 3:
        for result in sql:
            return result[11]


def linear_heat_transfer_coefficient18():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 44 """)
    res = int(input("""
    1 -- 150mm
    2 -- 200mm
    3 -- 250mm
    -"""))
    if res == 1:
        for result in sql:
            return result[8]
    if res == 2:
        for result in sql:
            return result[10]
    if res == 3:
        for result in sql:
            return result[11]


def linear_heat_transfer_coefficient19():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 45 """)
    res = int(input("""
    1 -- 150mm
    2 -- 200mm
    3 -- 250mm
    -"""))
    if res == 1:
        for result in sql:
            return result[8]
    if res == 2:
        for result in sql:
            return result[10]
    if res == 3:
        for result in sql:
            return result[11]


def linear_heat_transfer_coefficient20():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 46 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient21():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 47 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient22():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 48 """)
    res = int(input("""
    1 -- 300mm
    2 -- 400mm
    3 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[12]
    if res == 2:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient23():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 49 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient24():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 50 """)
    res = int(input("""
    1 -- 150mm
    2 -- 200mm
    3 -- 250mm
    -"""))
    if res == 1:
        for result in sql:
            return result[8]
    if res == 2:
        for result in sql:
            return result[10]
    if res == 3:
        for result in sql:
            return result[11]


def linear_heat_transfer_coefficient25():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 51 """)
    res = int(input("""
    1 -- 150mm
    2 -- 200mm
    3 -- 250mm
    -"""))
    if res == 1:
        for result in sql:
            return result[8]
    if res == 2:
        for result in sql:
            return result[10]
    if res == 3:
        for result in sql:
            return result[11]


def linear_heat_transfer_coefficient26():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 52 """)
    res = int(input("""
    1 -- 100mm
    2 -- 150mm
    3 -- 200mm
    -"""))
    if res == 1:
        for result in sql:
            return result[6]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[10]


def linear_heat_transfer_coefficient27():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 53 """)
    res = int(input("""
    1 -- 100mm
    2 -- 150mm
    3 -- 200mm
    -"""))
    if res == 1:
        for result in sql:
            return result[6]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[10]


def linear_heat_transfer_coefficient28():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 54 """)
    res = int(input("""
    1 -- 100mm
    2 -- 150mm
    3 -- 200mm
    -"""))
    if res == 1:
        for result in sql:
            return result[6]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[10]


def linear_heat_transfer_coefficient29():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 55 """)
    res = int(input("""
    1 -- 100mm
    2 -- 150mm
    3 -- 200mm
    -"""))
    if res == 1:
        for result in sql:
            return result[6]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[10]


def linear_heat_transfer_coefficient30_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 56 """)
    res = int(input("""
    1 -- 30mm
    2 -- 50mm
    3 -- 80mm
    -"""))
    if res == 1:
        for result in sql:
            return result[3]
    if res == 2:
        for result in sql:
            return result[4]
    if res == 3:
        for result in sql:
            return result[5]


def linear_heat_transfer_coefficient30_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 57 """)
    res = int(input("""
    1 -- 30mm
    2 -- 50mm
    3 -- 80mm
    -"""))
    if res == 1:
        for result in sql:
            return result[3]
    if res == 2:
        for result in sql:
            return result[4]
    if res == 3:
        for result in sql:
            return result[5]


def linear_heat_transfer_coefficient30_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 58 """)
    res = int(input("""
    1 -- 30mm
    2 -- 50mm
    3 -- 80mm
    -"""))
    if res == 1:
        for result in sql:
            return result[3]
    if res == 2:
        for result in sql:
            return result[4]
    if res == 3:
        for result in sql:
            return result[5]


def linear_heat_transfer_coefficient31():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 59 """)
    res = int(input("""
    1 -- 100mm
    2 -- 150mm
    3 -- 200mm
    -"""))
    if res == 1:
        for result in sql:
            return result[6]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[10]


def linear_heat_transfer_coefficient32():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 68 """)
    res = int(input("""
    1 -- 30mm
    2 -- 50mm
    3 -- 80mm
    4 -- 100mm
    5 -- 120mm
    6 -- 150mm
    7 -- 180mm
    8 -- 200mm
    9 -- 250mm
    10 -- 300mm
    11 -- 400mm
    12 -- 500mm
    -"""))
    if res == 1:
        for result in sql:
            return result[3]
    if res == 2:
        for result in sql:
            return result[4]
    if res == 3:
        for result in sql:
            return result[5]
    if res == 3:
        for result in sql:
            return result[6]
    if res == 3:
        for result in sql:
            return result[7]
    if res == 3:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]
    if res == 3:
        for result in sql:
            return result[10]
    if res == 3:
        for result in sql:
            return result[11]
    if res == 3:
        for result in sql:
            return result[12]
    if res == 3:
        for result in sql:
            return result[13]
    if res == 3:
        for result in sql:
            return result[14]


def linear_heat_transfer_coefficient33():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 70 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient34():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 60 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient35():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 61 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient36_1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 62 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient36_2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 63 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def linear_heat_transfer_coefficient36_3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 64 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def dot_heat_transfer_coefficient1():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 65 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def dot_heat_transfer_coefficient2():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 66 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def dot_heat_transfer_coefficient3():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 67 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


def dot_heat_transfer_coefficient4():
    sql.execute(
        """SELECT name, heat_transfer, brand_of_concreete, mm30, mm50, mm80, mm100, mm120, mm150, mm180, 
         mm200, mm250, mm300, mm400, mm500 FROM linear_heat_transfer_coefficient 
         WHERE name_id = 69 """)
    res = int(input("""
    1 -- 120mm
    2 -- 150mm
    3 -- 180mm
    -"""))
    if res == 1:
        for result in sql:
            return result[7]
    if res == 2:
        for result in sql:
            return result[8]
    if res == 3:
        for result in sql:
            return result[9]


