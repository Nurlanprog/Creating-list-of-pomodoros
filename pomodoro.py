"""
hour_1:minute_1 - hour_2:minute_2
Example: 6:00 - 6:25
"""
print("What hour will pomodoro start?")
hour_1 = int(input())

print("What minute will pomodoro start?")
minute_1 = int(input())

hour_2 = hour_1
minute_2 = minute_1
long_rest = 0  # variable for taking long rest time(15 minute)

print("What time will pomodoro end?")
end = int(input())

my_file = open("Pomodoro.txt", "a+")

while hour_1 != end:

    long_rest += 1
    minute_2 = minute_1 + 25  # incrementing focus session time(25 minute)

    if minute_1 >= 60:  # refreshing hour_1 and minute_1 if minute_1 higher than 60
        hour_1 += 1
        minute_1 -= 60
    if minute_2 >= 60:  # refreshing hour_2 and minute_2 if minute_2 higher than 60
        hour_2 += 1
        minute_2 -= 60

    my_file.write(
        str(hour_1)
        + str(":{}").format(
            "0" if minute_1 < 10 else ""
        )  # format used in order not to leave minute like that: 6:5. Correct form: 6:05
        + str(minute_1)
        + " - "
        + str(hour_2)
        + str(":{}").format(
            "0" if minute_2 < 10 else ""
        )  # format used in order not to leave minute like that: 6:5. Correct form: 6:05
        + str(minute_2)
        + "\n"
    )

    hour_1 = hour_2

    if long_rest % 4 == 0:  # for taking long rest
        minute_1 = minute_2 + 15
    else:  # for taking short rest
        minute_1 = minute_2 + 5

my_file.close()
