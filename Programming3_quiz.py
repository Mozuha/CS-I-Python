# Alyosha Perez, Mizuki Hashimoto

import Programming3_module  # Import Programming3_module module
import random

states = Programming3_module.states  # Dictionary "states"
again = 'y'
state = list(states.values())  # Convert states.values to list
abb = list(states.keys())  # Convert states.keys to list

while again == 'y':
    rand = random.choice(state)  # Choose randomly from the list "state"
    while True:
        print('What is the abbreviation of this state?: {}'.format(rand))  # Insert randomly chose value into {}
        answer = input('Answer: ')
        if answer == abb[state.index(rand)]:  # If answer is equal to same index as rand of abb
            print('Correct!')
            break  # Exit the loop
        else:
            print('Wrong.')
    abb.remove(answer)  # Remove used key
    state.remove(rand)  # Remove used value
    print(len(state), 'states remaining.') # Number of states (questions) remaining
    if len(state) == 0:  # If all states are used
        again = input('Congratulation! You have answered every question! Would you like to do again? (y/n): ')
        state = list(Programming3_module.states.values())  # Generate the full-filled list
        abb = list(Programming3_module.states.keys())  # Generate the full-filled list