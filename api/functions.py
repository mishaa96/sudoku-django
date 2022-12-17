import logging
import numpy as np

def get_range(index, size):
    sqrt = int(np.sqrt(size))
    start = index - index % sqrt
    end = sqrt + start
    return start, end

def duplicate_count(find, *arr):
    temp = np.concatenate(arr)
#     print(temp)
    return temp[temp==find].size
    
def used_choices(*arr):
    return np.unique(np.concatenate(arr))

def remaining_choices(*arr):
    return np.setdiff1d(*arr)

def new_puzzle(size, mode):
    # np.random.seed(0)
    if mode == "E":
        empty = np.arange(1, 4)
    elif mode == "M":
        empty = np.arange(2, 5)
    else:
        empty = np.arange(3, 9)
    puzzle = np.zeros((size, size), dtype=int)
    _, puzzle = solve_puzzle(puzzle, size)
    logging.info(_)
    # logging.info(puzzle)
    for row, arr in enumerate(puzzle):
        puzzle_choice = np.random.choice(empty)
        choices = np.arange(0, size)
        for _ in range(1, puzzle_choice + 1):
            random_col = np.random.choice(choices)
            if random_col in choices:
                index = np.argwhere(choices==3)
                np.delete(choices, index)
            puzzle[row][random_col] = 0
    return puzzle

# def solve_puzzle(puzzle, size=None, validate=False):
#     if isinstance(puzzle, list):
#         puzzle = np.array(puzzle)
#     if not size:
#         size = puzzle.shape[0]
#     np.random.seed(0)
#     choices = np.arange(1, 10)
#     puzzle_copy = puzzle.copy()
#     start_row = start_col = puzzle_retry = 0
#     stop_completely = False
#     print("here")
#     while (puzzle[puzzle==0].size or validate) and not stop_completely:
#         for row_index, row in enumerate(puzzle[start_row:, :], start_row):
#             start_col = 0
#             row_retry = 0
#             while (row[row==0].size or validate) and row_retry < size and not stop_completely:
#                 for col_index, cell in enumerate(row[start_col:], start_col):
#                     col = puzzle[:, col_index]
#                     row_start, row_end = get_range(row_index, size)
#                     col_start, col_end = get_range(col_index, size)
#                     grid = puzzle[row_start:row_end, col_start:col_end].reshape(1, 9).flatten()
#                     if cell:
#                         duplicates = duplicate_count(cell, grid, row, col)
#                         if duplicates > 3:
#                             stop_completely = True
#                             break
#                         row_retry = puzzle_retry = size
#                         continue
#                     ignore_choices = used_choices(grid, row, col)
#                     if not remaining_choices(choices, ignore_choices).size:
#                         start_col = col_index-1 if col_index else col_index
#                         row[start_col:] = puzzle_copy[row_index, start_col:]
#                         row_retry += 1
#                         break
#                     value = np.random.choice(remaining_choices(choices, ignore_choices))
#                     puzzle[row_index, col_index] = value
#             if row[row==0].size:
#                 row = puzzle_copy[row_index]
#                 start_row = row_index-1 if row_index else row_index
#                 puzzle[start_row:] = puzzle_copy[start_row:]
#                 puzzle_retry += 1
#                 break
#     if stop_completely or puzzle[puzzle==0].size:
#         return "error", puzzle_copy
#     return "success", puzzle

def solve_puzzle(puzzle, size=None, validate=False):
    if isinstance(puzzle, list):
        puzzle = np.array(puzzle)
    if not size:
        size = puzzle.shape[0]
    choices = np.arange(1, 10)
    puzzle_copy = puzzle.copy()
    start_row = start_col = puzzle_retry = 0
    stop_completely = False
    ## To check 
    while puzzle[puzzle==0].size and not stop_completely:
        for row_index, row in enumerate(puzzle[start_row:, :], start_row):
            start_col = 0
            row_retry = 0
            while row_retry < size and not stop_completely:
                for col_index, cell in enumerate(row[start_col:], start_col):
                    col = puzzle[:, col_index]
                    row_start, row_end = get_range(row_index, size)
                    col_start, col_end = get_range(col_index, size)
                    grid = puzzle[row_start:row_end, col_start:col_end].reshape(1, 9).flatten()
                    if cell:
                        duplicates = duplicate_count(cell, grid, row, col)
                        if duplicates > 3:
                            stop_completely = True
                            break
                        row_retry = puzzle_retry = size
                        continue
                    ignore_choices = used_choices(grid, row, col)
                    if not remaining_choices(choices, ignore_choices).size:
                        start_col = col_index-1 if col_index else col_index
                        row[start_col:] = puzzle_copy[row_index, start_col:]
                        row_retry += 1
                        break
                    value = np.random.choice(remaining_choices(choices, ignore_choices))
                    puzzle[row_index, col_index] = value
            if row[row==0].size:
                row = puzzle_copy[row_index]
                start_row = row_index-1 if row_index else row_index
                puzzle[start_row:] = puzzle_copy[start_row:]
                puzzle_retry += 1
                break
    if puzzle[puzzle==0].size:
        return "error", puzzle_copy
    return "success", puzzle