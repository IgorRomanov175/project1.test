from mb_logic1 import *
from mb_logic2 import *
from mb_logic3 import *
from mb_logic4 import *


def initial_list():
    ################################################################
    # пункт 3

    thermal_calculation_inside_wall()
    thermal_calculation_inside_wall_zero()
    if init_list_3_1_3[0] == 1:
        thermal_calculation_basement_underground_1()
    elif init_list_3_1_3[0] == 2:
        thermal_calculation_basement_underground_2()
    elif init_list_3_1_3[0] == 3:
        thermal_calculation_basement_underground_3()
    elif init_list_3_1_3[0] == 4:
        thermal_calculation_basement_underground_4()
    heat_transfer_resistance_of_external_walls()
    thermal_calculation_of_the_attic_floor()
    thermal_calculation_overlap_over_the_underground()
    a_1 = [thermal_calculation_of_the_basement_floor_1(), thermal_calculation_of_the_basement_floor_2(),
           thermal_calculation_of_the_basement_floor_3(), thermal_calculation_of_the_basement_floor_4()]
    for i in a_1:
        c = i
    heat_transfer_resistance_of_the_basement_floors()
    min_ht_resistance_of_external_enclosing_structures()

    ##################################################
    # пункт 4

    coefficient_glazing_of_the_facade()

    #################################################
    # пункт 5

    heat_consumption_of_the_house_through_the_enclosure()
    domestic_heat_during_the_heating_season()
    heat_flow_through_the_windows()
    heat_consumption_for_heating_the_building()
    heat_consumption_and_supply_of_heating_period()

    ##################################################
    # пункт 6

    energy_efficiency_class()

    con.commit()
    con_result.commit()

    con.close()
    con_result.close()
