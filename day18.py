from os.path import basename
import re

# return list of each operand and operator, with nested lists for parentheses
def parse_input(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()
    probs = []
    for l in lines:
        l = l.replace(' ', '')
        cur_list = []
        list_stack = []
        idx = 0
        while True:
            c = l[idx]
            if c in ['+','*','(',')']:
                if c in ['+', '*']:
                    cur_list.append(c)
                elif c == '(':
                    list_stack.append(cur_list)
                    cur_list = []
                elif c == ')':
                    parent = list_stack.pop()
                    parent.append(cur_list)
                    cur_list = parent
                idx += 1
            else: # parse number
                p = re.compile("[0-9]+")
                m = p.match(l[idx:])
                cur_list.append(int(m.group()))
                idx += len(m.group())
            if idx >= len(l):
                probs.append(cur_list)
                break
    return probs

def evaluate(exp, precedence):
    op = None
    cur_exp = exp
    for cur_op in precedence if precedence is not None else [0]: # loop once if no precedence
        vals = []
        new_exp = []
        for idx, c in enumerate(cur_exp):
            if type(c) is list:
                vals.append(evaluate(c, precedence))
            elif type(c) is int:
                vals.append(c)
            else:
                op = c

            if len(vals) == 2: 
                if precedence is not None and op != cur_op:
                    # op has lower preference than current, stash values
                    # and proceed; op will be computed on a future loop.
                    new_exp.append(vals[0])
                    new_exp.append(op)
                    vals = [vals[1]]
                else:
                    result = compute(op, vals[0], vals[1])
                    vals = [result]
        cur_exp = new_exp + [vals[0]]
    return vals[0]

def compute(op, val1, val2):
    if op == '+':
        return val1 + val2
    elif op == '*':
        return val1 * val2

def part1(probs):
    results = [evaluate(p, None) for p in probs]
    print(f"Sum of all results is {sum(results)}")

def part2(probs):
    results = [evaluate(p, ['+', '*']) for p in probs]
    print(f"Sum of all results is {sum(results)}")

if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    probs = parse_input(input_file)
    part1(probs)
    part2(probs)
