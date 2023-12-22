general_list = [12]
lenght_list = len(general_list)
if lenght_list == 0:
    print(general_list)
else:
    tm_var = int(general_list[-1])
    general_list.insert(0, tm_var)
    general_list.pop()
    print(general_list)
