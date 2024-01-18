def first_word(text: str):
    start_index = 0
    while start_index < len(text) and not text[start_index].isalpha() and text[start_index] not in "'":
        start_index += 1
    end_index = start_index
    while end_index < len(text) and (text[end_index].isalpha() or text[end_index] in "'"):
        end_index += 1
    return text[start_index:end_index]
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')