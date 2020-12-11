from os.path import basename
import itertools

def parse_input(input_file):
    with open(input_file) as f:
        adapters = [int(l.strip()) for l in f.readlines()]
    adapters.append(0) # outlet
    adapters.append(max(adapters) + 3) # built-in adapter
    adapters.sort()
    return adapters

def part1(adapters):
    ones, threes = 0, 0
    for idx in range(1, len(adapters)):
        diff = adapters[idx] - adapters[idx-1]
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
    print(f"Ones = {ones}, threes = {threes}.")

def count_valid_sequences(r1, seq, r2):
    # print(f"counting valid sequences for {seq}")
    valid = 0
    for seq_len in range(len(seq) + 1):
        for subseq in itertools.combinations(seq, seq_len):
            # print(f"{subseq}")
            if valid_sequence([r1] + list(subseq) + [r2]):
                valid += 1
    return valid

# does sequence have a difference of more than 3 jolts?
def valid_sequence(seq):
    for idx in range(1,len(seq)):
        if seq[idx] - seq[idx-1] > 3:
            return False
    return True

# All adapters with a leading and/or trailing 3-jolt difference must be part of the sequence.
# Call each of these required adapters A0, A1, A2...
# Between each pair of required adapters Ai, Ai+1, count all valid sequences i.e. those
# with no difference greater than 3 jolts.
# The product of these counts is the number of valid sequences.
def part2(adapters):
    # create sorted list of distinct indices of required adapters
    req = [0, len(adapters) - 1] # always need outlet and built-in adapter
    for idx in range(1, len(adapters)):
        if adapters[idx] - adapters[idx-1] == 3:
            req.append(idx-1)
            req.append(idx)
    req = sorted(list(set(req)))

    # find count of valid sequences using the adapters between each pair of required adapters
    valid = 1
    for idx in range(1, len(req)):
        r1, r2 = req[idx-1], req[idx]
        # print(f"Between required adapters {adapters[r1]} and {adapters[r2]}.")
        if r2 - r1 > 1: # no need to count consecutive joltage adapters
            new_valid = count_valid_sequences(adapters[r1], adapters[r1+1:r2], adapters[r2])
            valid *= new_valid
            # print(f"Found {new_valid} seqs, total = {valid}.")
    print(f"Found {valid} valid sequences.")

if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    adapters = parse_input(input_file)
    part1(adapters)
    part2(adapters)