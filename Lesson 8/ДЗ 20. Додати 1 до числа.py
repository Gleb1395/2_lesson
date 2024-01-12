def add_one(some_list):
    starting_lst = some_list
    new_lst = []
    num_str = ''.join(map(str, starting_lst))
    convert_the_number = str(int(num_str) + 1)
    for item in convert_the_number:
        new_lst.append(int(item))
    return new_lst
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")