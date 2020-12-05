#!/usr/bin/env python

with open("prob2.in") as fp:
    corrupted_data = [line.split(":") for line in fp.readlines()]

valid_passwords = []
for policy, data in corrupted_data:
    data = data.strip()
    limits, char = policy.split(" ")

    position_a, position_b = [int(i) for i in limits.split("-")]

    if (data[position_a - 1] == char) != (data[position_b - 1] == char):
        valid_passwords.append(data)

print(len(valid_passwords))