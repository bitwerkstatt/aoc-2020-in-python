from timeit import default_timer as timer
from utils import RawInputReader
from d01 import DayOneSolver

if __name__=="__main__":
    reader = RawInputReader("res/d01_input.txt");
    solver = DayOneSolver(reader.read_file())
    start = timer()
    print(solver.solve_part1())
    print(solver.solve_part2())
    end = timer()
    print(f"Execution time in millisec.: {end-start}")
