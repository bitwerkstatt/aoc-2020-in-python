class DayOneSolver:

    def __init__(self, raw_input):
        self.raw_input = raw_input

    def solve_part1(self):
        num_input = [int(n) for n in self.raw_input]
        return max(a*b for a in num_input for b in num_input if a + b == 2020)


    def solve_part2(self):
        num_input = [int(n) for n in self.raw_input]
        return max(a * b * c for a in num_input for b in num_input for c in num_input if a + b + c == 2020)

