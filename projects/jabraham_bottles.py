#!/usr/bin/env python3


def generate_verse(bottle_number):
    ''' Return a string of verse from the song "99 Bottles" corresponding to bottle_number'''
    master_verse = '''
{0} bottle{1} of beer on the wall!
{0} bottle{1} of beer!
Take one down
And pass it around
{2} bottle{3} of beer on the wall!\n'''
    
    if bottle_number == 2:
        return master_verse.format(2, 's', 1, '')
    if bottle_number == 1:
        last_verse =  master_verse.split("\n")
        last_verse[-2] = "No more bottles of beer on the wall!\n"
        last_verse = "\n".join(last_verse)
        return last_verse.format(1, '')

    return master_verse.format(bottle_number, 's', bottle_number - 1, 's')


def main():
    # TODO: add command-line arg
    for num in range(99, 0, -1):
        print(generate_verse(num))


if __name__ == "__main__":
    main()
