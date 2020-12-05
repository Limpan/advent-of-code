#!/usr/bin/env python

with open("prob3.in") as fp:
    slope = [row.strip() for row in fp.readlines()]

x, y = 0, 0
x_step = 3
trees = 0
width = len(slope[0])

print("Slope width is {} and has the length {}.".format(width, len(slope)))

for level in slope:
    if level[x] == "#":
        trees += 1

    x = (x + x_step) % width

print("Encounter {} trees.".format(trees))