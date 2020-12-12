from os.path import basename
import math
import re

# Return list of (direction, amount) tuples.
def parse_input(input_file):
    dirs = []
    pattern = re.compile("([A-Z]{1})([0-9]+)")
    with open(input_file) as f:
        for l in f.readlines():
            g = pattern.match(l.strip()).groups()
            dirs.append((g[0], int(g[1])))
    return dirs

# Rotate cur_pos by amt in degrees clockwise if True, else counter-clockwise.
def rot(amt, cur_pos, clockwise):
    if clockwise:
        amt *= -1
    rads = amt/90 * math.pi / 2
    c = math.cos(rads)
    s = math.sin(rads)
    rx = cur_pos[0] * c - cur_pos[1] * s
    ry = cur_pos[0] * s + cur_pos[1] * c
    return (int(round(rx)), int(round(ry)))

# Move and rotate the ship.
def part1(dirs):
    delta = (1,0)
    pos = (0,0)
    for d, amt in dirs:
        if d == 'N' or d == 'S':
            amt *= -1 if d == 'S' else 1
            pos = (pos[0], pos[1] + amt)
        elif d == 'E' or d == 'W':
            amt *= -1 if d == 'W' else 1
            pos = (pos[0] + amt, pos[1])
        elif d == 'F':
            pos = (pos[0] + amt * delta[0], pos[1] + amt * delta[1])
        elif d == 'L' or d == 'R':
            delta = rot(amt, delta, clockwise=(d=='R'))
        else:
            assert False, f"Unexpected direction {d}"
    print(f"Final position: {pos}. Manhattan distance from origin = {abs(pos[0])} + {abs(pos[1])} == {abs(pos[0]) + abs(pos[1])}.")

# Move and rotate the waypoint relative to the ship, only 'F' moves ship.
def part2(dirs, way_pos):
    pos = (0,0)
    for d, amt in dirs:
        if d == 'N' or d == 'S':
            amt *= -1 if d == 'S' else 1
            way_pos = (way_pos[0], way_pos[1] + amt)
        elif d == 'E' or d == 'W':
            amt *= -1 if d == 'W' else 1
            way_pos = (way_pos[0] + amt, way_pos[1])
        elif d == 'F':
            pos = (pos[0] + amt * way_pos[0], pos[1] + amt * way_pos[1])
        elif d == 'L' or d == 'R':
            way_pos = rot(amt, way_pos, clockwise=(d=='R'))
        else:
            assert False, f"Unexpected direction {d}"

    print(f"Final position: {pos}. Manhattan distance from origin = {abs(pos[0])} + {abs(pos[1])} == {abs(pos[0]) + abs(pos[1])}.")

if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    dirs = parse_input(input_file)
    part1(dirs)
    part2(dirs, way_pos=(10,1))
