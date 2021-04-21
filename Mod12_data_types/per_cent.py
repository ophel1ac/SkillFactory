per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} 

money = int(input("money = "))
deposit = [int(i * money) for i in per_cent.values()]

print(f"deposit = {deposit}")
print(f"Максимальная сумма, которую вы можете заработать — {max(deposit)}")