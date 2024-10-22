
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

if program == "j":
    if extra_rinse == "n" and extra_spin =="n":
        total_washing_time = 40
    elif extra_rinse == "y" and extra_spin =="n":
        total_washing_time = 40 + 15
    elif extra_rinse == "n" and extra_spin =="y":
        total_washing_time = 40 + 9
    else:
        total_washing_time = 40 + 15 + 9
elif program == "u":
    if extra_rinse == "n" and extra_spin =="n":
        total_washing_time = 70
    elif extra_rinse == "y" and extra_spin =="n":
        total_washing_time = 70 + 15
    elif extra_rinse == "n" and extra_spin =="y":
        total_washing_time = 70 + 9
    else:
        total_washing_time = 70 + 15 + 9
elif program == "s":
    if extra_rinse == "n" and extra_spin =="n":
        total_washing_time = 20
    elif extra_rinse == "y" and extra_spin =="n":
        total_washing_time = 20 + 15
    elif extra_rinse == "n" and extra_spin =="y":
        total_washing_time = 20 + 9
    else:
        total_washing_time = 20 + 15 + 9

print(f"total washingtime is {total_washing_time} ")


