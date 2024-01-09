def second_index(text, some_str):
    find_first_index = str(text).find(some_str)
    if find_first_index != -1:
        find_second_index = str(text).find(some_str, find_first_index + 1)
        if find_second_index != -1:
            return find_second_index

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')