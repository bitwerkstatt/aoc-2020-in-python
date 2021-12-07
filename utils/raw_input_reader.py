class RawInputReader(object):

    def __init__(self, filename):
        self.filename = filename
        self.raw_input = []

    def read_file(self):
        with open(self.filename, "r") as in_file:
            for line in in_file:
                self.raw_input.append(line.strip())
        return self.raw_input


