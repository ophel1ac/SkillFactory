def prices():
    amount = int(input("Введите количество посетителей:\n"))
    cost = []
    for i in range(1, amount + 1):
        age = int(input(f"Введите возраст {i} посетителя:\n"))
        if 18 <= age <= 24:
            cost.append(990)
        elif 25 <= age:
            cost.append(1390)
        else:
            cost.append(0)
    if len(cost) >= 4:
        return int(sum(cost) * 0.9)
    return sum(cost)

print(f"К оплате {prices()} руб.")