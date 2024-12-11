import random
from typing import Tuple


def monty_hall_game(switch_door: bool) -> bool:
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
    door_revealed = random.choice(doors_revealed)

    if switch_door:
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'


def simulate_game(num_games: int) -> Tuple[float, float]:
    num_wins_without_switching = sum([monty_hall_game(False) for _ in range(num_games)])
    num_wins_with_switching = sum([monty_hall_game(True) for _ in range(num_games)])

    return num_wins_without_switching, num_wins_with_switching

if __name__ == "__main__":
    num_games = 1000
    num_wins_without_switching, num_wins_with_switching = simulate_game(num_games)
    print(f"Winning percentage without switching doors: {num_wins_without_switching/num_games*100}%")
    print(f"Winning percentage with switching doors: {num_wins_with_switching/num_games*100}%")
