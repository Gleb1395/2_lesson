def correct_sentence(text: str):
    if '.' in text:
        text_lst = text.split('. ')
        each_words = [word.capitalize() for word in text_lst]
        sentence = '. '.join(each_words)
        if sentence [-1] == '.':
            return f'{sentence}'
        else:
            return f'{sentence}.'
    else:
        sentence = text.capitalize()
        return f'{sentence}.'
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')