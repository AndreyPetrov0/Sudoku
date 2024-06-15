import itertools
import random
from Validate_Sudoku import *


class Create_sudoku:

    def permutations_int(self):
        for i in itertools.permutations('120', 3):
            yield list(map(int, i))

    def create(self):
        sudoku = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
        random.shuffle(sudoku[0])
        for step in range(8):
            row = []
            three_parts = [sudoku[step][:3], sudoku[step][3:6], sudoku[step][6:]]
            permutation = self.permutations_int()

            for i in range(3):
                three_parts = [three_parts[1], three_parts[2], three_parts[0]]
                call_permut = next(permutation)
                row.append(three_parts[0][call_permut[0]])
                row.append(three_parts[0][call_permut[1]])
                row.append(three_parts[0][call_permut[2]])
            sudoku.append(row)
        return sudoku


W = Create_sudoku().create()
print(*W, sep='\n')
S = Validate_sudoku(W)
print(S.is_valid())
