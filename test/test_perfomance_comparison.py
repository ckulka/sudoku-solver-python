import copy
import time
from multiprocessing import Process

from sudoku_solver import sudoku_file_reader, recursive_solver, \
    recursive_options_solver
from sudoku_solver.observer_pattern import Sudoku


def run_observer_pattern(input_data, iterations):
    start = time.time()
    for i in range(iterations):
        input_data_copy = copy.deepcopy(input_data)
        Sudoku(input_data_copy).solve()
    end = time.time()
    print(f"Observer Pattern: {end - start}")


def run_recursive(input_data, iterations):
    start = time.time()
    for i in range(iterations):
        input_data_copy = copy.deepcopy(input_data)
        recursive_solver.solve(input_data_copy)
    end = time.time()
    print(f"Recursive Solver: {end - start}")


def run_recursive_options(input_data, iterations):
    start = time.time()
    for i in range(iterations):
        input_data_copy = copy.deepcopy(input_data)
        recursive_options_solver.solve(input_data_copy)
    end = time.time()
    print(f"Recursive Options Solver: {end - start}")


def run_solver(filename, iterations, timeout):
    print(f"Results for {filename}")
    input_data = sudoku_file_reader.parse(f"test/data/{filename}")
    args = (input_data, iterations)

    action_process = Process(target=run_observer_pattern, args=args)
    action_process.start()
    action_process.join(timeout=timeout)
    action_process.terminate()

    action_process = Process(target=run_recursive_options, args=args)
    action_process.start()
    action_process.join(timeout=timeout)
    action_process.terminate()

    action_process = Process(target=run_recursive, args=args)
    action_process.start()
    action_process.join(timeout=timeout)
    action_process.terminate()


def test_easy():
    run_solver("easy.txt", 10, 2)


def test_realistic_easy():
    run_solver("realistic_easy.txt", 10, 2)
