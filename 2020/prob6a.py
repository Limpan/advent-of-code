#!/usr/bin/env python


# Process input
entries = []
part = []
with open("prob6.in") as fp:
    for line in fp.readlines():
        if len(line.strip()) == 0:
            entries.append(part)
            part = []
        else:
            part.append(line.strip())
    if len(part) > 0:
        entries.append(part)

groups = []
for entry in entries:
    positive_answers = set()
    for line in entry:
        for question in line:
            positive_answers.add(question)
    groups.append(positive_answers)

answer = sum([len(g) for g in groups])

print("{} groups".format(len(entries)))
print("Answer: {}".format(answer))
