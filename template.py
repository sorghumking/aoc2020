from os.path import basename

def parse_input(input_file):
    with open(input_file) as f:
        return [l.strip() for l in f.readlines()]

def part1(foo):
    pass

def part2(foo):
    pass

if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    foo = parse_input(input_file)
    # part1(foo)
    # part2(foo)
