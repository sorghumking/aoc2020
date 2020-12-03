class Forest:
    def __init__(self, forest):
        self.f = forest
        self.width = len(self.f[0])
        self.height = len(self.f)

    def isTree(self, x, y):
        return self.at(x, y) == '#'

    def at(self, x, y):
        x = x % self.width
        assert y < self.height, "Out of the woods!"
        return self.f[y][x]

    def out(self, y):
        return y >= self.height

def get_input():
    forest = []
    with open("inputs/day3.txt") as f:
        for l in f.readlines():
            forest.append(l.strip())
    return forest

def countRouteTrees(forest, slope):
    pos = (0,0)
    f = Forest(forest)
    trees = 0
    while True:
        pos = (pos[0] + slope[0], pos[1] + slope[1])
        if f.out(pos[1]):
            break
        if f.isTree(pos[0], pos[1]):
            trees += 1
    print(f"With slope {slope}, encountered {trees} trees.")
    return trees

def part1(forest):
    trees = countRouteTrees(forest, (3,1))
    print(f"Encountered {trees} trees.")

def part2(forest):
    tree_list = [countRouteTrees(forest, slope) for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]]
    product = 1
    for t in tree_list:
        product *= t
    print(f"Product of encountered trees = {product}")


if __name__ == "__main__":
    forest = get_input()
    part1(forest)
    part2(forest)