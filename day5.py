def parse_input():
    with open("inputs/day5.txt") as f:
        return [l.strip() for l in f.readlines()]

# Boarding pass rows are are just binary in disguise.
# Map F -> 0 and B -> 1 and convert the string to decimal.
def get_row(p):
    binary = p.replace('F', '0').replace('B', '1')
    return int(binary, 2)

# Same goes for seats: L -> 0 and R -> 1.
def get_seat(p):
    binary = p.replace('L', '0').replace('R', '1')
    return int(binary, 2)

def part1(passes):
    max_id = 0
    for p in passes:
        row, seat = get_row(p[:7]), get_seat(p[7:])
        cur_id = row * 8 + seat
        if cur_id > max_id:
            max_id = cur_id
    print(f"Max seat ID is {max_id}.")

def part1_oneliner(passes):
    print(f"Max seat ID is {max([get_row(p[:7]) * 8 + get_seat(p[7:]) for p in passes])}.")

def part2(passes):
    ids = sorted([get_row(p[:7]) * 8 + get_seat(p[7:]) for p in passes])
    for idx, cur_id in enumerate(ids):
        if idx + 1 == len(ids):
            print("Last seat, bailing.")
        elif ids[idx + 1] - cur_id != 1:
            print(f"Your seat ID is between {cur_id} and {ids[idx + 1]}, so it must be {cur_id + 1}.")
            break


if __name__ == "__main__":
    passes = parse_input()
    part1(passes)
    part2(passes)