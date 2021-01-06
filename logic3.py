class Therm3_Math1:
    def __init__(self, x1, x2, x3, x4, x5, x6, x7):
        self.x = x1 + x2 + x3 + x4 + x5 + x6 + x7
        print(x1 + x2 + x3 + x4 + x5 + x6 + x7)


class Therm3_Math2:
    def __init__(self, linear_coeff, linear_lenth):
        self.y = linear_coeff * linear_lenth
        print(linear_coeff * linear_lenth)


class Therm3_Math3:
    def __init__(self, point_coeff, point_num):
        self.z = point_coeff * point_num
        print(point_coeff * point_num)


class Therm3_logic:
    def __init__(self, area):
        self.area = area
        self.list1 = []
        self.list2 = []
        self.list3 = []

    def therm_calc1(self, x1, x2, x3, x4, x5, x6, x7):
        self.list1.append(Therm3_Math1(x1, x2, x3, x4, x5, x6, x7))

    def therm_calc2(self, linear_coeff, linear_lenth):
        self.list2.append(Therm3_Math2(linear_coeff, linear_lenth))

    def therm_calc3(self, point_coeff, point_num):
        self.list3.append(Therm3_Math3(point_coeff, point_num))
