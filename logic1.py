# 1. Отдельный класс с формулой расчета функции
# 2. Класс принимающий значение характеристик шара
# 3. Функция которая записывет данные в бд


class Therm1_Math:
    def __init__(self, x, y):
        self.R_e = x / y
        print(x / y)


class Therm1_Logic:
    def __init__(self, x, y):
        self.width = x
        self.thermal_conductivity = y
        self.list = []

    def therm_calc(self, x, y):
        self.list.append(Therm1_Math(x, y))


#  таски: к методу full_therm_calc подвязать таблицу heat_transfer_coefficient импортировав модуль db в этот файл
#  методом перебора for i in self.list собрать общее значение термического оперения
