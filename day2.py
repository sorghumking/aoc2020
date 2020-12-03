import re

# parse each "[min]-[max] [required char]: [password]" line into a (min, max, required char, password) tuple
def get_input():
    passwords = []
    patt = re.compile("([0-9]+)-([0-9]+) ([a-z]): (.+)")
    with open("inputs/day2.txt") as f:
        for l in f.readlines():
            m = patt.match(l.strip())
            assert len(m.groups()) == 4, f"Unexpected token count of {len(m.groups())}, expected 4!"
            mn, mx, reqchar, pw = m.groups()
            passwords.append((int(mn), int(mx), reqchar, pw))
    return passwords

def part1(passwords):
    valid = 0
    for mn, mx, c, pw in passwords:
        count = pw.count(c)
        if count >= mn and count <= mx:
            valid += 1
    print(f"Part 1: Found {valid} valid passwords out of {len(passwords)} total.")
    return valid

def part2(passwords):
    valid = 0
    for p1, p2, c, pw in passwords:
        p1match = (pw[p1 - 1] == c)
        p2match = (pw[p2 - 1] == c)
        if (p1match and not p2match) or (p2match and not p1match):
            valid += 1
    print(f"Part 2: Found {valid} valid passwords out of {len(passwords)} total.")
    return valid
        

if __name__ == "__main__":
    passwords = get_input()
    part1(passwords)
    part2(passwords)