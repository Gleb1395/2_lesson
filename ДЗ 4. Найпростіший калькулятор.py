num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the second number: '))
sym_operation = input('Select the operation symbol "+" "-" "*" "/": ')
if sym_operation == "+":
    result = num_1 + num_2
    print('Result: ', result)
elif sym_operation == "-":
    result = num_1 - num_2
    print('Result: ', result)
elif sym_operation == "*":
    result = num_1 * num_2
    print('Result: ', result)
elif sym_operation == "/":
    if num_1 == 0 or num_2 == 0:
        print("You can't divide by 0!!! ")
    else:
        result = num_1 / num_2
        print('Result: ', result)
else:
    print('You have entered the wrong character')


