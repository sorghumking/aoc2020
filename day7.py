import re
from os.path import basename

# Return dictionary with elements of form
# key = bag name (adjective + color e.g. "dotted white")
# value = [(subbag count 1, subbag name 1), (subbag count 2, subbag name 2), ...]
def parse_input(input_file):
    bag_dict = {}
    with open(input_file) as f:
        for l in f.readlines():
            bag, subbags = parse_line(l.strip())
            bag_dict[bag] = subbags
    return bag_dict

def parse_line(line):
    bag, contents = line.split(" bags contain ")
    subbags = parse_contents(contents)
    return bag, subbags

def parse_contents(contents):
    result = []
    bags = contents.split(", ")
    if not bags[0].startswith("no"):
        for b in bags:
            count, adj, color, _ = b.split(" ")
            result.append((int(count), adj + ' ' + color))
    return result

def contains(bag_dict, cur_bag_key, search_bag):
    if len(bag_dict[cur_bag_key]) > 0:
        counts, subbags = zip(*bag_dict[cur_bag_key])
        if search_bag in subbags:
            return True
        else:
            for bag_key in subbags:
                if contains(bag_dict, bag_key, search_bag):
                    return True
    return False

def part1(bag_dict):
    count = 0
    for bag_key in bag_dict:
        if contains(bag_dict, bag_key, "shiny gold"):
            count += 1
    print(f"{count} bags can contain shiny gold bags.")

def count_subbags(bag_dict, subbags, level):
    if len(subbags) == 0:
        return 0
    # for count, bag in subbags:
    #     print(f"{' ' * level}{count}, {bag}")
    return sum([count + count * count_subbags(bag_dict, bag_dict[bag], level+1) for count,bag in subbags])

def part2(foo):
    count = count_subbags(bag_dict, bag_dict["shiny gold"], level=0)
    print(f"Shiny gold bags must contain {count} bags.")

if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    bag_dict = parse_input(input_file)
    part1(bag_dict)
    part2(bag_dict)
