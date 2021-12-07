from timeit import default_timer as timer
from utils import RawInputReader
from d03 import Toggoban

if __name__=="__main__":
    reader = RawInputReader("res/d03_input.txt")
    toggo = Toggoban(reader.read_file())
    print(toggo.solve_part1())
    print(toggo.solve_part2())
