#!/usr/bin/env python3

def add_dict(num_dict, num):
    new_dict = dict()
    for key, value in num_dict.items():
        new_dict[key] = value + num

    return new_dict

test_dict = {'1': -10, '2': 0, '3': 5, '3': 100}
print(add_dict(test_dict, 3))
