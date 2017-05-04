#!/usr/bin/env python3
''' Code for exercise 6 chapter 9 '''
import sys
import os


def main():
    '''
    Displays file name, size, and modification date for files in
    directory bigger than given size
    '''
    dir_name = sys.argv[1]
    min_size = int(sys.argv[2])
    file_dict = dict()
    msg = '''Filename: {}
Size: {}
Modification Date: {}'''

    dir_list = os.listdir(dir_name)
    for dir_item in dir_list:
        file_stat = os.stat(dir_name + "/" + dir_item)
        if file_stat.st_size > min_size:
            file_dict[dir_item] = file_stat

    for item in file_dict.items():
        print(msg.format(item[0], item[1][6], item[1][8]))

if __name__ == "__main__":
    main()
