result = 0
while True:
    num_1 = float(input('Enter the first number: '))
    num_2 = float(input('Enter the second number: '))
    sym_operation = input('Select the operation symbol "+" "-" "*" "/": ')
    if sym_operation == '+':
        result = num_1 + num_2
    elif sym_operation == "-":
        result = num_1 - num_2
    elif sym_operation == "*":
        result = num_1 * num_2
    elif sym_operation == "/":
        if num_1 == 0 or num_2 == 0:
            print("You can't divide by 0!!! ")
            break
        else:
            result = num_1 / num_2
    print(result)
    pass
    continue_action = input('Do you want to continue (yes/no): ')
    if continue_action == 'yes':
        continue
    else:
        break


