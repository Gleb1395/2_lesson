user_input_time = 224930
day = user_input_time // 86400
hour = (user_input_time % 86400) // 3600
minutes = (user_input_time % 86400 % 3600) // 60
second = user_input_time % 86400 % 3600 % 60
if day == 0:
    print(f'{day} днів, {str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(second).zfill(2)}')
elif day == 1 or day % 10 == 1:
    print(f'{day} день, {str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(second).zfill(2)}')
elif day > 9 and day < 20:
    print(f'{day} днів, {str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(second).zfill(2)}')
elif day < 5 or day % 10 < 5:
    print(f'{day} дні, {str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(second).zfill(2)}')
else:
    print(f'{day} днів, {str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(second).zfill(2)}')
