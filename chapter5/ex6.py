#!/usr/bin/env python3


def common_elements(list_one, list_two):
    ''' returns a list of common elements between list_one and list_two '''
    set_one = set(list_one)
    set_two = set(list_two)

    return list(set_one.intersection(set_two))


test_list = ['a', 'b', 'c', 'd', 'e']
test_list2 = ['c', 'd', 'e', 'f', 'g']

test = common_elements(test_list, test_list2)
print(test)
