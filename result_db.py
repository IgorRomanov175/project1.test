import sqlite3 as sq

with sq.connect('result.db') as con_result:
    sql_result = con_result.cursor()

    # ------------------------------------------------------------------------------------------------------------------

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_result_1_1 (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           thermal_calculation_name STRING,
                           thermal_calculation_result FLOAT
                           )""")

    con_result.commit()

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_result_1_2 (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           thermal_calculation_name STRING,
                           thermal_calculation_result FLOAT
                           )""")

    con_result.commit()

    sql_result.execute(""" CREATE TABLE IF NOT EXISTS thermal_calculation_result_1_3 (
                           name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           thermal_calculation_name STRING,
                           thermal_calculation_result FLOAT
                           )""")

    con_result.commit()


# -----------------------------------------------------------------------------------------------------------------------

def thermal_calculation_condition_inside_wall():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок зовнішніх стін" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_inside_wall_zero():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок зовнішньої стіни нижче відмітки 0.00" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_basement_underground_1():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для I зони" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_basement_underground_2():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для II зони" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_basement_underground_3():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для III зони" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_basement_underground_4():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок стін підвалу нижче поверхні землі для IV зони" """)
    for result in sql_result:
        return result[0]


def heat_transfer_resistance_of_external_walls_condition():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Розрахунок приведеного опору теплопередачі зовнішніх стін" """)
    for result in sql_result:
        return result[0]


# -----------------------------------------------------------------------------------------------------------------------

def thermal_calculation_condition_of_the_attic_floor():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок горищного покриття" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_overlap_over_the_underground():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок над підвалом та техпідпіллям" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_of_the_basement_floor_1():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для I зони" """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_of_the_basement_floor_2():
    sql_result.execute("""
        SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для II зони" 
        """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_of_the_basement_floor_3():
    sql_result.execute("""
        SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для III зони" 
        """)
    for result in sql_result:
        return result[0]


def thermal_calculation_condition_of_the_basement_floor_4():
    sql_result.execute("""
        SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для IV зони" 
        """)
    for result in sql_result:
        return result[0]


def heat_transfer_resistance_of_the_basement_floors_condition():
    sql_result.execute("""
        SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Теплотехнічний розрахунок підлоги підвалу" 
        """)
    for result in sql_result:
        return result[0]


# ----------------------------------------------------------------------------------------------------------------------


def total_heat_transfer_coefficient_of_the_house_condition():
    sql_result.execute("""
        SELECT thermal_calculation_result FROM thermal_calculation_result_1_1
        WHERE thermal_calculation_name = "Загальний коефіцієнт теплопередачі" 
        """)
    for result in sql_result:
        return result[0]


# ----------------------------------------------------------------------------------------------------------------------


def coefficient_of_glazing_of_the_facade():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_2
        WHERE thermal_calculation_name = "Коефіцієнт скління фасаду" """)
    for result in sql_result:
        return result[0]


def indicator_of_compactness_of_the_building():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_2
        WHERE thermal_calculation_name = "Показник компактності будинку" """)
    for result in sql_result:
        return result[0]


# ----------------------------------------------------------------------------------------------------------------------


def heat_consumption_of_the_house_through_the_enclosure_condition():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_3
        WHERE thermal_calculation_name = "Тепловитрати будинку через огороджувальну оболонку" """)
    for result in sql_result:
        return result[0]


def domestic_heat_during_the_heating_season_condition():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_3
        WHERE thermal_calculation_name = "Побутове надходження тепла протягом опалювального сезону" """)
    for result in sql_result:
        return result[0]


def heat_flow_through_the_windows_condition():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_3
        WHERE thermal_calculation_name = "Теплові надходження через вікна від сонячної радіації" """)
    for result in sql_result:
        return result[0]


def heat_consumption_for_heating_the_building_condition():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_3
        WHERE thermal_calculation_name = "Розрахункові витрати теплової енергії" """)
    for result in sql_result:
        return result[0]


def heat_consumption_and_supply_of_heating_period_condition():
    sql_result.execute(
        """SELECT thermal_calculation_result FROM thermal_calculation_result_1_3
        WHERE thermal_calculation_name = "Розрахункове значення питомих тепловитрат і теплонадходжень будинку" """)
    for result in sql_result:
        return result[0]
