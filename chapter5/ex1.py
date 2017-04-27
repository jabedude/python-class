#!/usr/bin/env python3


def pos_elements(num_list):
    ''' returns positive elements in num_list '''
    pos_list = []
    for num in num_list:
        if num > 0:
            pos_list.append(num)
    return pos_list


test_list = range(-3, 10)
print(pos_elements(test_list))
