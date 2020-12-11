from os.path import basename

from itertools import combinations

def parse_input(input_file):
    with open(input_file) as f:
        return [int(l.strip()) for l in f.readlines()]

def valid_sum(addends, target):
    for x, y in combinations(addends, 2):
        if x + y == target:
            return True
    return False

def part1(numbers, preamble):
    for idx, n in enumerate(numbers[preamble:]):
        if not valid_sum(numbers[idx:idx+preamble], n):
            print(f"{n} cannot be summed from {numbers[idx:idx+preamble]}.")
            part2(numbers, n, idx)
            break

def part2(numbers, target, target_idx):
    for idx in range(target_idx):
        for end_idx in range(idx+1, target_idx):
            addends = numbers[idx:end_idx]
            if sum(addends) == target:
                print(f"{target} is sum of {addends}. Ecryption weakness = {min(addends) + max(addends)}.")
                return

if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    numbers = parse_input(input_file)
    part1(numbers, 25)
