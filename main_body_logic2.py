from main_body_logic_template import *


# пункт 3.2
def thermal_calculation_of_the_attic_floor():
    thermal_calculation_template_1(
        x1="Теплотехнічний розрахунок горищного покриття",
        x2=heat_transfer_coefficient3_1(),
        x3=heat_transfer_coefficient3_2()
    )


# пункт 3.3
def thermal_calculation_overlap_over_the_underground():
    thermal_calculation_template_1(
        x1="Теплотехнічний розрахунок над підвалом та техпідпіллям",
        x2=heat_transfer_coefficient4_1(),
        x3=heat_transfer_coefficient4_2()
    )


# пункт 3.4
def thermal_calculation_of_the_basement_floor_1():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для I зони"
    )


def thermal_calculation_of_the_basement_floor_2():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для II зони"
    )


def thermal_calculation_of_the_basement_floor_3():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для III зони"
    )


def thermal_calculation_of_the_basement_floor_4():
    thermal_calculation_template_2(
        x1="Теплотехнічний розрахунок підлоги підвалу (підлога по грунту) для IV зони"
    )