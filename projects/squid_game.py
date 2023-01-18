import random
from tqdm import tqdm
from tabulate import tabulate

num_of_simulations = 1_000_000
survival_dict = {player: 0
                 for player in range(1, 17)}

for i in tqdm(range(num_of_simulations)):
    remaining_tiles = 18
    remaining_players = 16
    while remaining_tiles > 0 and remaining_players > 0:
        rand_num = random.choice([0, 1])
        if rand_num == 0:
            remaining_players -= 1
        remaining_tiles -= 1

    for player in survival_dict:
        if player > 16 - remaining_players:
            survival_dict[player] += 100/num_of_simulations

results = []
for player in survival_dict:
    results.append([player, survival_dict[player]])

print(tabulate(results, headers=["Player", "Chance %"], tablefmt="github"))
