def common_elements():
    first_lst_item = []
    second_lst_item = []
    for num in range(1, 50):
        if num % 3 == 0:
            first_lst_item.append(num)
        if num % 5 == 0:
            second_lst_item.append(num)
    intersection_item = set(first_lst_item) & set(second_lst_item)
    return intersection_item


result = common_elements()
print(result)