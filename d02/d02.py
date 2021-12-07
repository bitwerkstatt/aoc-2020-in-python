class PasswordValidator:

    def __init__(self, raw_input):
        self.raw_input = raw_input

    def parse_line(self, line):
        policy, password = line.split(":")
        constraints, test_char = policy.split(" ")
        constraint1, constraint2 = [int(n) for n in constraints.split("-")]
        return password, constraint1, constraint2, test_char

    def solve_part1(self):
        valid_passwords = 0
        for entry in self.raw_input:
            password, min_card, max_card, test_char = self.parse_line(entry)
            if password.count(test_char) in range(min_card, max_card + 1):
                valid_passwords += 1
        return valid_passwords

    def solve_part2(self):
        valid_passwords = 0
        for entry in self.raw_input:
            password, pos1, pos2, test_char = self.parse_line(entry)
            #This works, because each password starts with a space
            valid_passwords += (password[pos1] == test_char or password[pos2] == test_char) \
                               and not (password[pos1] == test_char and password[pos2] == test_char)
        return valid_passwords
