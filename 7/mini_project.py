import random

choices = ['s', 'w', 'g']

computer = random.choice(choices)
player = input("Choose Snake (s), Water (w), or Gun (g): ").lower()

if player not in choices:
    print("Invalid input")
else:
    print(f"You chose {player}, Computer chose {computer}")

    if player == computer:
        print("Draw")
    elif (player == 's' and computer == 'w') or \
         (player == 'w' and computer == 'g') or \
         (player == 'g' and computer == 's'):
        print("You win")
    else:
        print("Computer wins")
