money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0
total_money = money_capital + salary - spend
spend_max = spend + spend * increase

while total_money >= spend_max:
    total_money = total_money + salary - spend_max * (1 + increase)
    month += 1# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", month)
