class Toggoban:

    def __init__(self, raw_input):
        self.raw_input = raw_input

    def traverse_map(self, steps_right, steps_down):
        x_pos = 0
        y_pos = 0
        hits = 0
        while y_pos < len(self.raw_input):
            if self.raw_input[y_pos][x_pos] == "#":
                hits += 1
            x_pos = (x_pos + steps_right) % len(self.raw_input[0])
            y_pos += steps_down
        return hits

    def solve_part1(self):
        return self.traverse_map(3, 1)

    def solve_part2(self):
        return self.traverse_map(1, 1) * self.traverse_map(3, 1) * self.traverse_map(5, 1) * self.traverse_map(7, 1) * self.traverse_map(1, 2)
