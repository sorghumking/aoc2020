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
                elif len(items.split("|")) == 1:
                    rules[num] = [int(r) for r in items.split(" ")]
                else:
                    rules[num] = []
                    for i in items.split(" | "):
                        rules[num].append([int(r) for r in i.split(" ")])
            else:
                messages.append(l)
    return rules, messages


def part1(rules, messages):
    total_matches = 0
    for m in messages:
        r0 = resolve_rule(0, rules)
        if match(r0, m):
            # print(f"{m} matches!")
            total_matches += 1
    print(f"{total_matches} messages match rule 0.")
    # for rulenum in sorted(rules.keys()):
        # cur_rule = rules[rulenum]
        # rr = resolve_rule(rulenum, rules)
        # print(f"{rulenum}: {rr}")

def match(rule, message):
    matches = True
    idx = 0
    for r in rule:
        if type(r) == str:
            l = len(r)
            test = [r]
        else:
            l = len(r[0])
            test = r
        msg_slice = message[idx:idx+l]
        if msg_slice not in test:
            matches = False
            break
        idx += l
    if len(message[idx:]) > 0: # there's additional text in the message
        matches = False
    return matches

def resolve_rule(rulenum, rules):
    cur_rule = rules[rulenum]
    if type(cur_rule) == str:
        return cur_rule
    # must be a single list of rules, or multiple lists which indicate a pipe (|)
    if type(cur_rule[0]) == int:
        foo = []
        for r in cur_rule:
            rr = resolve_rule(r, rules)
            # if len(rr) == 2:
            #     comb = combine(rr[0], rr[1])
            #     foo.append(comb)
            # else:
            if type(rr[0]) == list:
                funzo = []
                for r in rr:
                    funzo += r
                foo.append(funzo)
            else:
                foo.append(rr)
        return foo
    else: # pipe
        foo = []
        for subrule in cur_rule:
            subfoo = []
            stringy = ""
            for sr in subrule:
                rr = resolve_rule(sr, rules)
                if type(rr) == str:
                    stringy += rr
                else:
                    subfoo.append(rr)
            if stringy != "":
                foo.append(stringy)
            else:
                assert len(subfoo) == 2, f"Unexpected pipe rule length: {cur_rule}"
                # comb = list(product(*subfoo))
                # if type(subfoo[0]) == str:
                comb = combine(subfoo[0], subfoo[1])
                # else:
                #     p1 = list(product(*subfoo[0]))
                #     p2 = list(product(*subfoo[1]))
                #     comb = p1 + p2
                foo.append(comb)
        return foo

def combine(l1, l2):
    result = []
    for x in l1:
        for y in l2:
            result.append(x + y)
    # for x in l2:
    #     for y in l1:
    #         result.append(x + y)
    return result

def part2(foo):
    pass

if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    rules, messages = parse_input(input_file)
    print(rules)
    print(messages)
    part1(rules, messages)
    # part2(foo)
