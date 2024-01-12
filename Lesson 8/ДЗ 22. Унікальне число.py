def find_unique_value(some_list):
    lst_2 = []
    for item in some_list:
        if some_list.count(item) == 1:
            lst_2.append(item)
    result = lst_2[0]
    return result
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")