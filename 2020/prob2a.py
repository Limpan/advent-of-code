#!/usr/bin/env python

with open("prob2.in") as fp:
    corrupted_data = [line.split(":") for line in fp.readlines()]

valid_passwords = []
for policy, data in corrupted_data:
    limits, char = policy.split(" ")
    min_, max_ = [int(i) for i in limits.split("-")]

    count = data.count(char)

    if count >= min_ and count <= max_:
        valid_passwords.append(data)

print(len(valid_passwords))