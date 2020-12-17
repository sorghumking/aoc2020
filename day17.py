from os.path import basename
from itertools import product

# return list of 3d/4d coords of active cubes
def parse_input(input_file, fourd=False):
    grid = []
    with open(input_file) as f:
        for y, l in enumerate(f.read().splitlines()):
            for x, c in enumerate(l):
                if c == '#':
                    if fourd:
                        grid.append((x,y,0,0))
                    else:
                        grid.append((x,y,0))
    return grid

# return all points adjacent to pt
def adjacent(pt, include_self=False):
    adj = list(product([-1,0,1],repeat=3))
    if not include_self:
        adj.remove((0,0,0))
    return [(pt[0]+adj[idx][0], pt[1]+adj[idx][1], pt[2]+adj[idx][2]) for idx in range(len(adj))]

# return all points adjcent to points in pts
def all_adjacent(pts, include_self):
    adj = []
    for pt in pts:
        adj += adjacent(pt, include_self)
    return list(set(adj))

# return all points adjacent to pt - 4D flavor
def adjacent4d(pt, include_self=False):
    adj = list(product([-1,0,1],repeat=4))
    if not include_self:
        adj.remove((0,0,0,0))
    return [(pt[0]+adj[idx][0], pt[1]+adj[idx][1], pt[2]+adj[idx][2], pt[3]+adj[idx][3]) for idx in range(len(adj))]

# return all points adjacent to points in pts - 4D flavor
def all_adjacent4d(pts, include_self):
    adj = []
    for pt in pts:
        adj += adjacent4d(pt, include_self)
    return list(set(adj))

def active(grid, pt):
    return pt in grid

def part1(grid):
    # print_grid(grid)
    for cycle in range(6):
        remove = []
        add = []
        adj = all_adjacent(grid, include_self=True)
        for curpt in adj: # one cycle
            adj_active = [pt for pt in adjacent(curpt) if active(grid, pt)]
            if active(grid, curpt):
                if len(adj_active) not in [2,3]:
                    remove.append(curpt)
            else:
                if len(adj_active) == 3:
                    add.append(curpt)
        for r in remove:
            grid.remove(r)
        grid += add
        # print(f"After cycle {cycle + 1}")
        # print_grid(grid)
    print(f"Active cubes: {len(grid)}")

def bounds(grid):
    x = [g[0] for g in grid]
    y = [g[1] for g in grid]
    z = [g[2] for g in grid]
    return min(x), max(x), min(y), max(y), min(z), max(z)

def bounds4d(grid):
    x = [g[0] for g in grid]
    y = [g[1] for g in grid]
    z = [g[2] for g in grid]
    w = [g[2] for g in grid]
    return min(x), max(x), min(y), max(y), min(z), max(z), min(w), max(w)

def print_grid(grid):
    bds = bounds(grid)
    print(f"Bounds = {bds}")
    for z in range(bds[4],bds[5]+1):
        print(f"z = {z}")
        for y in range(bds[2], bds[3]+1):
            for x in range(bds[0], bds[1]+1):
                if (x,y,z) in grid:
                    print("#", end='')
                else:
                    print(".", end='')
            print("")
        print("")

# Instead of attempting to bend mind around 4d, just make 4d versions of
# applicable fns and imitate part1(). Run and wait, last three cycles are
# slow.
def part2(grid):
    print("Be patient, this will take several minutes...")
    for cycle in range(6):
        print(f"Cycle {cycle+1}")
        remove = []
        add = []
        adj = all_adjacent4d(grid, include_self=True)
        print(f"{len(adj)} points to consider...")
        for curpt in adj: # one cycle
            adj_active = [pt for pt in adjacent4d(curpt) if active(grid, pt)]
            if active(grid, curpt):
                if len(adj_active) not in [2,3]:
                    remove.append(curpt)
            else:
                if len(adj_active) == 3:
                    add.append(curpt)
        for r in remove:
            grid.remove(r)
        grid += add
    print(f"Active cubes: {len(grid)}")


if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    grid3d = parse_input(input_file)
    part1(grid3d)
    grid4d = parse_input(input_file, fourd=True)
    part2(grid4d)