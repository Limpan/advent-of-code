#!/usr/bin/env python


with open("day9.in") as fp:
    values = [int(i) for i in fp.readlines()]


invalid_number = 257342611

index = 0
running_totals = []
while index < len(values):
    running_totals = [value + values[index] for value in running_totals]
    running_totals.append(values[index])
    if invalid_number in running_totals:
        distance = len(running_totals) - running_totals.index(invalid_number)
        contiguous_values = values[index - distance + 1:index + 1]
        sum_ = min(contiguous_values) + max(contiguous_values)
        print("The sum is {}".format(sum_))
        break
    index += 1
