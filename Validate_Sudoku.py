import copy

class Validate_sudoku(object):
    def __init__(self, data: list):
        self.data = data

    def is_valid(self) -> bool:
        if len(self.data) < 1:
            return False

        if all([all(map(lambda x: type(x) == int and x > 0 and x <= len(i), i)) for i in self.data]) != True:
            return False

        if self.validate_dimension(self.data) != True:
            return False

        if self.colum_and_row_validate(self.data) != True:
            return False

        if self.little_squares_validate(self.data) != True:
            return False

        return True

    @staticmethod
    def validate_dimension(enter_sudoku: list) -> bool:
        ''' function checks the ratio of rows and columns '''
        return all([all(map(lambda x: len(enter_sudoku) == len(i), i)) for i in enter_sudoku])

    @staticmethod
    def little_squares_validate(enter_sudoku: list) -> bool:
        ''' function for checking small sudoku elements '''
        if len(enter_sudoku) == 1:
            return True
        sudoku_squares = copy.deepcopy(enter_sudoku)
        len_colum = len(sudoku_squares[0])
        len_squr = [i for i in range(2, len(sudoku_squares[0])) if len(sudoku_squares[0]) % i == 0][0]
        while len(sudoku_squares) != 0:
            if len(sudoku_squares[0]) == 0:
                sudoku_squares = sudoku_squares[len_squr:]
                if len(sudoku_squares) == 0:
                    return True
            test_column = []
            for ind in range(len_squr):
                test_column += (sudoku_squares[ind][:len_squr])
                sudoku_squares[ind] = sudoku_squares[ind][len_squr:]
            if len_colum != len(set(test_column)):
                return False

    @staticmethod
    def colum_and_row_validate(enter_sudoku: list) -> bool:
        ''' function for checking colums and row sudoku '''
        for i in range(len(enter_sudoku)):
            if len({*enter_sudoku[i]}) != len(enter_sudoku[i]):
                return False
            diff_num = set()
            for colum in enter_sudoku:
                diff_num.add(colum[i])
            if len(diff_num) != len(enter_sudoku[0]):
                return False
        return True

if __name__ == '__main__':
    # Valid Sudoku
    goodSudoku1 = Validate_sudoku([
        [7, 8, 4, 1, 5, 9, 3, 2, 6],
        [5, 3, 9, 6, 7, 2, 8, 4, 1],
        [6, 1, 2, 4, 3, 8, 7, 5, 9],

        [9, 2, 8, 7, 1, 5, 4, 6, 3],
        [3, 5, 7, 8, 4, 6, 1, 9, 2],
        [4, 6, 1, 9, 2, 3, 5, 8, 7],

        [8, 7, 6, 3, 9, 4, 2, 1, 5],
        [2, 4, 3, 5, 6, 1, 9, 7, 8],
        [1, 9, 5, 2, 8, 7, 6, 3, 4]
    ])

    goodSudoku2 = Validate_sudoku([
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ])

    # Invalid Sudoku
    badSudoku1 = Validate_sudoku([
        [0, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 1, 9],

        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],

        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 1, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ])

    badSudoku2 = Validate_sudoku([
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1]
    ])

    badSudoku3 = Validate_sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                  [2, 3, 1, 5, 6, 4, 8, 9, 7],
                                  [3, 1, 2, 6, 4, 5, 9, 7, 8],
                                  [4, 5, 6, 7, 8, 9, 1, 2, 3],
                                  [5, 6, 4, 8, 9, 7, 2, 3, 1],
                                  [6, 4, 5, 9, 7, 8, 3, 1, 2],
                                  [7, 8, 9, 1, 2, 3, 4, 5, 6],
                                  [8, 9, 7, 2, 3, 1, 5, 6, 4],
                                  [9, 7, 8, 3, 1, 2, 6, 4, 5]])


    print(goodSudoku1.is_valid())    # True, 'Testing valid 9x9'
    print(goodSudoku2.is_valid())    # True, 'Testing valid 4x4'
    print(badSudoku1.is_valid())     # False, 'Values in wrong order'
    print(badSudoku2.is_valid())     # False, '4x5 (invalid dimension)'
    print(badSudoku3.is_valid())     # False little squares validate
