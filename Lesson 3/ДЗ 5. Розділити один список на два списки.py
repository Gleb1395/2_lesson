general_list = []
length_list = int(len(general_list))
if length_list % 2 == 0:
    tm_var = length_list // 2
    first_lst = general_list[0:tm_var]
    second_list = general_list[tm_var::]
    print([first_lst, second_list])
else:
    tm_var = length_list // 2 + 1
    first_lst = general_list[0:tm_var]
    second_list = general_list[tm_var::]
    print([first_lst, second_list])
