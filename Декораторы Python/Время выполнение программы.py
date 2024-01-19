import random
import time

"""
Декоратор классифицирует положительные числа на четные и нечетные и выводит результаты.

"""


def classify_numbers(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        even_element = [x for x in func(*args, **kwargs) if x % 2 == 0]
        odd_element = [y for y in func(*args, **kwargs) if y % 2 != 0]
        finish_time = time.time()
        print(f'Четные элементы этого списка -> {even_element}')
        print(f'Нечетные элементы этого списка -> {odd_element}')
        print(f'Общее время выполнения программы: {finish_time - start_time: .8f}')

        return even_element

    return wrapper


@classify_numbers
def finnd_posive_number(lst: list):
    result = [x for x in lst if x > 0]
    return result


finnd_posive_number([-5, 8, -4, -3, 9, -3, 5, -19, 20, -7, 5, 12, -20, 7, 19, 20, -19, 19, -3, -9])
# finnd_posive_number([random.randint(-100000, 100000) for _ in range(10000)])
