#!/usr/bin/env python3


def sort(unsorted_list):
    return sorted(unsorted_list)


def reverse(ordered_list):
    return list(reversed(ordered_list))


values = [10, 40, 30, 20, 5]
print(sort(values))
print(reverse(values))
print(reverse(sort(values)))
print(values)
