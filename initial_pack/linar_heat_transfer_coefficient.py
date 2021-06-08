import json

with open("C:\Python_project\project1.test\json\init_array_data.json", "r") as json_file:
    a = json.load(json_file)

node1 = [[0.080, 0.073, 0.062],
         [0.087, 0.082, 0.069],
         [0.094, 0.090, 0.076]]

node2 = [[0.090, 0.074, 0.062],
         [0.100, 0.082, 0.069],
         [0.110, 0.090, 0.076]]

node3 = [[0.074, 0.056, 0.046],
         [0.082, 0.063, 0.051],
         [0.091, 0.070, 0.056]]

node4 = [[0.147, 0.155, 0.159],
         [0.166, 0.175, 0.179],
         [0.184, 0.193, 0.196]]

node5 = [[0.839, 0.797, 0.758],
         [0.833, 0.793, 0.754],
         [0.827, 0.789, 0.751]]

node6 = [[0.977, 0.922, 0.869],
         [0.970, 0.916, 0.865],
         [0.963, 0.911, 0.86]]

node7 = [[0.710, 0.609, 0.537],
         [0.718, 0.616, 0.543],
         [0.726, 0.623, 0.548]]

node8 = [[0.159, 0.136, 0.121],
         [0.173, 0.150, 0.133],
         [0.187, 0.162, 0.145]]

node9 = [[0.136, 0.113, 0.097],
         [0.150, 0.124, 0.107],
         [0.162, 0.136, 0.117]]

node10 = [[0.174, 0.200, 0.222],
          [0.178, 0.205, 0.228],
          [0.182, 0.210, 0.234]]

node11 = [[0.131, 0.115, 0.103],
          [0.142, 0.125, 0.107],
          [0.152, 0.135, 0.121]]

node12 = [[0.115, 0.096, 0.084],
          [0.125, 0.106, 0.092],
          [0.135, 0.114, 0.100]]

node13 = [[0.051, 0.052, 0.053],
          [0.064, 0.066, 0.067],
          [0.770, 0.079, 0.081]]

node14 = [0.081, 0.081, 0.080]

node15 = [0.059, 0.064, 0.068]

node16 = [0.068, 0.071, 0.073]

node17 = [0.063, 0.062, 0.062]

node18 = [0.035, 0.041, 0.046]

node19 = [0.049, 0.053, 0.058]

node20 = [0.075, 0.091, 0.101]

node21 = [0.077, 0.079, 0.085]

node22 = [0.052, 0.066, 0.073]

node23 = [0.080, 0.076, 0.074]

node24 = [0.086, 0.069, 0.058]

node25 = [0.097, 0.077, 0.063]

node26 = [0.062, 0.054, 0.047]

node27 = [0.041, 0.038, 0.035]

node28 = [0.022, 0.016, 0.012]

node29 = [0.022, 0.016, 0.012]

node30 = [[1.045, 1.045, 1.004],
          [1.028, 1.032, 0.994],
          [1.012, 1.019, 0.984]]

node31 = [[0.116, 0.088, 0.071]]

node32 = [0.88]

node33 = [1.05]

node34 = [1.04, 0.98]

node35 = [0.9, 0.86]

node36 = [[0.092, 0.088, 0.081],
          [0.101, 0.094, 0.089],
          [0.108, 0.104, 0.097]]

node1_1 = [0.015]

node1_2 = [0.018]

node1_3 = [0.005]

node1_4 = [0.0015]


def node_1():
    print("Вузол примикання зовнішніх стін із цегли з опорядженням штукатуркою до міжповерхового перекриття")
    if a["linar_coefficient"]["node1"]["subnode1.1"] == 1:
        x = node1[0][0]
    elif a["linar_coefficient"]["node1"]["subnode1.1"] == 2:
        x = node1[0][1]
    elif a["linar_coefficient"]["node1"]["subnode1.1"] == 3:
        x = node1[0][2]
    elif a["linar_coefficient"]["node1"]["subnode1.2"] == 1:
        x = node1[1][0]
    elif a["linar_coefficient"]["node1"]["subnode1.2"] == 2:
        x = node1[1][1]
    elif a["linar_coefficient"]["node1"]["subnode1.2"] == 3:
        x = node1[1][2]
    elif a["linar_coefficient"]["node1"]["subnode1.3"] == 1:
        x = node1[2][0]
    elif a["linar_coefficient"]["node1"]["subnode1.3"] == 2:
        x = node1[2][1]
    elif a["linar_coefficient"]["node1"]["subnode1.3"] == 3:
        x = node1[2][2]
    else:
        x = None
    return x


