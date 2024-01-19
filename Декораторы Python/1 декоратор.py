import time
"""
Это базовый пример, он есть во всех книгах, я его сделал для примера и удобства
"""

def time_dicorate(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        print(f'Время выполнения {finish_time - start_time}')
        return result
    return wrapper
@time_dicorate
def first_word(text: str):
    start_index = 0
    while start_index < len(text) and not text[start_index].isalpha() and text[start_index] not in "'":
        start_index += 1
    end_index = start_index
    while end_index < len(text) and (text[end_index].isalpha() or text[end_index] in "'"):
        end_index += 1
    return text[start_index:end_index]
print(first_word("Hello world"))