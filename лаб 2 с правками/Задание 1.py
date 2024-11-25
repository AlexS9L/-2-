money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    d = spend - salary
    if d > money_capital:
        break

    money_capital -= d
    spend *= 1 + increase
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
