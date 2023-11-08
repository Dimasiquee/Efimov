list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

total_amount = len(list_players)
half = total_amount // 2
first_team = list_players[:half]
second_team = list_players[half:]
print(first_team)
print(second_team)
