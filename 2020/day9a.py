#!/usr/bin/env python


def checksum(list_, number):
    for index, first_number in enumerate(list_):
        for second_number in list_[index:]:
            if first_number + second_number == number:
                return True
    return False


with open("day9.in") as fp:
    values = [int(i) for i in fp.readlines()]


history = values[:25]
for number in values[25:]:
    if not checksum(history, number):
        print("The first number that fails the test is {}".format(number))
        break
    history = values[1:] + [number]
