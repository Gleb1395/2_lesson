general_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
lst_without_zero = []
lst_with_zero = []
for item in general_list:
    if item != 0:
        lst_without_zero.append(item)
    else:
        lst_with_zero.append(item)
print(lst_without_zero + lst_with_zero)
