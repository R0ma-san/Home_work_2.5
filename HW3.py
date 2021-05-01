spendings = [140, 30, 999, 145, 538, 878, 901, 613, 471, 286, 147, 90]
income = [300, 40, 0, 4000, 8911, 73, 85, 0, 9000, 941, 658, 190]

def func(spendings, income):
    koef_sum = 0
    j = 0
    for i in spendings:
        koef = 0
        try:
            koef = i/income[j]
        except ZeroDivisionError:
            koef = 0
        koef_sum+=koef
        j+=1
    return koef_sum/12
print(func(spendings, income))

