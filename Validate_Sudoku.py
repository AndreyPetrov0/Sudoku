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
