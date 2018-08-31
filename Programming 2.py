# Alyosha Perez, Mizuki Hashimoto
import random

# Define the function guess(rand, count)
def guess (rand, count):
    user_input = int(input('Enter a number between 1 to 100: '))
    count += 1  # Increase the number of attempt.
    if user_input == rand:
        print('You win! Guessed {} times'.format(count) if count <= 7 else "You lose. Guessed {} times.".format(count))
        # Tell the player "You win!" if the number player guessed and system picked are matched within 7 attempts.
        # Tell the player "You lose." if the number player guessed and system picked are matched but over 7 attempts.
    elif user_input > rand:
        print('Incorrect. Lower.')  # Give the player hint "Lower" if user_input is higher than rand.
        guess(rand, count)  # Execute guess(rand, count) again.
    elif user_input < rand:
        print('Incorrect. Higher.')  # Give the player hing "Higher" if user_input is lower than rand.
        guess(rand, count)

print("Let's play a guessing game. The system will pick a random number between 1 and 100. Guess a number the system has picked.")

# Reset the number of attempt and pick the new random number, then execute guess(rand, count)
again = 'y'
while again == 'y':
    count = 0
    rand = random.randint(1, 100)
    guess(rand, count)
    again = input("Try again? (y/n): ")  # Ask the player if he want to play again or not.