import string
import keyword

item = input('Enter the variable: ')
lower_case_characters = string.ascii_lowercase
upper_case_characters = string.ascii_uppercase
all_punctuation = string.punctuation
all_digits = string.digits
count = 0
element_true = '_'
found = 0
while True:
    if item.isdigit() or item[0].isdigit() or item.isspace():
        print(False)
    elif ' ' in item:
        print(False)
    elif keyword.iskeyword(item):
        print(False)
    else:
        for x in item:
            for y in upper_case_characters:
                if x == y:
                    count += 1
                    break
            for j in all_punctuation:
                if x == j and j != element_true:
                    found += 1
                    break
        if count > 0 or found > 0:
            print(False)
        else:
            print(True)
    break
