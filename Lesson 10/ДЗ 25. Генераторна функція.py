from inspect import isgenerator


def custom_pow(x: int) -> int:
    return x ** 2


def some_gen(begin: int, end: int, func):
    count = 0
    while end > count:
        yield begin
        begin = func(begin)
        count += 1

gen = some_gen(2, 4, custom_pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
