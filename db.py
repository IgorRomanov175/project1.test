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

    def heat_transfer_coefficient1():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient 
            WHERE name_id = 1 """)
        for result in sql:
            print(result[0])
            
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient 
            WHERE name_id = 1 """)
        for result in sql:
            print(result[0])

    def heat_transfer_coefficient2():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient 
            WHERE name_id = 2 """)
        for result in sql:
            print(result[1])
        
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient 
            WHERE name_id = 2""")
        for result in sql:
            print(result[0])

    def heat_transfer_coefficient3():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 3 """)
        for result in sql:
            print(result[1])
        
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 3 """)
        for result in sql:
            print(result[0])

    def heat_transfer_coefficient4():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 4 """)
        for result in sql:
            print(result[1])
        
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 4 """)
        for result in sql:
            print(result[0])

    def heat_transfer_coefficient5():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 6 """)
        for result in sql:
            print(result[1])

        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 6 """)
        for result in sql:
            print(result[0])

    def heat_transfer_coefficient6():
        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 6 """)
        for result in sql:
            print(result[1])

        sql.execute(
            """SELECT internal, external FROM heat_transfer_coefficient
            WHERE name_id = 6 """)
        for result in sql:
            print(result[0])

value1 = heat_transfer_coefficient1()
print(value1)

value2 = heat_transfer_coefficient2()
print(value2)

value3 = heat_transfer_coefficient3()
print(value3)

value4 = heat_transfer_coefficient4()
print(value4)

value5 = heat_transfer_coefficient5()
print(value5)

value6 = heat_transfer_coefficient6()
print(value6)