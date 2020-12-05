#!/usr/bin/env python

with open("prob3.in") as fp:
    slope = [row.strip() for row in fp.readlines()]


def traverse(x_step, y_step):
    x, y = 0, 0
    trees = 0
    width = len(slope[0])
    for i in range(0, len(slope), y_step):
        if slope[i][x] == "#":
            trees += 1
        x = (x + x_step) % width

    return trees

a = traverse(1, 1)
b = traverse(3, 1)
c = traverse(5, 1)
d = traverse(7, 1)
e = traverse(1, 2)
res = a*b*c*d*e

print("Result: {}".format(res))