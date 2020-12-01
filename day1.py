from itertools import combinations

def get_input():
    inputs = []
    with open("inputs/day1.txt") as f:
        inputs = [int(l.strip()) for l in f.readlines()]
    return inputs

# brutish
def part1(entries):
    for idx1 in range(len(entries)):
        for idx2 in range(len(entries)):
            if idx1 == idx2:
                continue
            e1, e2 = entries[idx1], entries[idx2]
            if e1 + e2 == 2020:
                print(f"{e1} + {e2} == 2020! {e1} * {e2} = {e1 * e2}")
                return

def part2(entries):
    combs = combinations(entries, 3) # get all unique 3-tuples from elements in entries
    for c in combs:
        if sum(c) == 2020:
            print(f"sum of {c} == 2020! product = {c[0] * c[1] * c[2]}")
            return

if __name__ == "__main__":
    # print(get_input())
    entries = get_input()
    part1(entries)
    part2(entries)
