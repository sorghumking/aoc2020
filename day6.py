from os.path import basename

# Return a list where each element is a list of the individual responses of each group.
def parse_input(input_file):
    responses = []
    with open(input_file) as f:
        cur = []
        for l in f.readlines():
            if l.strip() == "":
                responses.append(cur)
                cur = []
            else:
                cur.append(l.strip())
    if cur != []:
        responses.append(cur)
    return responses

def part1(responses):
    group_responses = ["".join(gr) for gr in responses] # mash each group's responses into a single string
    group_counts = [len(set(r)) for r in group_responses] # count unique questions answered by each group
    print(f"Total count = {sum(group_counts)}.")

def count_all_yes(group_responses):
    answered_qs = list(set("".join(group_responses))) # all questions answered by at least one individual
    all_yes = 0
    for q in answered_qs:
        answers = [q in answer for answer in group_responses]
        if False not in answers: # did everyone respond yes to the current question?
            all_yes += 1
    return all_yes

def part2(responses):
    all_yes_counts = [count_all_yes(group_responses) for group_responses in responses]
    print(f"Total all-yes responses = {sum(all_yes_counts)}.")

if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    responses = parse_input(input_file)
    part1(responses)
    part2(responses)