def node_2():
    print("Вузол примикання зовнішніх стін із залізобетону з опорядженням штукатуркою до міжповерхневого перекриття")
    if a["linar_coefficient"]["node2"]["subnode1.1"] == 1:
        x = node2[0][0]
    elif a["linar_coefficient"]["node2"]["subnode1.1"] == 2:
        x = node2[0][1]
    elif a["linar_coefficient"]["node2"]["subnode1.1"] == 3:
        x = node2[0][2]
    elif a["linar_coefficient"]["node2"]["subnode1.2"] == 1:
        x = node2[1][0]
    elif a["linar_coefficient"]["node2"]["subnode1.2"] == 2:
        x = node2[1][1]
    elif a["linar_coefficient"]["node2"]["subnode1.2"] == 3:
        x = node2[1][2]
    elif a["linar_coefficient"]["node2"]["subnode1.3"] == 1:
        x = node2[2][0]
    elif a["linar_coefficient"]["node2"]["subnode1.3"] == 2:
        x = node2[2][1]
    elif a["linar_coefficient"]["node2"]["subnode1.3"] == 3:
        x = node2[2][2]
    else:
        x = None
    return x


def node_3():
    print("""Вузол примикання зовнішніх стін із вентильованим повітрянним прошарком з опорядженням штукатуркою 
до міжповерхневого перекриття""")
    if a["linar_coefficient"]["node3"]["subnode1.1"] == 1:
        x = node3[0][0]
    elif a["linar_coefficient"]["node3"]["subnode1.1"] == 2:
        x = node3[0][1]
    elif a["linar_coefficient"]["node3"]["subnode1.1"] == 3:
        x = node3[0][2]
    elif a["linar_coefficient"]["node3"]["subnode1.2"] == 1:
        x = node3[1][0]
    elif a["linar_coefficient"]["node3"]["subnode1.2"] == 2:
        x = node3[1][1]
    elif a["linar_coefficient"]["node3"]["subnode1.2"] == 3:
        x = node3[1][2]
    elif a["linar_coefficient"]["node3"]["subnode1.3"] == 1:
        x = node3[2][0]
    elif a["linar_coefficient"]["node3"]["subnode1.3"] == 2:
        x = node3[2][1]
    elif a["linar_coefficient"]["node3"]["subnode1.3"] == 3:
        x = node3[2][2]
    else:
        x = None
    return x


def node_4():
    print("Вузол примикання зовнішніх стін із ніздрюватого бетону до міжповерхового перекриття")
    if a["linar_coefficient"]["node4"]["subnode1.1"] == 1:
        x = node4[0][0]
    elif a["linar_coefficient"]["node4"]["subnode1.1"] == 2:
        x = node4[0][1]
    elif a["linar_coefficient"]["node4"]["subnode1.1"] == 3:
        x = node4[0][2]
    elif a["linar_coefficient"]["node4"]["subnode1.2"] == 1:
        x = node4[1][0]
    elif a["linar_coefficient"]["node4"]["subnode1.2"] == 2:
        x = node4[1][1]
    elif a["linar_coefficient"]["node4"]["subnode1.2"] == 3:
        x = node4[1][2]
    elif a["linar_coefficient"]["node4"]["subnode1.3"] == 1:
        x = node4[2][0]
    elif a["linar_coefficient"]["node4"]["subnode1.3"] == 2:
        x = node4[2][1]
    elif a["linar_coefficient"]["node4"]["subnode1.3"] == 3:
        x = node4[2][2]
    else:
        x = None
    return x


def node_5():
    print("Вузол примикання зовнішніх стін із цегли з опорядженням штукатуркою до балконного перекриття")
    if a["linar_coefficient"]["node5"]["subnode1.1"] == 1:
        x = node5[0][0]
    elif a["linar_coefficient"]["node5"]["subnode1.1"] == 2:
        x = node5[0][1]
    elif a["linar_coefficient"]["node5"]["subnode1.1"] == 3:
        x = node5[0][2]
    elif a["linar_coefficient"]["node5"]["subnode1.2"] == 1:
        x = node5[1][0]
    elif a["linar_coefficient"]["node5"]["subnode1.2"] == 2:
        x = node5[1][1]
    elif a["linar_coefficient"]["node5"]["subnode1.2"] == 3:
        x = node5[1][2]
    elif a["linar_coefficient"]["node5"]["subnode1.3"] == 1:
        x = node5[2][0]
    elif a["linar_coefficient"]["node5"]["subnode1.3"] == 2:
        x = node5[2][1]
    elif a["linar_coefficient"]["node5"]["subnode1.3"] == 3:
        x = node5[2][2]
    else:
        x = None
    return x


