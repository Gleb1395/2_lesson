import random

general_list = []
for i in range(random.randint(3, 10)):
    general_list.append(random.randint(1, 10))
print(general_list)
new_list = [general_list[0], general_list[2], general_list[-2]]
print(new_list)
