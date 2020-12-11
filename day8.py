from os.path import basename

def parse_input(input_file):
    instructions = []
    with open(input_file) as f:
        for l in f.readlines():
            l = l.strip()
            cmd, val = l.split(" ")
            instructions.append((cmd, int(val)))
    return instructions

def run(instructions):
    visited = []
    accum = 0
    cur_idx = 0
    while True:
        if cur_idx in visited:
            print(f"Revisiting instruction at index {cur_idx}, accumulator value is {accum}.")
            return False
        elif cur_idx == len(instructions):
            print(f"Program terminated, accumulator value is {accum}.")
            return True
        visited.append(cur_idx)
        cmd, val = instructions[cur_idx]
        if cmd == 'nop':
            cur_idx += 1
        elif cmd == 'jmp':
            cur_idx += val
        elif cmd == 'acc':
            accum += val
            cur_idx += 1
        else:
            assert False, f"Unexpected instruction {cmd}!"

def part1(instructions):
    run(instructions)

def part2(instructions):
    nops_and_jumps = [(idx, cmd) for idx, cmd in enumerate(instructions) if cmd[0] in ['nop', 'jmp']]
    print(nops_and_jumps)
    for idx, cmd in nops_and_jumps:
        mod_instructions = instructions.copy()
        new_op = 'nop' if cmd[0] == 'jmp' else 'jmp'
        mod_instructions[idx] = (new_op, cmd[1])
        if run(mod_instructions):
            break

if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    instructions = parse_input(input_file)
    # part1(instructions)
    part2(instructions)