def node_6():
    print("Вузол примикання зовнішніх стін із залізобетону з опорядженням штукатуркою до балконного перекриття")
    if a["linar_coefficient"]["node6"]["subnode1.1"] == 1:
        x = node6[0][0]
    elif a["linar_coefficient"]["node6"]["subnode1.1"] == 2:
        x = node6[0][1]
    elif a["linar_coefficient"]["node6"]["subnode1.1"] == 3:
        x = node6[0][2]
    elif a["linar_coefficient"]["node6"]["subnode1.2"] == 1:
        x = node6[1][0]
    elif a["linar_coefficient"]["node6"]["subnode1.2"] == 2:
        x = node6[1][1]
    elif a["linar_coefficient"]["node6"]["subnode1.2"] == 3:
        x = node6[1][2]
    elif a["linar_coefficient"]["node6"]["subnode1.3"] == 1:
        x = node6[2][0]
    elif a["linar_coefficient"]["node6"]["subnode1.3"] == 2:
        x = node6[2][1]
    elif a["linar_coefficient"]["node6"]["subnode1.3"] == 3:
        x = node6[2][2]
    else:
        x = None
    return x


def node_7():
    print("Вузол примикання зовнішніх стін із ніздрюватого бетону до балконного перекриття")
    if a["linar_coefficient"]["node7"]["subnode1.1"] == 1:
        x = node7[0][0]
    elif a["linar_coefficient"]["node7"]["subnode1.1"] == 2:
        x = node7[0][1]
    elif a["linar_coefficient"]["node7"]["subnode1.1"] == 3:
        x = node7[0][2]
    elif a["linar_coefficient"]["node7"]["subnode1.2"] == 1:
        x = node7[1][0]
    elif a["linar_coefficient"]["node7"]["subnode1.2"] == 2:
        x = node7[1][1]
    elif a["linar_coefficient"]["node7"]["subnode1.2"] == 3:
        x = node7[1][2]
    elif a["linar_coefficient"]["node7"]["subnode1.3"] == 1:
        x = node7[2][0]
    elif a["linar_coefficient"]["node7"]["subnode1.3"] == 2:
        x = node7[2][1]
    elif a["linar_coefficient"]["node7"]["subnode1.3"] == 3:
        x = node7[2][2]
    else:
        x = None
    return x


def node_8():
    print("Вузол кутового сполучення зовнішніх стін із залізобетону та цегли з опорядженням штукатуркою ")
    if a["linar_coefficient"]["node8"]["subnode1.1"] == 1:
        x = node8[0][0]
    elif a["linar_coefficient"]["node8"]["subnode1.1"] == 2:
        x = node8[0][1]
    elif a["linar_coefficient"]["node8"]["subnode1.1"] == 3:
        x = node8[0][2]
    elif a["linar_coefficient"]["node8"]["subnode1.2"] == 1:
        x = node8[1][0]
    elif a["linar_coefficient"]["node8"]["subnode1.2"] == 2:
        x = node8[1][1]
    elif a["linar_coefficient"]["node8"]["subnode1.2"] == 3:
        x = node8[1][2]
    elif a["linar_coefficient"]["node8"]["subnode1.3"] == 1:
        x = node8[2][0]
    elif a["linar_coefficient"]["node8"]["subnode1.3"] == 2:
        x = node8[2][1]
    elif a["linar_coefficient"]["node8"]["subnode1.3"] == 3:
        x = node8[2][2]
    else:
        x = None
    return x


