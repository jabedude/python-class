#!/usr/bin/env python3

text_set = set()
freq_dict = dict()
duplicate_count = 0

while 1:
    data = input("Please enter a line (q to quit): ")

    if data == "q":
        break

    for word in data.split():
        if word in text_set:
            duplicate_count += 1
            freq_dict[word] += 1
            text_set.add(word)
            continue

        freq_dict[word] = 1
        text_set.add(word)

print(sorted(text_set))
print("User gave {} unique entries".format(len(text_set)))
for word, freq in sorted(freq_dict.items(), key=lambda x: x[1], reverse=True):
    print("{} occured {} times".format(word, freq))
