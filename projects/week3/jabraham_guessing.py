#!/usr/bin/env python3
''' Docstring '''
from random import randint


ANSWER = randint(1, 100)
BANNER = '''Hello. I'm thinking of a number from 1 to 100...
Try to guess my number!'''
PROMPT   = "Guess> "
err_msg  = "{} is an invalid choice. Please enter a number from 1 to 100."
suc_msg  = "{} was correct! You guessed the number in {} guess{}"
high_msg = "{} is too high!"
low_msg  = "{} is too low!"


def main():

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
                print(high_msg.format(user_input))

            else:
                print(low_msg.format(user_input))

        except ValueError:
            print(err_msg.format(user_input))


if __name__ == "__main__":
    main()
