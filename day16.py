from os.path import basename
import re

# return list of rules, each a tuple of form (rule name, min1, max1, min2, max2),
# and a list of tickets, each a list of integers. tickets[0] is your ticket.
def parse_input(input_file):
    rules = []
    tickets = []
    in_rules = True
    with open(input_file) as f:
        for l in f.read().splitlines():
            if l == "your ticket:" or l == "nearby tickets:":
                in_rules = False
                continue
            elif l != "":
                if in_rules:
                    r = parse_rule(l)
                    rules.append(r)
                else: # tickets
                    t = parse_ticket(l)
                    tickets.append(t)
    return rules, tickets

def parse_rule(l):
    p = re.compile("([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)")
    m = p.match(l)
    assert len(m.groups()) == 5
    groups = [m.groups()[0]] + [int(g) for g in m.groups()[1:]]
    return tuple(groups)

def parse_ticket(l):
    return [int(n) for n in l.split(',')]

def part1(rules, tickets):
    valid_tickets = []
    invalid_total = 0
    for t in tickets[1:]: # skip your ticket
        valid_ticket = False
        for value in t:
            valid = False
            for _, min1, max1, min2, max2 in rules:
                if (value >= min1 and value <= max1) or (value >= min2 and value <= max2):
                    valid = True
                    break
            if not valid:
                invalid_total += value
                valid_ticket = False
                break
            else:
                valid_ticket = True
        if valid_ticket:
            valid_tickets.append(t)
    print(f"Ticket scanning error rate is {invalid_total}.")
    return tickets[:1] + valid_tickets # include your ticket

def part2(rules, tickets):
    rules_results = []
    rules_names = []

    # for each rule, count all valid entries for each position in a ticket
    for r in rules:
        name, min1, max1, min2, max2 = r
        valid_idxs = [0] * len(tickets[0])
        for t in tickets:
            for idx, value in enumerate(t):
                if (value >= min1 and value <= max1) or (value >= min2 and value <= max2):
                    valid_idxs[idx] += 1
        rules_results.append(valid_idxs)
        rules_names.append(name)


    # Find the entry position at which every ticket has a valid value for a rule, there
    # will be only one. Note that position and name. Ignore that position and search for
    # a new position for which every ticket has a valid value for a rule. Proceed until
    # all rules are accounted for.
    set_rule_names = []
    set_rules = []
    while len(set_rules) < len(rules):
        for ridx in range(len(rules_results)):
            rr = rules_results[ridx]
            # print(f"Rule {rules_names[ridx]}")
            # print(f"{rr}")
            entries = [idx for idx in range(len(rr)) if rr[idx] == len(tickets) and idx not in set_rules]
            # print(f"{rr.count(len(tickets))} possible entries: {entries}")
            if len(entries) == 1:
                set_rule_names.append(rules_names[ridx])
                set_rules.append(entries[0])
                break

    # Gather entry positions of "departure" rules
    departure_idxs = []
    for i, r in enumerate(zip(set_rule_names, set_rules)):
        print(f"Rule {r[0]}: entry {r[1]}")
        if r[0].find("departure") != -1:
            departure_idxs.append(r[1])

    # Compute product of our ticket's departure values
    answer = 1
    for idx in departure_idxs:
        answer *= tickets[0][idx]
    print(f"Your ticket: {tickets[0]}")
    print(f"Departure entry values: {[tickets[0][v] for v in departure_idxs]}")
    print(f"Product of departure entry values is {answer}.")


if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    rules, tickets = parse_input(input_file)
    valid_tickets = part1(rules, tickets)
    # print(f"{len(valid_tickets)} valid tickets out of {len(tickets)}.")
    # print(f"rules count = {len(rules)}, ticket len = {len(tickets[0])}")
    part2(rules, valid_tickets)
