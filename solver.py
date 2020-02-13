import numpy as np
import time

grid = [[6, 0, 0, 0, 9, 0, 1, 0, 0],
        [0, 7, 9, 1, 6, 0, 2, 0, 5],
        [0, 0, 1, 3, 0, 0, 7, 0, 0],
        [0, 0, 5, 0, 4, 6, 0, 0, 2],
        [0, 0, 3, 0, 0, 0, 4, 0, 0],
        [2, 0, 0, 5, 8, 0, 9, 0, 0],
        [0, 0, 8, 0, 0, 5, 6, 0, 0],
        [1, 0, 7, 0, 3, 4, 5, 9, 0],
        [0, 0, 6, 0, 2, 0, 0, 0, 4]]

solved = False


def possible(y, x, n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    sx = (x // 3) * 3
    sy = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[sy+i][sx+j] == n:
                return False
    return True


def solve():

    global grid
    global solved
    if solved is not True:
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1, 10):
                        if possible(y, x, n):
                            grid[y][x] = n
                            solve()
                            grid[y][x] = 0
                    return
        solved = True
        print(np.array(grid))


start = time.time()
solve()
print(f'Solved in {(time.time() - start):.6f} seconds.')

