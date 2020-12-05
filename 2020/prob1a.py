#!/usr/bin/env python

with open("prob1.in") as fp:
    values = [int(i) for i in fp.readlines()]

for i in range(len(values)):
    for j in range(i, len(values)):
        if values[i] + values[j] == 2020:
            print(values[i] * values[j])