def node_9():
    print("Вузол кутового сполучення зовнішніх стін із залізобетону та цегли з вентильованим повітряним прошарком")
    if a["linar_coefficient"]["node9"]["subnode1.1"] == 1:
        x = node9[0][0]
    elif a["linar_coefficient"]["node9"]["subnode1.1"] == 2:
        x = node9[0][1]
    elif a["linar_coefficient"]["node9"]["subnode1.1"] == 3:
        x = node9[0][2]
    elif a["linar_coefficient"]["node9"]["subnode1.2"] == 1:
        x = node9[1][0]
    elif a["linar_coefficient"]["node9"]["subnode1.2"] == 2:
        x = node9[1][1]
    elif a["linar_coefficient"]["node9"]["subnode1.2"] == 3:
        x = node9[1][2]
    elif a["linar_coefficient"]["node9"]["subnode1.3"] == 1:
        x = node9[2][0]
    elif a["linar_coefficient"]["node9"]["subnode1.3"] == 2:
        x = node9[2][1]
    elif a["linar_coefficient"]["node9"]["subnode1.3"] == 3:
        x = node9[2][2]
    else:
        x = None
    return x


def node_10():
    print("Вузол кутового сполучення зовнішніх стін із залізобетону з утепленням та ніздрюватого бетону")
    if a["linar_coefficient"]["node10"]["subnode1.1"] == 1:
        x = node10[0][0]
    elif a["linar_coefficient"]["node10"]["subnode1.1"] == 2:
        x = node10[0][1]
    elif a["linar_coefficient"]["node10"]["subnode1.1"] == 3:
        x = node10[0][2]
    elif a["linar_coefficient"]["node10"]["subnode1.2"] == 1:
        x = node10[1][0]
    elif a["linar_coefficient"]["node10"]["subnode1.2"] == 2:
        x = node10[1][1]
    elif a["linar_coefficient"]["node10"]["subnode1.2"] == 3:
        x = node10[1][2]
    elif a["linar_coefficient"]["node10"]["subnode1.3"] == 1:
        x = node10[2][0]
    elif a["linar_coefficient"]["node10"]["subnode1.3"] == 2:
        x = node10[2][1]
    elif a["linar_coefficient"]["node10"]["subnode1.3"] == 3:
        x = node10[2][2]
    else:
        x = None
    return x


def node_11():
    print("Вузол кутового сполучення зовнішніх стін із цегли з опорядженням штукатуркою ")
    if a["linar_coefficient"]["node11"]["subnode1.1"] == 1:
        x = node11[0][0]
    elif a["linar_coefficient"]["node11"]["subnode1.1"] == 2:
        x = node11[0][1]
    elif a["linar_coefficient"]["node11"]["subnode1.1"] == 3:
        x = node11[0][2]
    elif a["linar_coefficient"]["node11"]["subnode1.2"] == 1:
        x = node11[1][0]
    elif a["linar_coefficient"]["node11"]["subnode1.2"] == 2:
        x = node11[1][1]
    elif a["linar_coefficient"]["node11"]["subnode1.2"] == 3:
        x = node11[1][2]
    elif a["linar_coefficient"]["node11"]["subnode1.3"] == 1:
        x = node11[2][0]
    elif a["linar_coefficient"]["node11"]["subnode1.3"] == 2:
        x = node11[2][1]
    elif a["linar_coefficient"]["node11"]["subnode1.3"] == 3:
        x = node11[2][2]
    else:
        x = None
    return x


def node_12():
    print("Вузол кутового сполучення зовнішніх стін із цегли з вентильованим повітряним прошарком ")
    if a["linar_coefficient"]["node12"]["subnode1.1"] == 1:
        x = node12[0][0]
    elif a["linar_coefficient"]["node12"]["subnode1.1"] == 2:
        x = node12[0][1]
    elif a["linar_coefficient"]["node12"]["subnode1.1"] == 3:
        x = node12[0][2]
    elif a["linar_coefficient"]["node12"]["subnode1.2"] == 1:
        x = node12[1][0]
    elif a["linar_coefficient"]["node12"]["subnode1.2"] == 2:
        x = node12[1][1]
    elif a["linar_coefficient"]["node12"]["subnode1.2"] == 3:
        x = node12[1][2]
    elif a["linar_coefficient"]["node12"]["subnode1.3"] == 1:
        x = node12[2][0]
    elif a["linar_coefficient"]["node12"]["subnode1.3"] == 2:
        x = node12[2][1]
    elif a["linar_coefficient"]["node12"]["subnode1.3"] == 3:
        x = node12[2][2]
    else:
        x = None
    return x


