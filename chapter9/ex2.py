#!/usr/bin/env python3
''' Code for exercise 2 chapter 9 '''
import sys


def main():
    ''' Docstring '''
    if len(sys.argv) == 3 and sys.argv[1] == "-t":
        file_name = sys.argv[2]
    else:
        file_name = input("Please enter a file name: ")

    line_count = 0
    word_count = 0
    char_count = 0

    with open(file_name, "r") as count_file:
        while True:
            line = count_file.readline()
            if not line:
                break
            line_count += 1
            word_count += len(line.split())
            char_count += len(line)

    msg = "{} {} {} {}".format(line_count, word_count, char_count, file_name)
    print(msg)

if __name__ == "__main__":
    main()
