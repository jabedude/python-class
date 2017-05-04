#!/usr/bin/env python3
''' Code for exercise 4 chapter 10 '''

def build_dict(text_list):
    ''' Docstring '''
    master_dict = dict()
    name_list = [x.split()[0] for x in text_list]
    for name in name_list:
        if name not in master_dict:
            master_dict[name] = {"Desktop" : 0, "Laptop" : 0, "Tablet" : 0}
    return master_dict


def parse_line(line, master_dict):
    ''' Doctring '''
    val_list = line.split()
    master_dict[val_list[0]][val_list[1]] += int(val_list[2])
    # print(master_dict[val_list[0]])
    #print(master_dict)


def main():
    ''' Docstring '''
    with open("computers.txt", "r") as comp_file:
        comp_lines = comp_file.readlines()

    master_dict = build_dict(comp_lines)
    for line in comp_lines:
        parse_line(line, master_dict)
    print(master_dict)

if __name__ == "__main__":
    main()
