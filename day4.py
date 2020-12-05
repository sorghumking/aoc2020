import re

def parse_input():
    # gather elements of each passport
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

# OH SHIT THIS GOT UGLY
def part2(passports):
    validators = {}
    validators['byr'] = (re.compile("[0-9]{4}$"), lambda x: int(x) >= 1920 and int(x) <= 2002)
    validators['iyr'] = (re.compile("[0-9]{4}$"), lambda x: int(x) >= 2010 and int(x) <= 2020)
    validators['eyr'] = (re.compile("[0-9]{4}$"), lambda x: int(x) >= 2020 and int(x) <= 2030)
    validators['hcl'] = (re.compile("#[0-9a-f]{6}$"), lambda x: True)
    validators['ecl'] = (re.compile("(amb|blu|brn|gry|grn|hzl|oth)$"), lambda x: True)
    validators['pid'] = (re.compile("[0-9]{9}$"), lambda x: True)

    valid_count = 0
    for pp in passports:
        if len(pp) == 8 or (len(pp) == 7 and 'cid' not in pp):
            valid = True
            for key, val in pp.items():
                # appears there are no invalid keys
                # if key not in ['byr', 'iyr', 'eyr', 'hcl', 'ecl', 'pid', 'hgt', 'cid']:
                #     print(f"Invalid key: {key}")
                #     valid = False
                #     break
                if key == 'hgt':
                    if not valid_height(val):
                        print(f"Invalid height: {val}")
                        valid = False
                        break
                elif key != 'cid':
                    pattern, test = validators[key]
                    match = pattern.match(val)
                    if match is None or not test(match.group()):
                        print(f"Invalid {key}: {val}")
                        valid = False
                        break
            if valid:
                valid_count += 1
    print(f"Found {valid_count} valid passports out of {len(passports)} total.")

def valid_height(hgt):
    patt = re.compile("([0-9]+)(cm|in)$")
    match = patt.match(hgt)
    if match is not None:
        amt, unit = match.groups()
        amt = int(amt)
        return (unit == 'in' and amt >= 59 and amt <= 76) or (unit == 'cm' and amt >= 150 and amt <= 193)
    return False

if __name__ == "__main__":
    passports = parse_input()
    # part1(passports)
    part2(passports)
    # print(passports)
