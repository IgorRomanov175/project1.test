from db import *


class DBN_calc:
    #  Формула расчёта данных взятых из таблици heat_transfer_coefficient 1/z1 + 1/z2
    def __init__(self, z1, z2):
        self.z = (1 / z1) + (1 / z2)
        print((1 / z1) + (1 / z2))


class DBN_logic:
    #  изъятие значений z1 и z2 из таблици heat_transfer_coefficient
    def __init__(self, z1, z2):
        self.z1 = z1
        self.z2 = z2
        self.list = []

    def dbn_calc(self, z1, z2):
        self.list.append(DBN_calc(z1, z2))