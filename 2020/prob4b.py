#!/usr/bin/env python

def process_entry(data):
    entry = {}
    for field in data.split():
        f = field.split(":")
        if len(f) == 2:
            entry[f[0].strip()] = f[1].strip()
    return entry


def is_valid_entry(entry):
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    # optionad_keys = ["cid"]

    for key in required_keys:
        if not key in entry.keys():
            return False

    # byr:
    # >= 1920, <= 2002
    byr = int(entry["byr"])
    if not (byr >= 1920 and byr <= 2002):
        return False

    # iyr
    # >= 2010, <= 2020
    iyr = int(entry["iyr"])
    if not (iyr >= 2010 and iyr <= 2020):
        return False

    # eyr
    # >= 2020, <= 2030
    eyr = int(entry["eyr"])
    if not (eyr >= 2020 and eyr <= 2030):
        return False

    # hgt
    # number + "cm" | "in"
    # cm: >= 150, <= 193
    # in: >= 59, <= 76
    unit = entry["hgt"][-2:]
    if unit in ("cm", "in"):
        height = int(entry["hgt"][:-2])
        if unit == "cm" and not (height >= 150 and height <= 193):
            return False
        if unit == "in" and not (height >= 59 and height <= 76):
            return False
    else:
        return False

    # hcl:
    # html color code (hex)
    hcl = entry["hcl"]

    if not hcl[0] == "#":
        return False
    if not len( [n for n in hcl if n in "0123456789ABCDEFabcdef"] ) == 6:
        return False

    # ecl:
    # amb blu brn gry grn hzl oth
    if entry["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return False

    # pid:
    # nine digits, #########
    pid = [n for n in entry["pid"] if n.isdigit()]
    if not len(pid) == 9:
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
