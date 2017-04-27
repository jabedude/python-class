#!/usr/bin/env python3

import sys


def main():
    args = sys.argv[1:]

    total = 0
    for num in args:
        total += int(num)

    avg = total / len(args)

    print("The sum of the arguments is {}".format(total))
    print("The average of the arguments is {:.4f}".format(avg))


if __name__ == "__main__":
    main()
