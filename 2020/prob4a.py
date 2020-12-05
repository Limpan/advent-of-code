#!/usr/bin/env python

def process_entry(data):
    entry = {}
    for field in data.split():
        f = field.split(":")
        if len(f) == 2:
            entry[f[0]] = f[1]
    return entry


def is_valid_entry(entry):
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    # optionad_keys = ["cid"]

    for key in required_keys:
        if not key in entry.keys():
            return False
    
    return True


# Process input
entries = []
part = ""
with open("prob4.in") as fp:
    for line in fp.readlines():
        part += line
        if len(line.strip()) == 0:
            entries.append(process_entry(part))
            part = ""
    if len(part.strip()) > 0:
        entries.append(process_entry(part))

# Filter out invalid entries
entries = list(filter(is_valid_entry, entries))

print("Found {} entries.".format(len(entries)))
