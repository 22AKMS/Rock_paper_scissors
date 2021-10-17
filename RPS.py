# Everett & Alshaikh & Abdullah
import random
game = [
    ["draw", "win", "lose"],
    ["lose", "draw", "win"],
    ["win", "lose", "draw"]]
user_input = int(input(
    "Pick one choice by it's number: \n Rock=1 \n Paper=2 \n Scissors=3 \n\n "))-1
comp_choice = random.randint(0, 2)
if comp_choice == 0:
    response = "rock"
elif comp_choice == 1:
    response = "paper"
elif comp_choice == 2:
    response = "scissors"
print(f"You {game[comp_choice][user_input]}. the computer picked {response}")
