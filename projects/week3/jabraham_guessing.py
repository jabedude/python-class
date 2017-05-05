#!/usr/bin/env python3
'''
This program is an implementation of the "High-Low Guessing Game".
The user is prompted to guess a number from 1 to 100 and the
program will tell the user if the number is greater or lesser than
the correct number.
'''
from random import randint


# CONSTANTS #
ANSWER = randint(1, 100)
BANNER = '''Hello. I'm thinking of a number from 1 to 100...
Try to guess my number!'''
PROMPT = "Guess> "
# MESSAGES #
err_msg = "{} is an invalid choice. Please enter a number from 1 to 100."
suc_msg = "{} was correct! You guessed the number in {} guess{}."
wrong_msg = "{} is too {}!"


def main():
    '''
    This function is the entry point of the program and handles user
    interaction with the game.
    '''

    print(BANNER)
    print(ANSWER)
    guesses_num = 0

    while True:
        user_input = input(PROMPT)
        guesses_num += 1

        try:
            user_input = int(user_input)

            if user_input not in range(1, 101):
                raise ValueError

            elif user_input == ANSWER:
                if guesses_num == 1:
                    print(suc_msg.format(user_input, guesses_num, ""))
                else:
                    print(suc_msg.format(user_input, guesses_num, "es"))
                break

            elif user_input > ANSWER:
                print(wrong_msg.format(user_input, "high"))

            else:
                print(wrong_msg.format(user_input, "low"))

        except ValueError:
            print(err_msg.format(user_input))


if __name__ == "__main__":
    main()
