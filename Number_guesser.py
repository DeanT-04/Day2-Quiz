import random

# Get user input for the top of the range
top_of_range = input("Type a number: ")

# Check if the input is a digit
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    # Check if the number is less than or equal to 0
    if top_of_range <= 0:
        print("Please pick a number larger than 0.")
        quit()
else:
    print("Please type a number next time.")
    quit()

# Generate a random number within the given range
random_number = random.randint(0, top_of_range)

# Initialize the guess count
guesses = 0

# Start the guessing loop
while True:
    # Increment the guess count
    guesses += 1

    # Get user guess
    user_guess = input("Make a guess: ")

    # Check if the guess is a digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    # Check if the guess is correct
    if user_guess == random_number:
        print("CORRECT!!")
        break
    # Check if the guess is too high
    elif user_guess > random_number:
        print("Lower")
    # If the guess is too low
    else:
        print("Higher")

# Print the number of guesses it took to get the correct answer
print("You got it in", guesses, "guesses.")
