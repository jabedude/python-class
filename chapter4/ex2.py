#!/usr/bin/env python3

text_set = set()
duplicate_count = 0

while 1:
    data = input("Please enter a line (q to quit): ")

    if data == "q":
        break

    for word in data.split():
        if word in text_set:
            duplicate_count += 1

        text_set.add(word)

print(sorted(text_set))
print("User gave {} unique entries".format(len(text_set)))
