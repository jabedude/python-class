#!/usr/bin/env python3
''' Code for exercise 4 chapter 10 '''

def build_dict(text_list):
    ''' Docstring '''
    master_dict = dict()
    comp_dict = {"Desktop" : 0, "Laptop" : 0, "Tablet" : 0}
    name_list = [x.split()[0] for x in text_list]
    for name in name_list:
        if name not in master_dict:
            master_dict[name] = comp_dict
    return master_dict


def parse_line(line):
    ''' Doctring '''
    line = line.strip()
    line_list = line.split()


def main():
    ''' Docstring '''
    with open("computers.txt", "r") as comp_file:
        comp_lines = comp_file.readlines()

    print(build_dict(comp_lines))


if __name__ == "__main__":
    main()
