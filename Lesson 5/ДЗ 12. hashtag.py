import string

something = 'Should, I. subscribe? Yes!'
empty_lst = []
hastag_lst = []
for x in something.title():
    empty_lst.append(x)
for y in empty_lst:
    if y not in string.punctuation and y != ' ':
        hastag_lst.append(y)
hastag_lst.insert(0, '#')
print(''.join(hastag_lst[:140]))
