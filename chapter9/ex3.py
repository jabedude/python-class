#!/usr/bin/env python3
''' Code for exercise 3 chapter 9 '''


def main():
    '''
    Function asks user for two file names and copies the first to the second
    '''
    in_name = input("Enter the name of the input file: ")
    out_name = input("Enter the name of the output file: ")

    with open(in_name, "r") as in_file, open(out_name, "w") as out_file:
        while True:
            line = in_file.readline()
            if not line:
                break
            out_file.write(line)


if __name__ == "__main__":
    main()
