class Therm3_Math1:
    def __init__(self, x1, y1):
        self.x = y1 / x1


class Therm3_Math2:
    def __init__(self, linear_coeff, linear_lenth):
        self.y = linear_coeff * linear_lenth


class Therm3_Math3:
    def __init__(self, point_coeff, point_num):
        self.z = point_coeff * point_num


class Therm3_logic:
    def __init__(self, area):
        self.zero = 0
        self.area = area
        self.list1 = []
        self.list2 = []
        self.list3 = []

    def therm_calc1(self, x1, y1):
        self.list1.append(Therm3_Math1(x1, y1))

    def therm_calc2(self, linear_coeff, linear_lenth):
        self.list2.append(Therm3_Math2(linear_coeff, linear_lenth))

    def therm_calc3(self, point_coeff, point_num):
        self.list3.append(Therm3_Math3(point_coeff, point_num))

    def area1(self):
        return self.zero

    def therm_calc_all1(self):
        new_formul_calc = self.area1()
        for i in self.list1:
            new_formul_calc += i.x
        return new_formul_calc

    def therm_calc_all2(self):
        new_formul_calc = self.therm_calc_all1()
        for i in self.list2:
            new_formul_calc += i.y
        return new_formul_calc

    def therm_calc_all3(self):
        new_formul_calc = self.therm_calc_all2()
        for i in self.list3:
            new_formul_calc += i.z
        return new_formul_calc

    def therm_calc_all4(self):
        full_ansver = self.therm_calc_all3()
        return self.area / full_ansver
