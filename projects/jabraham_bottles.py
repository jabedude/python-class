#!/usr/bin/env python3
'''
This program prints the lyrics to the song "99 Bottles"
'''
import sys


def generate_verse(bottle_number):
    '''
    Return a string of verse from the song "99 Bottles"
    corresponding to bottle_number
    '''

    master_verse = '''
{0} bottle{1} of beer on the wall!
{0} bottle{1} of beer!
Take one down
And pass it around
{2} bottle{3} of beer on the wall!\n'''

    if bottle_number == 2:
        return master_verse.format(2, 's', 1, '')
    if bottle_number == 1:
        last_verse = master_verse.split("\n")
        last_verse[-2] = "No more bottles of beer on the wall!\n"
        last_verse = "\n".join(last_verse)
        return last_verse.format(1, '')

    return master_verse.format(bottle_number, 's', bottle_number - 1, 's')


def main():
    '''
    Recieves one command line argument and prints the appropriate
    lyrics to the song "99 Bottles. Default value is 99"
    '''

    if len(sys.argv) == 2:
        user_number = sys.argv[1]
        if user_number.isdigit() and user_number != "0":
            user_number = int(user_number)
        else:
            print("Usage: {} <number of bottles> "
                  "Number must be greater than 0.".format(sys.argv[0]))
            exit(1)
    else:
        user_number = 99

    for num in range(user_number, 0, -1):
        print(generate_verse(num))


if __name__ == "__main__":
    main()
