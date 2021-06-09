import json

with open("C:\Python_project\project1.test\json\init_main_data_1.json", "r") as json_file:
    data_json = json.load(json_file)

# Площі
calc_area_1 = data_json["area"]["calc_area_1"]  # Площа зовнішніх стін
calc_area_1_1 = data_json["area"]["calc_area_1_1"]  # Площа зовнішніх стін нижче відмітки 0.00
calc_area_1_2 = data_json["area"]["calc_area_1_2"]  # Площа стін підвалу нижче поверхні землі
calc_area_2 = data_json["area"]["calc_area_2"]  # Площа перекриття над підвалом, техпідпіллям
calc_area_3_1 = data_json["area"]["calc_area_3_1"]
calc_area_3_2 = data_json["area"]["calc_area_3_2"]
calc_area_3_3 = data_json["area"]["calc_area_3_3"]
calc_area_3_4 = data_json["area"]["calc_area_3_4"]
calc_area_3 = data_json["area"]["calc_area_3"]  # Площа підлоги по грунту
calc_area_4 = data_json["area"]["calc_area_4"]  # Площа горищного перекриття
calc_area_5 = data_json["area"]["calc_area_5"]  # Площа світлопрозорих конструкцій
calc_area_6 = data_json["area"]["calc_area_6"]  # Площа вхідних дверей
calc_area_7 = data_json["area"]["calc_area_7"]  # РОзрахункова площа будинку
calc_all_initial = calc_area_1 + calc_area_2 + calc_area_3 + calc_area_4 + calc_area_5 + calc_area_6

########################################################################################################################

# Об'єм

calc_volume_1 = data_json["volume"]  # Опалювальний об'єм будинку
########################################################################################################################

# Пункт 3.7

r_t_s = data_json["paragraph_3_7"]["formula_5"]["r_t_s"]  # опір світлопрозорих конструкцій
r_d = data_json["paragraph_3_7"]["formula_5"]["r_d"]  # опір дверей
e = data_json["paragraph_3_7"]["formula_5"]["e"]

########################################################################################################################

# пункт 5 формула (3) ДСТУ_Н Б.А.2.2-5

z_op = data_json["paragraph_5"]["formula_3"]["z_op"]  # Тривалість опалювального періоду
t_v = data_json["paragraph_5"]["formula_3"]["t_v"]  # Розрахункова температура внутрішнього повітря будівлі
t_n = data_json["paragraph_5"]["formula_3"]["t_n"]
t_z = data_json["paragraph_5"]["formula_3"]["t_z"]
t_op = data_json["paragraph_5"]["formula_3"]["t_op"]  # Розрахункова температура зовнішнього повітря
d_d = (t_v - t_op) * z_op  # Кількість градусо_діб
x1 = 0.024  # розмірний коефіцієнт

########################################################################################################################

# пункт 3.7 формула (12) ДСТУ_Н Б.А.2.2-5

l_v = 7 * calc_area_7  # нормативне значення кількості припливного повітря під час механічної вентиляції
n_v = data_json["paragraph_3_7"]["formula_12"]["n_v"]  # Кількість годин механічної вентиляції протягом тижня
nu = data_json["paragraph_3_7"]["formula_12"]["nu"]
# Коефіцієнт впливу зустрічного теплового потоку в огороджувальні конструкції
n_inf = (168 - n_v)  # Кількість годин інфільтрації протягом тижня
v_v = data_json["paragraph_3_7"]["formula_12"]["v_v"]  # Коефіцієнт зниження об'єму повітря у будинку
p_inf = 0.5 * v_v * calc_volume_1  # Кількість повітря, що інфільтрується в будинок через огороджувальні конструкції

########################################################################################################################

# пункт 5 формула (8) ДСТУ_Н Б.А.2.2-5

x2 = 0.278  # розмірний коефіцієнт
c = 1  # питома теплоємність повітря

########################################################################################################################

# пункт 5 формула (14) ДСТУ_Н Б.А.2.2-5

e_v_in = data_json["paragraph_5"]["formula_14"]["e_v_in"]  #
e_v_out = data_json["paragraph_5"]["formula_14"]["e_v_out"]  #

########################################################################################################################

# пункт 5 формула (2) ДСТУ_Н Б.А.2.2-5

v_coef = data_json["paragraph_5"]["formula_2"]["v_coef"]  # коефіцієнт, що враховує здатність огороджувальних
# конструкцій акумулювати або віддавати тепло під час періодичного теплового режиму
eps_coef = data_json["paragraph_5"]["formula_2"]["eps_coef"]  # коефіцієнт авторегулювання подачі тепла в сис. опалення
beta_h_coef = data_json["paragraph_5"]["formula_2"]["beta_h_coef"]  # коефіцієнт, що враховує додаткове теплоспожив системи
# опалення, пов'язане з дискретністю номінального теплового потоку номенклатурного ряду опалювальних приладів
# та додатковими тепловитратами через неопалювальні приміщення

########################################################################################################################

#  кортежи информации для пунктов 3.1.1 , 3.1.2, 3.2, 3.3

thermal_calculation_inside_wall_array = data_json["array_data"]["value_data"]["paragraph_3_1_1"]
thermal_calculation_inside_wall_zero_array = data_json["array_data"]["value_data"]["paragraph_3_1_2"]

thermal_calculation_basement_underground_array = data_json["array_data"]["value_data"]["paragraph_3_1_3"]

thermal_calculation_of_the_attic_floor_array = data_json["array_data"]["value_data"]["paragraph_3_2"]
thermal_calculation_overlap_over_the_underground_array = data_json["array_data"]["value_data"]["paragraph_3_3"]

thermal_calculation_of_the_basement_floor_array = data_json["array_data"]["value_data"]["paragraph_3_4"]

######################################################################################################################

# init_data для пунктов 3.1.3, 3.4

init_list_3_1_3 = data_json["array_data"]["init_data"]["paragraph_3_1_3"]

init_list_3_4 = data_json["array_data"]["init_data"]["paragraph_3_4"]

########################################################################################################################

# init data для пункта 3.1.4

init_list_3_1_4 = data_json["array_data"]["init_data"]["paragraph_3_1_4"]