def node_13():
    print("Вузол кутового сполучення зовнішніх стін із ніздрюватого бетону")
    if a["linar_coefficient"]["node13"]["subnode1.1"] == 1:
        x = node10[0][0]
    elif a["linar_coefficient"]["node13"]["subnode1.1"] == 2:
        x = node10[0][1]
    elif a["linar_coefficient"]["node13"]["subnode1.1"] == 3:
        x = node10[0][2]
    elif a["linar_coefficient"]["node13"]["subnode1.2"] == 1:
        x = node10[1][0]
    elif a["linar_coefficient"]["node13"]["subnode1.2"] == 2:
        x = node10[1][1]
    elif a["linar_coefficient"]["node13"]["subnode1.2"] == 3:
        x = node10[1][2]
    elif a["linar_coefficient"]["node13"]["subnode1.3"] == 1:
        x = node10[2][0]
    elif a["linar_coefficient"]["node13"]["subnode1.3"] == 2:
        x = node10[2][1]
    elif a["linar_coefficient"]["node13"]["subnode1.3"] == 3:
        x = node10[2][2]
    else:
        x = None
    return x


def node_14():
    print("""Вузол примикання віконної конструкції до зовнішніх стін із цегли з опорядженням штукатуркою
в зоні перемички""")
    if a["linar_coefficient"]["node14"] == 1:
        x = node14[0]
    elif a["linar_coefficient"]["node14"] == 2:
        x = node14[1]
    elif a["linar_coefficient"]["node14"] == 3:
        x = node14[2]
    else:
        x = None
    return x


def node_15():
    print("""Вузол примикання віконної конструкції до зовнішніх стін із цегли з опорядженням штукатуркою
в зоні підвіконня""")
    if a["linar_coefficient"]["node15"] == 1:
        x = node15[0]
    elif a["linar_coefficient"]["node15"] == 2:
        x = node15[1]
    elif a["linar_coefficient"]["node15"] == 3:
        x = node15[2]
    else:
        x = None
    return x


def node_16():
    print("""Вузол примикання віконної конструкції до зовнішніх стін із цегли з опорядженням штукатуркою
в зоні рядового сполучення """)
    if a["linar_coefficient"]["node16"] == 1:
        x = node16[0]
    elif a["linar_coefficient"]["node16"] == 2:
        x = node16[1]
    elif a["linar_coefficient"]["node16"] == 3:
        x = node16[2]
    else:
        x = None
    return x


def node_17():
    print("""Вузол примикання віконної конструкції до зовнішніх стін із цегли з вентильованим повітряним прошарком 
в зоні перемички""")
    if a["linar_coefficient"]["node17"] == 1:
        x = node17[0]
    elif a["linar_coefficient"]["node17"] == 2:
        x = node17[1]
    elif a["linar_coefficient"]["node17"] == 3:
        x = node17[2]
    else:
        x = None
    return x


def node_18():
    print("""Вузол примикання віконної конструкції до зовнішніх стін із цегли з вентильованим повітряним прошарком 
в зоні підвіконня""")
    if a["linar_coefficient"]["node18"] == 1:
        x = node18[0]
    elif a["linar_coefficient"]["node18"] == 2:
        x = node18[1]
    elif a["linar_coefficient"]["node18"] == 3:
        x = node18[2]
    else:
        x = None
    return x


def node_19():
    print("""Вузол примикання віконної конструкції до зовнішніх стін із цегли з вентильованим повітряним прошарком 
в зоні рядового сполучення""")
    if a["linar_coefficient"]["node19"] == 1:
        x = node19[0]
    elif a["linar_coefficient"]["node19"] == 2:
        x = node19[1]
    elif a["linar_coefficient"]["node19"] == 3:
        x = node19[2]
    else:
        x = None
    return x


def node_20():
    print("""Вузол примикання віконної конструкції до зовнішніх стін із ніздрюватого бетону в зоні перемички""")
    if a["linar_coefficient"]["node20"] == 1:
        x = node20[0]
    elif a["linar_coefficient"]["node20"] == 2:
        x = node20[1]
    elif a["linar_coefficient"]["node20"] == 3:
        x = node20[2]
    else:
        x = None
    return x


def node_21():
    print("""Вузол примикання віконної конструкції до зовнішніх стін із цегли з ніздрюватого бетону
в зоні підвіконня""")
    if a["linar_coefficient"]["node21"] == 1:
        x = node21[0]
    elif a["linar_coefficient"]["node21"] == 2:
        x = node21[1]
    elif a["linar_coefficient"]["node21"] == 3:
        x = node21[2]
    else:
        x = None
    return x


