general_list = [0, 1, 7, 2, 4, 8]
if len(general_list) == 0:
    print('Result: ', 0)
else:
    even_numbers = general_list[::2]
    last_item = general_list[-1]
    sum_item = 0
    for x in even_numbers:
        sum_item = sum_item + x
    print('Result: ', sum_item * last_item)
