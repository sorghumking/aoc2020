from os.path import basename
import re

def parse_input(input_file):
    cmds = []
    with open(input_file) as f:
        for l in f.readlines():
            toks = l.strip().split(" = ")
            if toks[0] == 'mask':
                cmds.append((toks[0], toks[1]))
            else:
                addr = re.compile("([0-9]+)").search(toks[0]).group()
                cmds.append(('mem', int(addr), int(toks[1])))
    return cmds

def part1(cmds):
    mask = None
    memory = ["0"]*80000
    for cmd in cmds:
        if cmd[0] == 'mask':
            mask = cmd[1]
        else: # mem
            _, addr, val = cmd
            memory[addr] = apply_mask(mask, val)
    total = sum([int(v,2) for v in memory])
    print(f"Sum of values in memory = {total}.")

def apply_mask(mask, val):
    # print(f"Masking\n{val}\n{mask}")
    binval = bin(val)[2:]
    binval = (36 - len(binval)) * '0' + binval
    new_mem = ""
    for i in range(36):
        if mask[i] == 'X':
            new_mem += binval[i]
        else:
            new_mem += mask[i]
    # print(f"{new_mem}")
    return new_mem

def apply_v2_mask(mask, val):
    addrs = []
    binval = bin(val)[2:]
    binval = (36 - len(binval)) * '0' + binval
    x_inds = []
    new_mem = ""
    for i in range(36):
        if mask[i] == '0':
            new_mem += binval[i]
        elif mask[i] == '1':
            new_mem += '1'
        elif mask[i] == 'X':
            new_mem += 'X'
            x_inds.append(i)

    # generate all possible 2^[count of floating bits] addresses
    perms = 2**len(x_inds)
    for p in range(perms): # replace Xs with digits of binary nums
        bp = bin(p)[2:]
        bp = (len(x_inds) - len(bp)) * '0' + bp
        bp_idx = 0
        new_addr = ""
        for idx, m in enumerate(new_mem):
            if idx in x_inds:
                new_addr += bp[bp_idx]
                bp_idx += 1
            else:
                new_addr += m
        addrs.append(new_addr)
    # print(f"Created {len(addrs)} addresses.")
    # print(addrs)
    return addrs

def part2(cmds):
    mask = None
    # memory = ["0"]*80000
    memory = {}
    for cmd in cmds:
        if cmd[0] == 'mask':
            mask = cmd[1]
        else: # mem
            _, addr, val = cmd
            addrs = apply_v2_mask(mask, addr)
            for a in addrs:
                memory[a] = val
    total = sum([v for k,v in memory.items()])
    print(f"Sum of values in memory = {total}.")


if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    cmds = parse_input(input_file)
    # part1(cmds)
    part2(cmds)
