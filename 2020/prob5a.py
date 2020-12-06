#!/usr/bin/env python

def process_bp(bp):
    low = 0
    high = 127
    for c in bp[:7]:
        if c == "F":
            high = low + (high - low) // 2
        if c == "B":
            low = low + (high - low) // 2 + 1

    row = low

    low = 0
    high = 7
    for c in bp[7:]:
        if c == "L":
            high = low + (high - low) // 2
        if c == "R":
            low = low + (high - low) // 2 + 1
    column = low

    return row, column


def calc_seat_id(row, column):
    return row * 8 + column


with open("prob5.in") as fp:
    bps = [line.strip() for line in fp.readlines()]
    
print("Total of {} boarding passes.".format(len(bps)))

ids = [calc_seat_id(*process_bp(bp)) for bp in bps]

print("Highest ID is {}.".format(max(ids)))