def node_22():
    print("""Вузол примикання віконної конструкції до зовнішніх стін із цегли з ніздрюватого бетону
в зоні рядового сполучення""")
    if a["linar_coefficient"]["node22"] == 1:
        x = node22[0]
    elif a["linar_coefficient"]["node22"] == 2:
        x = node22[1]
    elif a["linar_coefficient"]["node22"] == 3:
        x = node22[2]
    else:
        x = None
    return x


def node_23():
    print("""Вузол примикання зовнішніх стін із тришарових панелей на основі важкого бетону до 
міжповерхового перекриття""")
    if a["linar_coefficient"]["node23"] == 1:
        x = node23[0]
    elif a["linar_coefficient"]["node23"] == 2:
        x = node23[1]
    elif a["linar_coefficient"]["node23"] == 3:
        x = node23[2]
    else:
        x = None
    return x


def node_24():
    print("Вузол влаштування зовнішніх стін із вентильваним повітряним прошарком на основі дерев'яного каркаса")
    if a["linar_coefficient"]["node24"] == 1:
        x = node24[0]
    elif a["linar_coefficient"]["node24"] == 2:
        x = node24[1]
    elif a["linar_coefficient"]["node24"] == 3:
        x = node24[2]
    else:
        x = None
    return x


def node_25():
    print("Вузол примикання конструкції горищного даху з одношаровою теплоізоляцією до дерев'яної крокви")
    if a["linar_coefficient"]["node25"] == 1:
        x = node25[0]
    elif a["linar_coefficient"]["node25"] == 2:
        x = node25[1]
    elif a["linar_coefficient"]["node25"] == 3:
        x = node25[2]
    else:
        x = None
    return x


def node_26():
    print("""Вузол примикання конструкції горищного даху з двошаровою теплоізоляцією  
до дерев'яної крокви та обрешіткою 50мм""")
    if a["linar_coefficient"]["node26"] == 1:
        x = node26[0]
    elif a["linar_coefficient"]["node26"] == 2:
        x = node26[1]
    elif a["linar_coefficient"]["node26"] == 3:
        x = node26[2]
    else:
        x = None
    return x


def node_27():
    print("""Вузол примикання конструкції горищного даху з двошаровою теплоізоляцією 
до дерев'яної крокви та обрешіткою 100мм""")
    if a["linar_coefficient"]["node27"] == 1:
        x = node27[0]
    elif a["linar_coefficient"]["node27"] == 2:
        x = node27[1]
    elif a["linar_coefficient"]["node27"] == 3:
        x = node27[2]
    else:
        x = None
    return x


def node_28():
    print("""Вузол примикання конструкції горищного даху з двошаровою теплоізоляцією 
до дерев'яної обрешітки товщиною 50мм""")
    if a["linar_coefficient"]["node28"] == 1:
        x = node28[0]
    elif a["linar_coefficient"]["node28"] == 2:
        x = node28[1]
    elif a["linar_coefficient"]["node28"] == 3:
        x = node28[2]
    else:
        x = None
    return x


def node_29():
    print("""Вузол примикання конструкції горищного даху з двошаровою теплоізоляцією 
до дерев'яної обрешітки товщиною 100мм""")
    if a["linar_coefficient"]["node29"] == 1:
        x = node29[0]
    elif a["linar_coefficient"]["node29"] == 2:
        x = node29[1]
    elif a["linar_coefficient"]["node29"] == 3:
        x = node29[2]
    else:
        x = None
    return x


def node_30():
    print("Вузол примикання конструкції перекриття до внутрішніх стін")
    if a["linar_coefficient"]["node30"]["subnode1.1"] == 1:
        x = node30[0][0]
    elif a["linar_coefficient"]["node30"]["subnode1.1"] == 2:
        x = node30[0][1]
    elif a["linar_coefficient"]["node30"]["subnode1.1"] == 3:
        x = node30[0][2]
    elif a["linar_coefficient"]["node30"]["subnode1.2"] == 1:
        x = node30[1][0]
    elif a["linar_coefficient"]["node30"]["subnode1.2"] == 2:
        x = node30[1][1]
    elif a["linar_coefficient"]["node30"]["subnode1.2"] == 3:
        x = node30[1][2]
    elif a["linar_coefficient"]["node30"]["subnode1.3"] == 1:
        x = node30[2][0]
    elif a["linar_coefficient"]["node30"]["subnode1.3"] == 2:
        x = node30[2][1]
    elif a["linar_coefficient"]["node30"]["subnode1.3"] == 3:
        x = node30[2][2]
    else:
        x = None
    return x


