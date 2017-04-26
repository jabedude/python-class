#!/usr/bin/env python3

def greater_than(*args, num):
    count = 0
    for number in args:
        if number > num:
            count += 1
    return count

res = greater_than(5, -10, 10, -20, 30, num=0)
print(res)
