# 1. Отдельный класс с формулой расчета функции
# 2. Класс принимающий значение характеристик шара
# 3. Функция которая записывет данные в бд


class Therm1_Math:
    def __init__(self, x, y):
        self.R_e = x / y
        print(x / y)


class Therm1_Logic:
    def __init__(self, z1, z2):
        self.z1 = z1
        self.z2 = z2
        self.list = []

    def therm_calc(self, x, y):
        self.list.append(Therm1_Math(x, y))

    def dbn_calc(self):
        return (1 / self.z1) + (1 / self.z2)

    def full_formul_calc(self):
        new_formul_calc = self.dbn_calc()
        for i in self.list:
            new_formul_calc += i.R_e
        return new_formul_calc
