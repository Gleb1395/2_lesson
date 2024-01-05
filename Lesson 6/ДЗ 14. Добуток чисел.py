user_input = int(input("Введите целое число: "))
num = str(user_input)
lst = []
sum_el = 1
while True:
    for x in str(num):
        lst.append(x)
    for y in lst:
        sum_el = int(y) * sum_el
    num = sum_el
    if len(str(num)) > 1:
        lst.clear()
        sum_el = 1
        continue
    else:
        break
print(num)