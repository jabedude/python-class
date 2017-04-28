#!/usr/bin/env python3


def generate_verse(bottle_number):
    master_verse = '''
{0} bottle{2} of beer on the wall!
{0} bottle{2} of beer!
Take one down
And pass it around
{1} bottle{3} of beer on the wall!\n'''
    
    if bottle_number == 2:
        return master_verse.format(2, 1, 's', '')
    if bottle_number == 1:
        return "LAST" # TODO: format master_verse & remove last line

    return master_verse.format(bottle_number, bottle_number - 1, 's', 's')


def main():

    for num in range(99, 0, -1):
        print(generate_verse(num))


if __name__ == "__main__":
    main()
