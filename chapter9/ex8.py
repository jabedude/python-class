#!/usr/bin/env python3
''' Code for exercise 8 chapter 9 '''
import sys


def main():
    ''' Docstring '''
    freq_dict = dict()

    for name in sys.argv[1:]:
        with open(name, "r") as file_in:
            while True:
                line = file_in.readline().strip()
                if not line:
                    break

                if line in freq_dict:
                    freq_dict[line] += 1
                else:
                    freq_dict[line] = 1

    for name, freq in sorted(freq_dict.items()):
        print("{}\t{}".format(name, freq))

if __name__ == "__main__":
    main()
