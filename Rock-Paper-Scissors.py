import random

# Initialize the win counters
user_wins = 0
computer_wins = 0

# Define the possible options
options = ["rock", "paper", "scissors"]

# Start the game loop
while True:
    # Get user input and convert it to lowercase
    user_input = input("Type Rock/paper/Scissors or Q to quit: ").lower()

    # Check if the user wants to quit
    if user_input == "q":
        break

    # Check if the user input is valid
    if user_input not in options:
        continue

    # Generate a random number to represent the computer's choice
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # Determine the winner of the round
    if (user_input == "rock" and computer_pick == "scissors") or \
       (user_input == "paper" and computer_pick == "rock") or \
       (user_input == "scissors" and computer_pick == "paper"):
        print("You won!")
        user_wins += 1
    else:
        print("You lost.")
        computer_wins += 1

# Print the final scores and a thank you message
print("You won", user_wins, "times against the computer.")
print("The computer won", computer_wins, "times against you.")
print("Thanks for playing!")
