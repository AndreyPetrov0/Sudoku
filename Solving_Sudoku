from Validate_Sudoku import *

class Solving_sudoku:
    empty_sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    def __init__(self, *cord_num):
        self.cord_num = cord_num

    def completing_sudoku(self) -> list:
        ''' function for completing sudoku '''
        for i in self.cord_num:
            self.empty_sudoku[i[0]][i[1]] = i[2]
        return self.empty_sudoku

    def available_numbers(self, row_num: int, colum_num: int) -> set:
        ''' function for checking columns, rows and individual squares '''
        full_set_numbers = {1,2,3,4,5,6,7,8,9}
        possible_numbers = set()
        for i in self.empty_sudoku[row_num]:
            if i != 0:
                possible_numbers.add(i)
        for colum_check in self.empty_sudoku:
            if colum_check[colum_num] != 0:
                possible_numbers.add(colum_check[colum_num])

        start_colum, end_colum = 0, 0
        start_row, end_row = 0, 0

        if colum_num < 3:
            start_colum, end_colum = 0 , 3
        elif colum_num >= 3 and colum_num < 6:
            start_colum, end_colum = 3 , 6
        elif colum_num >= 6:
            start_colum, end_colum = 6 , 9

        if row_num < 3:
            start_row, end_row = 0 , 3
        elif row_num >= 3 and row_num < 6:
            start_row, end_row = 3 , 6
        elif row_num >= 6:
            start_row, end_row = 6 , 9

        for index in range(start_row, end_row):
            for number in self.empty_sudoku[index][start_colum: end_colum]:
                if number != 0:
                    possible_numbers.add(number)

        return full_set_numbers - possible_numbers


    def sudoku_solution(self) -> list:
        ''' function for solving sudoku (completes the sudoku puzzle only once)'''
        count_zero = 81 - len(self.cord_num)
        while count_zero > 0:
            for row in range(len(self.empty_sudoku)):
                for num_ind in range(len(self.empty_sudoku[row])):
                    if self.empty_sudoku[row][num_ind] == 0:
                        ave_num: set = self.available_numbers(row, num_ind)
                        if len(ave_num) == 1:
                            self.empty_sudoku[row][num_ind] = list(ave_num)[0]
                            count_zero -= 1
        return self.empty_sudoku


S = Solving_sudoku([0, 5, 4], [0, 6, 5], [0, 7, 3], [0, 8, 1], [1, 0, 8], [1, 1, 3], [1, 2, 1], [1, 5, 7], [1, 6, 6], [1, 8, 9], [2, 0, 5], [2, 1, 4], [2, 2, 9], [2, 6, 8], [2, 8, 7], [3, 1, 2], [3, 3, 5], [3, 5, 1], [3, 7, 7], [4, 0, 4], [4, 1, 1], [4, 6, 9], [4, 7, 6], [5, 1, 6], [5, 2, 3], [5, 4, 2], [6, 4, 3], [6, 6, 4], [6, 7, 9], [6, 8, 6], [7, 1, 9], [7, 3, 7], [7, 4, 4], [7, 7, 1], [8, 0, 2], [8, 1, 8], [8, 5, 6], [8, 6, 7])
print(*S.completing_sudoku(), sep='\n')
print('---------------------------')
print(*S.sudoku_solution(), sep='\n')
R = Validate_sudoku(S.empty_sudoku)
print(R.is_valid())
