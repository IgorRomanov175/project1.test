from mb_logic1 import *
from mb_logic2 import *
from mb_logic3 import *
from mb_logic4 import *


def initial_list():
    ################################################################
    # пункт 3

    # thermal_calculation_inside_wall()
    # thermal_calculation_inside_wall_zero()
    # a = int(input("Оберіть зону теплотехнічного розрахунку стін підвалу нижче поверхні землі:"
    #               "\n1 - I зона"
    #               "\n2 - II зона"
    #               "\n3 - III зона"
    #               "\n4 - IV зона"
    #               "\n- "))
    # if a == 1:
    #     thermal_calculation_basement_underground_1()
    # elif a == 2:
    #     thermal_calculation_basement_underground_2()
    # elif a == 3:
    #     thermal_calculation_basement_underground_3()
    # elif a == 4:
    #     thermal_calculation_basement_underground_4()
    # heat_transfer_resistance_of_external_walls()
    # thermal_calculation_of_the_attic_floor()
    # thermal_calculation_overlap_over_the_underground()
    # b = int(input("Додати розрахунок підлоги підвалу?\n1-ТАК\n2-НІ\n-"))
    # while b == 1:
    #     c = int(input("Оберіть зону теплотехнічного розрахунку підлоги підвалу (підлоги по грунту):"
    #                   "\n1 - I зона"
    #                   "\n2 - II зона"
    #                   "\n3 - III зона"
    #                   "\n4 - IV зона"
    #                   "\n5 - Завершити"
    #                   "\n- "))
    #     if c == 1:
    #         thermal_calculation_of_the_basement_floor_1()
    #     elif c == 2:
    #         thermal_calculation_of_the_basement_floor_2()
    #     elif c == 3:
    #         thermal_calculation_of_the_basement_floor_3()
    #     elif c == 4:
    #         thermal_calculation_of_the_basement_floor_4()
    #     else:
    #         break
    # heat_transfer_resistance_of_the_basement_floors()
    # min_ht_resistance_of_external_enclosing_structures()
    #
    # ##################################################
    # # пункт 4
    #
    # coefficient_glazing_of_the_facade()
    #
    # #################################################
    # # пункт 5
    #
    # heat_consumption_of_the_house_through_the_enclosure()
    # domestic_heat_during_the_heating_season()
    # heat_flow_through_the_windows()
    # heat_consumption_for_heating_the_building()
    # heat_consumption_and_supply_of_heating_period()

    ##################################################
    # пункт 6

    energy_efficiency_class()

    con.commit()
    con_result.commit()

    con.close()
    con_result.close()
