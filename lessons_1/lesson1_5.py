proceeds = float(input("Введите издержки: "))
profit = float(input("Введите выручку: "))

if (profit-proceeds)>0:
    print("прибыль — выручка больше издержек!")
    print("Рентабельность: ", int(profit/proceeds*100), "%")
    val = profit / int(input("Введите число сотрудников: "))
    print("Прибыль на сотрудника = ",val)
else:
    print("убыток — издержки больше выручки!")


