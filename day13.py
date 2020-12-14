from os.path import basename

def parse_input(inputfile):
    raw = ""
    with open("inputs/day13.txt") as f:
        raw = f.readlines()[0].strip()
    return parse_buses(raw)

# Return list of (bus code, wait time) tuples parsed from e.g. "32,x,x,9" string
def parse_buses(raw):
    buses = []
    for idx, c in enumerate(raw.split(",")):
        if c != 'x':
            buses.append((int(c), idx))
    return buses

def part1(time, buses):
    best_bus, best_time = None, 999999
    for b in buses:
        wait_time = b - (time % b)
        if wait_time < best_time:
            best_time = wait_time
            best_bus = b
    print(f"Best bus is {best_bus}, wait of {best_time} minutes. Result: {best_bus * best_time}.")

# Find aligned time and increment for first 2 buses with the largest codes.
# Use that aligned time and increment to find aligned time for 3 buses. Repeat
# until aligned time for all buses is found.
def part2(buses):
    t = 0
    incr = 1
    buses.sort(key=lambda x: -x[0]) # sort from highest to lowest bus code
    for count in range(2, len(buses)+1):
        print(f"For buses {buses[:count]}...")
        new_t, new_incr = find_aligned_time(buses[:count], t, incr)
        t = new_t
        incr = new_incr

def find_aligned_time(buses, t, incr):
    first_time = None
    while True:
        correct = 0
        for bus, wait_time in buses:
            if (t + wait_time) % bus == 0:
                correct += 1
                continue
            else:
                break
        if correct == len(buses):
            if first_time is None:
                print(f"Every bus is aligned at time {t}.")
                first_time = t
            else:
                diff = t - first_time
                print((f"Period between alignments is {diff}."))
                return first_time, diff
        t += incr

if __name__ == "__main__":
    part1(1006605, [19,37,883,23,13,17,797,41,29])
    buses = parse_input("inputs/day13.txt")
    part2(buses)