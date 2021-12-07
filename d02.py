from timeit import default_timer as timer
from utils import RawInputReader
from d02 import PasswordValidator

if __name__=="__main__":
    reader = RawInputReader("res/d02_input.txt")
    validator = PasswordValidator(reader.read_file())
    start = timer()
    print(validator.solve_part1())
    print(validator.solve_part2())
    end = timer()
    print(f"Execution time in msec.: {end - start}")
