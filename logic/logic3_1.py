class Therm3_Math1:
    def __init__(self, x1, y1):
        self.x = y1 / x1


class Therm3_1_logic:
    def __init__(self, area):
        self.zero = 0
        self.area = area
        self.list1 = []

    def therm_calc1(self, x1, y1):
        self.list1.append(Therm3_Math1(x1, y1))

    def area1(self):
        return self.zero

    def therm_calc_all1(self):
        new_formul_calc = self.area1()
        for i in self.list1:
            new_formul_calc += i.x
        return new_formul_calc

    def therm_calc_all2(self):
        full_ansver = self.therm_calc_all1()
        return self.area / full_ansver
