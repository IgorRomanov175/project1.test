from mb_initial_list import *


class MainMenu:
    def __init__(self, choose_action):
        self.choose_action = choose_action
        if choose_action == 1:
            initial_list()

        if self.choose_action == 2:
            sql_result.execute("DROP TABLE thermal_calculation_result_1_1")
            sql_result.execute("DROP TABLE thermal_calculation_result_1_2")
            sql_result.execute("DROP TABLE thermal_calculation_result_1_3")
            sql.execute("DROP TABLE calculation_coefficient")

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
