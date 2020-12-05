#!/usr/bin/env python

with open("prob1.in") as fp:
    values = [int(i) for i in fp.readlines()]

limit = len(values)

for i in range(limit):
    for j in range(i, limit):
        for k in range(j, limit):
            if values[i] + values[j] + values[k] == 2020:
                print(values[i] * values[j] * values[k])