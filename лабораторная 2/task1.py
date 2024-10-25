money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
budget = money_capital + salary
count = 0
while budget >= spend:
    budget = budget + salary - spend
    spend = spend * (1 + increase)
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
