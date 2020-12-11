from os.path import basename
import copy

def parse_input(input_file):
    seats = []
    with open(input_file) as f:
        for l in f.readlines():
            seats.append([c for c in l.strip()])
    return seats

class Layout:
    def __init__(self, seats):
        self.seats = seats # list of rows (input lines)
        self.width = len(self.seats[0])
        self.height = len(self.seats)
        self.slopes = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

    def at(self, pos):
        # assert self.valid_x(pos[0])
        # assert self.valid_y(pos[1])
        return self.seats[pos[1]][pos[0]]

    def set_at(self, pos, val):
        # assert self.valid_x(pos[0])
        # assert self.valid_y(pos[1])
        self.seats[pos[1]][pos[0]] = val

    def search_line(self, pos, slope):
        cur_pos = (pos[0] + slope[0], pos[1] + slope[1])
        while self.valid_x(cur_pos[0]) and self.valid_y(cur_pos[1]):
            val = self.at(cur_pos)
            if val in ['#', 'L']:
                return val
            cur_pos = (cur_pos[0] + slope[0], cur_pos[1] + slope[1])
        return '.'

    def count(self, search_val):
        total = 0
        for y, row in enumerate(self.seats):
            for x, val in enumerate(row):
                if self.at((x,y)) == search_val:
                    total += 1
        return total

    def valid_x(self, x):
        return x >= 0 and x < self.width

    def valid_y(self, y):
        return y >= 0 and y < self.height

    def can_occupy(self, pos):
        adj = [self.at(p) for p in self.adjacent(pos)]
        return '#' not in adj

    def can_occupy_part2(self, pos):
        visible = [self.search_line(pos, s) for s in self.adjacent_slopes(pos)]
        return '#' not in visible

    def can_empty(self, pos):
        adj = [self.at(p) for p in self.adjacent(pos)]
        return adj.count('#') >= 4

    def can_empty_part2(self, pos):
        visible = [self.search_line(pos, s) for s in self.adjacent_slopes(pos)]
        return visible.count('#') >= 5


    # return all valid positions adjacent to pos
    def adjacent(self, pos):
        adj_pos = [(pos[0] + dx, pos[1] + dy) for dx,dy in self.slopes]
        return [ap for ap in adj_pos if self.valid_x(ap[0]) and self.valid_y(ap[1])]

    # return all valid slopes adjacent to pos
    def adjacent_slopes(self, pos):
        adj_pos = [(pos[0] + dx, pos[1] + dy, (dx,dy)) for dx,dy in self.slopes]
        return [ap[2] for ap in adj_pos if self.valid_x(ap[0]) and self.valid_y(ap[1])]

class LineOfSightLayout(Layout):
    def __init__(self, seats):
        Layout.__init__(seats)

    def can_empty(self, pos):
        visible = [self.search_line(pos, s) for s in self.adjacent_slopes(pos)]
        return visible.count('#') >= 5

    def can_occupy(self, pos):
        visible = [self.search_line(pos, s) for s in self.adjacent_slopes(pos)]
        return '#' not in visible


def part1(seats):
    state = Layout(seats)
    print(f"{state.count('#')} seats are occupied, {state.count('L')} seats are unoccupied.")
    count = 0
    while True:
        new_state = update(state)
        count += 1
        if new_state.seats == state.seats:
            total = new_state.count('#')
            print(f"Cycle {count}, no change! {total} seats are occupied.")
            break
        else:
            state.seats = copy.deepcopy(new_state.seats)


def update(state):
    new_state = Layout(copy.deepcopy(state.seats))
    for y, row in enumerate(state.seats):
        for x, val in enumerate(row):
            pos = (x,y)
            if val == 'L':
                if state.can_occupy(pos):
                    new_state.set_at(pos, '#')
            elif val == '#':
                if state.can_empty(pos):
                    new_state.set_at(pos, 'L')
    return new_state

def update_part2(state):
    new_state = Layout(copy.deepcopy(state.seats))
    for y, row in enumerate(state.seats):
        for x, val in enumerate(row):
            pos = (x,y)
            if val == 'L':
                if state.can_occupy_part2(pos):
                    new_state.set_at(pos, '#')
            elif val == '#':
                if state.can_empty_part2(pos):
                    new_state.set_at(pos, 'L')
    return new_state    

def part2(seats):
    state = Layout(seats)
    print(f"{state.count('#')} seats are occupied, {state.count('L')} seats are unoccupied.")
    count = 0
    while True:
        new_state = update_part2(state)
        count += 1
        if new_state.seats == state.seats:
            total = new_state.count('#')
            print(f"Cycle {count}, no change! {total} seats are occupied.")
            break
        else:
            state.seats = copy.deepcopy(new_state.seats)


if __name__ == "__main__":
    input_file = "inputs/{}.txt".format(basename(__file__).replace(".py", ""))
    seats = parse_input(input_file)
    # part1(seats)
    part2(seats)
