def swap_in_place(var_1, var_2):
    print var_1, var_2
    var_2 = var_1 ^ var_2
    var_1 = var_2 ^ var_1
    var_2 = var_1 ^ var_2
    print var_1, var_2

swap_in_place(1, 2)
