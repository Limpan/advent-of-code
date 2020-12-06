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
    # Count number of answers to different questions.
    positive_answers = {}
    for line in entry:
        for question in line:
            if question in positive_answers:
                positive_answers[question] += 1
            else:
                positive_answers[question] = 1
    
    # Filter out the ones where everyone answered.
    all_positive_answers = set()
    for q, n in positive_answers.items():
        if n == len(entry):
            all_positive_answers.add(q)

    groups.append(all_positive_answers)

# Calculate the final answer
answer = sum([len(g) for g in groups])

print("{} groups".format(len(entries)))
print("Answer: {}".format(answer))
