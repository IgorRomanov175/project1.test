class Therm2_Math:
    def __init__(self, x, y):
        self.R_e_zero = x / y
        print(x / y)


class Therm2_Logic:
    def __init__(self, z_zero):
        self.z_zero = z_zero
        self.list = []

    def therm2_calc(self, x, y):
        self.list.append(Therm2_Math(x, y))

    def heat_trans_res(self):
        return self.z_zero

    def full_therm2_calc(self):
        new_formul_calc = self.heat_trans_res()
        for i in self.list:
            new_formul_calc += i.R_e_zero
        return new_formul_calc
