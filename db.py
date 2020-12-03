import sqlite3 as sq

with sq.connect('server.db') as con:
    sql = con.cursor()
    # con.row_factory = sq.Row
    # sql.execute("DROP TABLE users")

    sql.execute(""" CREATE TABLE IF NOT EXISTS users (
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

value1_1 = heat_transfer_coefficient1_1()
# print(value1_1)

value1_2 = heat_transfer_coefficient1_2()
# print(value1_2)

value2_1 = heat_transfer_coefficient2_1()
# print(value2_1)

value2_2 = heat_transfer_coefficient2_2()
# print(value2_2)

value3_1 = heat_transfer_coefficient3_1()
# print(value3_1)

value3_2 = heat_transfer_coefficient3_2()
# print(value3_2)

value4_1 = heat_transfer_coefficient4_1()
# print(value4_1)

value4_2 = heat_transfer_coefficient4_2()
# print(value4_2)

value5_1 = heat_transfer_coefficient5_1()
# print(value5_1)

value5_2 = heat_transfer_coefficient5_2()
# print(value5_2)

value6_1 = heat_transfer_coefficient6_1()
# print(value6_1)

value6_2 = heat_transfer_coefficient6_2()
# print(value6_2)