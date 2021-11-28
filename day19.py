from os.path import basename
from itertools import product

def parse_input(input_file):
    rules = {}
    messages = []
    in_messages = False
    with open(input_file) as f:
        for l in f.read().splitlines():
            if l == "":
                in_messages = True
                continue
            if not in_messages:
                num, items = l.split(': ')
                num = int(num)
                if len(items.split(" ")) == 1:
                    tok = items.split(" ")[0]
                    if tok in ['"a"', '"b"']:
                        rules[num] = tok.replace('"', '')
                    else:
                        rules[num] = [int(tok)]
                elif len(items.split("|")) == 1: # no OR
                    rules[num] = [int(r) for r in items.split(" ")]
                else:
                    rules[num] = []
                    for i in items.split(" | "):
                        rules[num].append(tuple([int(r) for r in i.split(" ")]))
            else:
                messages.append(l)
    return rules, messages

def matches_rule(rules, rule, msg, level):
    if isinstance(rule, str):
        # print(f"Rule {rule}, checking against {msg}")
        if not msg[:len(rule)] == rule:
            # print(f"{'  '*level}no match.")
            return 0
        else:
            # print(f"{'  '*level}match!")
            return len(rule)
    elif isinstance(rule[0], int):
        # print(f"{'  '*level} Rule {rule}, must match all")
        trim_msg = msg[:]
        for r in rule:
            result = matches_rule(rules, rules[r], trim_msg, level+1)
            if result <= 0:
                return 0
            else:
                trim_msg = trim_msg[result:]
        return len(msg) - len(trim_msg)
    elif isinstance(rule[0], tuple):
        # print(f"{'  '*level} Compound rule {rule}, must match one")
        for subrule in rule:
            # print(f"{'  '*level} Trying {subrule} with '{msg}'...")
            result = matches_rule(rules, list(subrule), msg, level+1)
            if result > 0:
                return result
        return 0
    else:
        assert False, f"Unexpected rule found: {rule}"
    return -1

if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    rules, messages = parse_input(input_file)
    print(f"Found {len(rules)} rules, {len(messages)} messages.")
    # print(f"{rules}")
    match_count = 0
    for m in messages:
        # print(f"Testing message {m}...")
        result = matches_rule(rules, rules[0], m, 0)
        if result > 0 and result == len(m):
            match_count += 1
            # print(f"{m} matches")
    print(f"{match_count} matches total.")
