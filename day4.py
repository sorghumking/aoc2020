import re

def parse_input():
    # gather components of each passport
    ppLines = []
    with open("inputs/day4.txt") as f:
        cur = []
        for l in f.readlines():
            if l.strip() == "":
                ppLines.append(cur)
                cur = []
            else:
                cur += l.strip().split(" ")
    if cur != []:
        ppLines.append(cur)

    # build dictionary for each passport
    passports = []
    for ppl in ppLines:
        ppDict = {}
        for elt in ppl:
            toks = elt.split(":")
            ppDict[toks[0]] = toks[1]
        passports.append(ppDict)
    return passports

def part1(passports):
    valid = 0
    for pp in passports:
        if len(pp) == 8:
            valid += 1
        elif len(pp) == 7 and 'cid' not in pp:
            valid += 1
    print(f"Found {valid} valid passports out of {len(passports)} total.")

def in_range(val, mn, mx):
    return val >= mn and val <= mx

def valid_height(match):
    amt, unit = match.groups()
    amt = int(amt)
    return (unit == 'in' and in_range(amt, 59, 76)) or (unit == 'cm' and in_range(amt, 150, 193))

def part2(passports):
    validators = {}
    validators['byr'] = (re.compile("[0-9]{4}$"), lambda x: in_range(int(x.group()), 1920, 2002))
    validators['iyr'] = (re.compile("[0-9]{4}$"), lambda x: in_range(int(x.group()), 2010, 2020))
    validators['eyr'] = (re.compile("[0-9]{4}$"), lambda x: in_range(int(x.group()), 2020, 2030))
    validators['hcl'] = (re.compile("#[0-9a-f]{6}$"), lambda x: True)
    validators['ecl'] = (re.compile("(amb|blu|brn|gry|grn|hzl|oth)$"), lambda x: True)
    validators['pid'] = (re.compile("[0-9]{9}$"), lambda x: True)
    validators['hgt'] = (re.compile("([0-9]+)(cm|in)$"), lambda x: valid_height(x))

    valid_count = 0
    for pp in passports:
        if len(pp) == 8 or (len(pp) == 7 and 'cid' not in pp):
            valid = True
            for key, val in pp.items():
                if key == 'cid':
                    continue
                pattern, test = validators[key]
                match = pattern.match(val)
                if match is None or not test(match):
                    # print(f"Invalid {key}: {val}")
                    valid = False
                    break
            if valid:
                valid_count += 1
    print(f"Found {valid_count} valid passports out of {len(passports)} total.")

if __name__ == "__main__":
    passports = parse_input()
    part1(passports)
    part2(passports)