def node_31():
    print("Вузол примикання конструкції перекриття до дерев'яної лаги ")
    if a["linar_coefficient"]["node31"] == 1:
        x = node31[0]
    elif a["linar_coefficient"]["node31"] == 2:
        x = node31[1]
    elif a["linar_coefficient"]["node31"] == 3:
        x = node31[2]
    else:
        x = None
    return x


def node_32():
    print("Вузол примикання конструкції підлоги по грунту до стіни цоколя")
    if a["linar_coefficient"]["node32"] == 1:
        x = node32[0]
    else:
        x = None
    return x


def node_33():
    print("Вузол примикання конструкції підлоги по грунту до стіни підвала")
    if a["linar_coefficient"]["node33"] == 1:
        x = node33[0]
    else:
        x = None
    return x


def node_34():
    print("Вузол примикання конструкції по грунту до зовнішніх стін з фасадною теплоізоляцією ")
    if a["linar_coefficient"]["node34"] == 1:
        x = node34[0]
    elif a["linar_coefficient"]["node34"] == 2:
        x = node34[1]
    else:
        x = None
    return x


def node_35():
    print("Вузол примикання конструкції по грунту до зовнішніх стін з блоків з ніздрюватого бетону ")
    if a["linar_coefficient"]["node35"] == 1:
        x = node35[0]
    elif a["linar_coefficient"]["node35"] == 2:
        x = node35[1]
    else:
        x = None
    return x


def node_36():
    print("Вузол кутового сполучення зовнішніх стін з цегли з додатковою теплоізоляцією та опорядженням штукатуркою")
    if a["linar_coefficient"]["node36"]["subnode1.1"] == 1:
        x = node36[0][0]
    elif a["linar_coefficient"]["node36"]["subnode1.1"] == 2:
        x = node36[0][1]
    elif a["linar_coefficient"]["node36"]["subnode1.1"] == 3:
        x = node36[0][2]
    elif a["linar_coefficient"]["node36"]["subnode1.2"] == 1:
        x = node36[1][0]
    elif a["linar_coefficient"]["node36"]["subnode1.2"] == 2:
        x = node36[1][1]
    elif a["linar_coefficient"]["node36"]["subnode1.2"] == 3:
        x = node36[1][2]
    elif a["linar_coefficient"]["node36"]["subnode1.3"] == 1:
        x = node36[2][0]
    elif a["linar_coefficient"]["node36"]["subnode1.3"] == 2:
        x = node36[2][1]
    elif a["linar_coefficient"]["node36"]["subnode1.3"] == 3:
        x = node36[2][2]
    else:
        x = None
    return x


def node_37():
    print("Вузол примикання до металевого несучого елемента каркаса")
    x1 = float(input("Введіть товщину теплоізоляції: "))
    x2 = float(input("Введіть товщину гіпсокартону: "))
    x3 = float(input("Введіть товщину полки швелера: "))
    x4 = float(input("Введіть товщину твелера: "))

    x = 0.1 - 0.4 * x1 - 4 * x2 + 2.2 * x3 + 25 * x4
    return x


def node_1_1():
    print("Вузол улаштування несучого кронштейна фасадної системи з вентильованим повітряним прошарком")
    if a["point_coefficient"]["node1"] == 1:
        x = node1_1[0]
    else:
        x = None
    return x


def node_1_2():
    print("""Вузол улаштування анкера на основі металевого гнучкого Z-подібного елемента фасадної системи 
з опорядженням цеглою""")
    if a["point_coefficient"]["node2"] == 1:
        x = node1_2[0]
    else:
        x = None
    return x


def node_1_3():
    print("""Вузол улаштування пластикового дюбеля з металевим стрижнем для кріплення теплоізоляційного шару 
в фасадній системі з опорядженням штукатурками""")
    if a["point_coefficient"]["node3"] == 1:
        x = node1_3[0]
    else:
        x = None
    return x


def node_1_4():
    print("""Вузол улаштування пластикового дюбеля з пластиковим стрижнем для кріплення теплоізоляційного шару
в фасадній системі з опорядженням штукатурками""")
    if a["point_coefficient"]["node4"] == 1:
        x = node1_4[0]
    else:
        x = None
    return x
