from main_body_logic1 import *
from main_body_logic2 import *


class MainMenu:
    def __init__(self, choose_action):
        self.choose_action = choose_action
        if choose_action == 1:
            thermal_calculation_inside_wall()
            thermal_calculation_inside_wall_zero()
            a = int(input("Оберіть зону теплотехнічного розрахунку стін підвалу нижче поверхні землі:"
                          "1 - I зона"
                          "2 - II зона"
                          "3 - III зона"
                          "4 - IV зона"
                          "- "))
            if a == 1:
                thermal_calculation_basement_underground_1()
            if a == 2:
                thermal_calculation_basement_underground_2()
            if a == 3:
                thermal_calculation_basement_underground_3()
            if a == 4:
                thermal_calculation_basement_underground_4()
            heat_transfer_resistance_of_external_walls()

            thermal_calculation_of_the_attic_floor()
            thermal_calculation_overlap_over_the_underground()
            thermal_calculation_of_the_basement_floor()

            con.commit()
            con_result.commit()

            con.close()
            con_result.close()

        if self.choose_action == 2:
            sql.execute("DROP TABLE thermal_calculation_inside_wall")
            sql.execute("DROP TABLE thermal_calculation_inside_wall_zero")
            sql.execute("DROP TABLE thermal_calculation_basement_underground_1")
            sql.execute("DROP TABLE thermal_calculation_basement_underground_2")
            sql.execute("DROP TABLE thermal_calculation_basement_underground_3")
            sql.execute("DROP TABLE thermal_calculation_basement_underground_4")
            sql.execute("DROP TABLE thermal_calculation_of_the_attic_floor")
            sql.execute("DROP TABLE thermal_calculation_overlap_over_the_underground")
            sql.execute("DROP TABLE thermal_calculation_of_the_basement_floor_1")
            sql.execute("DROP TABLE thermal_calculation_of_the_basement_floor_2")
            sql.execute("DROP TABLE thermal_calculation_of_the_basement_floor_3")
            sql.execute("DROP TABLE thermal_calculation_of_the_basement_floor_4")

            sql_result.execute("DROP TABLE thermal_calculation_condition_inside_wall")
            sql_result.execute("DROP TABLE thermal_calculation_condition_inside_wall_zero")
            sql_result.execute("DROP TABLE thermal_calculation_condition_basement_underground_1")
            sql_result.execute("DROP TABLE thermal_calculation_condition_basement_underground_2")
            sql_result.execute("DROP TABLE thermal_calculation_condition_basement_underground_3")
            sql_result.execute("DROP TABLE thermal_calculation_condition_basement_underground_4")
            sql_result.execute("DROP TABLE thermal_calculation_condition_of_the_attic_floor")
            sql_result.execute("DROP TABLE thermal_calculation_condition_overlap_over_the_underground")
            sql_result.execute("DROP TABLE thermal_calculation_condition_of_the_basement_floor_1")
            sql_result.execute("DROP TABLE thermal_calculation_condition_of_the_basement_floor_2")
            sql_result.execute("DROP TABLE thermal_calculation_condition_of_the_basement_floor_3")
            sql_result.execute("DROP TABLE thermal_calculation_condition_of_the_basement_floor_4")


            sql_result.execute("DROP TABLE thermal_calculation_result_1_1")
            sql_result.execute("DROP TABLE thermal_calculation_result_1_2")

        if self.choose_action == 3:
            return


if __name__ == '__main__':
    start = int(input("""
        Выберите действие:
        1.Продолжить со старой таблицой;
        2.Перезаписать таблицу;
        3.Завершение программы;
        - """))
    main_body_project = MainMenu(start)
