user_input_time = int(input("Введить кількість секунд: "))
day = user_input_time // 86400
hour = (user_input_time % 86400) // 3600
minutes = (user_input_time % 86400 % 3600) // 60
second = user_input_time % 86400 % 3600 % 60
if day == 0:
    days_str = 'днів'
elif day == 1 or day % 10 == 1 and day != 11:
    days_str = 'день'
elif day > 9 and day < 20:
    days_str = 'днів'
elif day < 5 or day % 10 < 5:
    days_str = 'дні'
else:
    days_str = 'днів'
print(f'{day} {days_str}, {str(hour).zfill(2)}:{str(minutes).zfill(2)}:{str(second).zfill(2)}')
