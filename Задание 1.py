money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
cash_month = 0

while money_capital + salary > spend:
    if salary < spend:
        money_capital -= (spend - salary)
    if money_capital <= 0:
        break
    cash_month += 1
    spend = spend + (spend * increase)

print("Количество месяцев, которое можно протянуть без долгов:", cash_month)
