from main_body_logic1 import *
from main_body_logic2 import *


class MainMenu:
    def __init__(self, choose_action):
        self.choose_action = choose_action
        if choose_action == 1:
            thermal_calculation_inside_wall()
            thermal_calculation_inside_wall_zero()
            thermal_calculation_basement_underground()
            heat_transfer_resistance_of_external_walls()

            thermal_calculation_of_the_attic_floor()

            con.commit()
            con_result.commit()

            con.close()
            con_result.close()

        if self.choose_action == 2:
            sql.execute("DROP TABLE thermal_calculation_inside_wall")
            sql.execute("DROP TABLE thermal_calculation_inside_wall_zero")
            sql.execute("DROP TABLE thermal_calculation_basement_underground")

            sql_result.execute("DROP TABLE thermal_calculation_condition_inside_wall")
            sql_result.execute("DROP TABLE thermal_calculation_condition_inside_wall_zero")
            sql_result.execute("DROP TABLE thermal_calculation_condition_basement_underground")

            sql_result.execute("DROP TABLE thermal_calculation_result_1_1")

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
