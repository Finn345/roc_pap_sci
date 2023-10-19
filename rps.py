import random

choices = ['rock', 'paper', 'scissors']

while True:
    player_choice = input("Choose: rock, paper, scissors, or 'quit' to exit: ").lower()

    if player_choice == 'quit':
        break
    if player_choice in choices:
        computer_choice = random.choice(choices)

        print('Player Chooses: ', player_choice)
        print('Computer Chooses: ', computer_choice)

        if player_choice == computer_choice:
            print("Tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You Win!")
        else:
            print('You Lose! :(')
    else:
        print('Invalid choice. Please choose rock, paper, scissors, or "quit".')
