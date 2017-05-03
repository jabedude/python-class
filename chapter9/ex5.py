#!/usr/bin/env python3
''' Code for exercise 5 chapter 9 '''
import sys


def main():
    '''
    Function asks user for two file names and copies the first to the second
    File names can be passed via command line
    '''
    if len(sys.argv) == 3:
        in_name = sys.argv[1]
        out_name = sys.argv[2]
    else:
        in_name = input("Enter the name of the input file: ")
        out_name = input("Enter the name of the output file: ")

    try:
        with open(in_name, "r") as in_file, open(out_name, "w") as out_file:
            while True:
                line = in_file.readline()
                if not line:
                    break
                out_file.write(line)
    except OSError as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    main()
