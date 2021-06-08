import sqlite3 as sq

with sq.connect('main_body.db') as con:
    sql = con.cursor()
    # con.row_factory = sq.Row
    # sql.execute("DROP TABLE thermal_calculation")

#-----------------------------------------------------------------------------------------------------------------------

    sql.execute(""" CREATE TABLE IF NOT EXISTS heat_transfer_coefficient (
                    name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name STRING,
                    internal FLOAT,
                    external FLOAT
                    )""")

    con.commit()

    sql.execute(""" CREATE TABLE IF NOT EXISTS calculation_coefficient (
                    name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name STRING,
                    coefficient FLOAT
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
            WHERE name_id = 5 """)
        for result in sql:
            return result[1]


    def heat_transfer_coefficient5_2():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 5 """)
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

#-----------------------------------------------------------------------------------------------------------------------

    def calculation_coefficient_1():
        sql.execute(
            """SELECT coefficient FROM calculation_coefficient
            WHERE name =  "calculation_coefficient_1" """)
        for result in sql:
            return result[0]

