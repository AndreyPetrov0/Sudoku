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
        ''' function for filling sudoku '''
        for cord in self.cord_num:
            self.empty_sudoku[cord[0]][cord[1]] = cord[2]
        return self.empty_sudoku

    class square_definition_interface:
        start_colum, end_colum = 0, 0
        start_row, end_row = 0, 0

        def __init__(self, row_index: int, colum_index: int):
            self.row_index = row_index
            self.colum_index = colum_index
            self.definition(self.row_index, self.colum_index)

        def definition(self, row_index: int, colum_index: int):
            if colum_index < 3:
                self.start_colum, self.end_colum = 0, 3
            elif colum_index >= 3 and colum_index < 6:
                self.start_colum, self.end_colum = 3, 6
            elif colum_index >= 6:
                self.start_colum, self.end_colum = 6, 9

            if row_index < 3:
                self.start_row, self.end_row = 0, 3
            elif row_index >= 3 and row_index < 6:
                self.start_row, self.end_row = 3, 6
            elif row_index >= 6:
                self.start_row, self.end_row = 6, 9


    def available_numbers(self, row_index: int, colum_index: int) -> set:
        ''' function for checking columns, rows and individual squares '''
        full_set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        possible_numbers = set()

        for row_num in self.empty_sudoku[row_index]:
            if row_num != 0:
                possible_numbers.add(row_num)

        for colum_num in self.empty_sudoku:
            if colum_num[colum_index] != 0:
                possible_numbers.add(colum_num[colum_index])

        definition = self.square_definition_interface(row_index, colum_index)

        for index in range(definition.start_row, definition.end_row):
            for number in self.empty_sudoku[index][definition.start_colum: definition.end_colum]:
                if number != 0:
                    possible_numbers.add(number)

        return full_set_numbers - possible_numbers


    def count_ava_num_in_row(self, row_index: int) -> dict:
        ''' function to count the available numbers in a row '''
        ava_row_num = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for ind in range(9):
            if self.empty_sudoku[row_index][ind] == 0:
                ava_num_in_point: set = self.available_numbers(row_index, ind)
                number_appented_twice_in_square: set = self.number_appented_twice_in_square(row_index, ind)
                if list(number_appented_twice_in_square)[0] in ava_num_in_point:
                    ava_num_in_point = ava_num_in_point & number_appented_twice_in_square

                number_appented_twice_in_row = self.number_appented_twice_in_row(row_index)
                ls_nm_row = list(number_appented_twice_in_row)
                if len(ls_nm_row) != 0:
                    if ls_nm_row[0] in ava_num_in_point and ls_nm_row[1] in ava_num_in_point:
                        ava_num_in_point = ava_num_in_point & number_appented_twice_in_row

                for number in ava_num_in_point:
                    ava_row_num[number] += 1
        return ava_row_num


    def count_ava_num_in_colum(self, colum_index: int) -> dict:
        ''' function to count the available numbers in a colum '''
        ava_colum_num = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for ind in range(9):
            if self.empty_sudoku[ind][colum_index] == 0:
                ava_num_in_point: set = self.available_numbers(ind, colum_index)
                number_appented_twice_in_square: set = self.number_appented_twice_in_square(ind, colum_index)
                if list(number_appented_twice_in_square)[0] in ava_num_in_point:
                    ava_num_in_point = ava_num_in_point & number_appented_twice_in_square

                number_appented_twice_in_colum = self.number_appented_twice_in_colum(colum_index)
                ls_nm_co = list(number_appented_twice_in_colum)
                if len(ls_nm_co) != 0:
                    if ls_nm_co[0] in ava_num_in_point and ls_nm_co[1] in ava_num_in_point:
                        ava_num_in_point = ava_num_in_point & number_appented_twice_in_colum

                for number in ava_num_in_point:
                    ava_colum_num[number] += 1
        return ava_colum_num


    def double_bets_in_row(self, row_index: int) -> set:
        ''' function for finding duplicate pairs in a row '''
        double_num = []
        for ind in range(9):
            if self.empty_sudoku[row_index][ind] == 0:
                ava_num_in_point = self.available_numbers(row_index, ind)
                doub_num_in_squar = self.double_bets_in_squares(row_index, ind)
                ava_num = ava_num_in_point - doub_num_in_squar
                if len(ava_num) == 2:
                    double_num.append(tuple(ava_num))
                elif len(ava_num) == 0:
                    double_num.append(tuple(ava_num_in_point))

        for bets in double_num:
            if double_num.count(bets) == 2:
                return set(bets)
        return set()


    def double_bets_in_colum(self, colum_index: int) -> set:
        ''' function for finding duplicate pairs in a column '''
        double_num = []
        for ind in range(9):
            if self.empty_sudoku[ind][colum_index] == 0:
                ava_num_in_point = self.available_numbers(ind, colum_index)
                doub_num_in_squar = self.double_bets_in_squares(ind, colum_index)
                ava_num = ava_num_in_point - doub_num_in_squar
                if len(ava_num) == 2:
                    double_num.append(tuple(ava_num))
                elif len(ava_num) == 0:
                    double_num.append(tuple(ava_num_in_point))

        for bets in double_num:
            if double_num.count(bets) == 2:
                return set(bets)
        return set()


    def double_bets_in_squares(self, row_index: int, colum_index: int) -> set:
        ''' function for finding duplicate pairs in a square '''
        definition = self.square_definition_interface(row_index, colum_index)
        count_zero = 0
        double_num = []
        for index_row in range(definition.start_row, definition.end_row):
            for index_colum in range(definition.start_colum, definition.end_colum):
                if self.empty_sudoku[index_row][index_colum] == 0:
                    count_zero += 1
                    ava_num = self.available_numbers(index_row, index_colum)
                    if len(ava_num) == 2:
                        double_num.append(tuple(ava_num))

        for bets in double_num:
            if double_num.count(bets) == 2 and count_zero != 2:
                return set(bets)
        return set()


    def number_appented_twice_in_square(self, row_index: int, colum_index: int):
        ''' the function finds numbers that occur twice in a square '''
        definition = self.square_definition_interface(row_index, colum_index)

        Count_squares = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

        for index_row in range(definition.start_row, definition.end_row):
            for index_colum in range(definition.start_colum, definition.end_colum):
                if self.empty_sudoku[index_row][index_colum] == 0:
                    ava_num = self.available_numbers(index_row, index_colum)
                    for number in ava_num:
                        Count_squares[number] += 1

        double_num = []
        for index_row in range(definition.start_row, definition.end_row):
            for index_colum in range(definition.start_colum, definition.end_colum):
                if self.empty_sudoku[index_row][index_colum] == 0:
                    dob = []
                    ava_num = self.available_numbers(index_row, index_colum)
                    double_bets = self.double_bets_in_squares(index_row, index_colum)
                    for num in ava_num:
                        if Count_squares[num] == 2:
                            dob.append(num)

                    if len(dob) == 2 and set(dob) != double_bets:
                        double_num.append(set(dob))
                    elif len(dob) == 3 and len(double_num) != 0:
                        if dob[0] in double_num[0] and dob[1] in double_num[0]:
                            double_num.append(set([dob[0], dob[1]]))
                        elif dob [1] in double_num and dob[2] in double_num[0]:
                            double_num.append(set([dob[0], dob[1]]))

        if len(double_num) == 2 and double_num[0] == double_num[1]:
            return double_num[0]
        else:
            return {0}

    def number_appented_twice_in_colum(self, colum_index: int) -> set:
        ''' the function finds numbers that occur twice in colum '''
        ava_colum_num = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for ind in range(9):
            if self.empty_sudoku[ind][colum_index] == 0:
                ava_num_in_point: set = self.available_numbers(ind, colum_index)
                number_appented_twice_in_square: set = self.number_appented_twice_in_square(ind, colum_index)
                ls_e = list(number_appented_twice_in_square)
                if ls_e[0] in ava_num_in_point and ls_e[1] in ava_num_in_point:
                    ava_num_in_point = ava_num_in_point & number_appented_twice_in_square
                for number in ava_num_in_point:
                    ava_colum_num[number] += 1

        double_num = []
        for ind in range(9):
            if self.empty_sudoku[ind][colum_index] == 0:
                dob = []
                ava_num_in_point = self.available_numbers(ind, colum_index)
                double_bets_in_colum = self.double_bets_in_colum(colum_index)
                ava_num = ava_num_in_point - double_bets_in_colum
                for num in ava_num:
                    if ava_colum_num[num] == 2:
                        dob.append(num)
                    elif ava_colum_num[num] == 1:
                        dob = []
                if len(dob) >= 2 and set(dob) != double_bets_in_colum:
                    double_num.append(set(dob))
        for i in double_num:
            if len(i) == 2:
                return i
        else:
            return set()


    def number_appented_twice_in_row(self, row_index: int) -> set:
        ''' the function finds numbers that occur twice in row '''
        ava_row_num = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for ind in range(9):
            if self.empty_sudoku[row_index][ind] == 0:
                ava_num_in_point: set = self.available_numbers(row_index, ind)
                number_appented_twice_in_square: set = self.number_appented_twice_in_square(row_index, ind)
                if list(number_appented_twice_in_square)[0] in ava_num_in_point:
                    ava_num_in_point = ava_num_in_point & number_appented_twice_in_square
                for number in ava_num_in_point:
                    ava_row_num[number] += 1

        double_num = []
        for ind in range(9):
            if self.empty_sudoku[row_index][ind] == 0:
                dob = []
                ava_num = self.available_numbers(row_index, ind)
                double_bets_in_row = self.double_bets_in_row(row_index)
                ava_num = ava_num - double_bets_in_row
                for num in ava_num:
                    if ava_row_num[num] == 2:
                        dob.append(num)
                if len(dob) == 2 and set(dob) != double_bets_in_row:
                    double_num.append(set(dob))
        if len(double_num) == 2 and double_num[0] == double_num[1]:
            return double_num[0]
        else:
            return set()


    def sudoku_solution(self) -> list:
        ''' function for solving sudoku (completes the sudoku puzzle only once) '''
        count_zero = 81 - len(self.cord_num)
        stop_iter = 0
        while count_zero > 0 and stop_iter < 20:
            start_row , end_row = 0 , 3
            # start_row, end_row = 3,6
            for step_level_1 in range(3):
                start_colum , end_colum = 0 , 3
                # start_colum, end_colum = 3,6
                for step_level_2 in range(3):
                    Count_squares = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

                    for step_level_3 in range(2):

                        for index_row in range(start_row, end_row):
                            for index_number in range(start_colum, end_colum):
                                if self.empty_sudoku[index_row][index_number] == 0:
                                    double_bets_in_row: set = self.double_bets_in_row(index_row)
                                    double_bets_in_colum: set = self.double_bets_in_colum(index_number)
                                    double_bets_in_squares: set = self.double_bets_in_squares(index_row, index_number)
                                    ava_num_in_point: set = self.available_numbers(index_row, index_number) - double_bets_in_row - double_bets_in_colum - double_bets_in_squares
                                    number_append = self.number_appented_twice_in_square(index_row, index_number)

                                    if step_level_3 == 0:
                                        stop_checking = False

                                        if len(ava_num_in_point) == 1:
                                            # ************ POINT STEK ***************
                                            self.empty_sudoku[index_row][index_number] = list(ava_num_in_point)[0]
                                            count_zero -= 1
                                            stop_checking = True
                                            # print(*self.empty_sudoku, sep='\n')
                                            # print(f'row - {index_row}')
                                            # print(f'colum - {index_number}')
                                            # print(f'ava_num_in_point==1 - {list(ava_num_in_point)[0]}')
                                        # -----------------------------------------------------------------------------------------
                                        if stop_checking == False:
                                            # ************ ROW STEK ***************
                                            count_row_num: dict = self.count_ava_num_in_row(index_row)
                                            point_in_row: set = self.available_numbers(index_row, index_number)
                                            # ***************************
                                            if tuple(number_append)[0] in point_in_row:
                                                point_in_row = point_in_row & number_append

                                            number_appented_twice_in_row = self.number_appented_twice_in_row(index_row)
                                            ls_nm_row = list(number_appented_twice_in_row)
                                            if len(ls_nm_row) != 0:
                                                if ls_nm_row[0] in point_in_row and ls_nm_row[1] in point_in_row:
                                                    point_in_row = point_in_row & number_appented_twice_in_row

                                            if len(double_bets_in_row) == 2:
                                                count_row_num.pop(list(double_bets_in_row)[0])
                                                count_row_num.pop(list(double_bets_in_row)[1])
                                            for number_row, count_num_row in count_row_num.items():
                                                if count_num_row == 1 and number_row in point_in_row:
                                                    self.empty_sudoku[index_row][index_number] = number_row
                                                    count_zero -= 1
                                                    stop_checking = True
                                                    # print(*self.empty_sudoku, sep='\n')
                                                    # print(f'row - {index_row}')
                                                    # print(f'colum - {index_number}')
                                                    # print(f'count_row_num==1 - {number_row}')
                                        #-----------------------------------------------------------------------------------------
                                        if stop_checking == False:
                                            # ************* COLUM STEK **************
                                            count_colum_num: dict = self.count_ava_num_in_colum(index_number)
                                            point_in_col: set = self.available_numbers(index_row, index_number)
                                            # ***************************
                                            if tuple(number_append)[0] in point_in_col:
                                                point_in_col = point_in_col & number_append

                                            number_appented_twice_in_colum = self.number_appented_twice_in_colum(index_number)
                                            ls_nm_co = list(number_appented_twice_in_colum)
                                            if len(ls_nm_co) != 0:
                                                if ls_nm_co[0] in point_in_col and ls_nm_co[1] in point_in_col:
                                                    point_in_col = ava_num_in_point & number_appented_twice_in_colum

                                            if len(double_bets_in_colum) == 2:
                                                count_colum_num.pop(list(double_bets_in_colum)[0])
                                                count_colum_num.pop(list(double_bets_in_colum)[1])
                                            for number_colum, count_num_colum in count_colum_num.items():
                                                if count_num_colum == 1 and number_colum in point_in_col:
                                                    self.empty_sudoku[index_row][index_number] = number_colum
                                                    count_zero -= 1
                                                    stop_checking = True
                                                    # print(*self.empty_sudoku, sep='\n')
                                                    # print(f'row - {index_row}')
                                                    # print(f'colum - {index_number}')
                                                    # print(f'count_colum_num==1 - {number_colum}')
                                        # -----------------------------------------------------------------------------------------
                                        if stop_checking == False:
                                            # ************ SQUARES STEK ***************
                                            ava_num: set = self.available_numbers(index_row, index_number) - double_bets_in_squares
                                            # ***************************
                                            if tuple(number_append)[0] in ava_num:
                                                ava_num = ava_num & number_append
                                            for number in ava_num:
                                                Count_squares[number] += 1

                                    elif step_level_3 == 1:
                                        if tuple(number_append)[0] in ava_num_in_point:
                                            ava_num_in_point = ava_num_in_point & number_append
                                        for number in ava_num_in_point:
                                            if Count_squares[number] == 1:
                                                self.empty_sudoku[index_row][index_number] = number
                                                count_zero -= 1
                                                # print(*self.empty_sudoku, sep='\n')
                                                # print(f'row - {index_row}')
                                                # print(f'colum - {index_number}')
                                                # print(f'Count_squares==1 - {number}')
                    start_colum += 3
                    end_colum += 3
                start_row += 3
                end_row += 3
            stop_iter += 1

        return self.empty_sudoku

if __name__ == '__main__':
    # S = Solving_sudoku([0,5,4], [0, 6, 5], [0, 7, 3], [0, 8, 1], [1, 0, 8], [1, 1, 3], [1, 2, 1], [1, 5, 7], [1, 6, 6], [1, 8, 9], [2, 0, 5], [2, 1, 4], [2, 2, 9], [2, 6, 8], [2, 8, 7], [3, 1, 2], [3, 3, 5], [3, 5, 1], [3, 7, 7], [4, 0, 4], [4, 1, 1], [4, 6, 9], [4, 7, 6], [5, 1, 6], [5, 2, 3], [5, 4, 2], [6, 4, 3], [6, 6, 4], [6, 7, 9], [6, 8, 6], [7, 1, 9], [7, 3, 7], [7, 4, 4], [7, 7, 1], [8, 0, 2], [8, 1, 8], [8, 5, 6], [8, 6, 7])
    # S= Solving_sudoku([0,3,8], [0, 8, 9], [1, 3, 2], [1, 4, 7], [1, 5, 3], [2, 3, 5], [2, 6, 1], [2, 8, 8], [3, 1, 8], [3, 4, 4], [4, 2, 5], [4, 5, 7], [5, 2, 1], [5, 7, 4], [5, 8, 6], [6, 6, 3], [7, 0, 2], [7, 1, 3], [7, 7, 8], [8, 0, 7], [8, 4, 5], [8, 6, 2])
    # S=Solving_sudoku([1,0,3], [1, 1, 5], [1, 2, 1], [1, 3, 6], [1, 6, 9], [0, 8, 3], [2, 0, 4], [2, 2, 9], [2, 8, 7], [3, 1, 7], [3, 6, 1], [3, 7, 9], [4, 0, 9], [4, 1, 4], [4, 2, 6], [4, 4, 5], [4, 6, 8], [5, 0, 1], [5, 3, 3], [5, 8, 5], [6, 3, 4], [6, 4, 1], [6, 5, 5], [7, 2, 5], [7, 5, 3], [8, 5, 8], [8, 7, 6], [8, 8, 1])
    S=Solving_sudoku([0,1,1], [0,2,6], [0,3,7], [0,5,5], [0,6,3], [1,0,4], [1,4,6], [2,0,2], [2,8,1], [3,0,6], [4,5,3], [4,7,8], [5,1,9], [5,2,7], [5,4,5], [5,8,4], [6,1,2], [7,3,9], [7,6,4], [8,1,5], [8,2,1], [8,4,7], [8,8,9])
    # S=Solving_sudoku([0,2,1],[0,4,4], [0,6,6], [1,2,9],[1,7,3],[2,2,7],[2,5,6],[2,6,5],[2,8,9],[3,0,4],[3,4,2],[3,7,5],[3,8,7],[4,0,2],[4,7,9],[5,0,7],[5,1,5],[5,2,3],[5,5,1],[5,7,8],[6,5,3],[6,7,1],[6,8,5],[7,3,2],[7,6,7],[7,8,3],[8,3,6],[8,5,5])
    # S = Solving_sudoku([0,2,3],[0,4,1],[0,5,9],[0,8,7],[1,0,1],[1,1,2],[1,3,7],[1,5,4],[1,8,5],[2,7,3],[3,4,6],[3,5,8],[3,6,7],[3,7,2],[4,1,7],[5,0,2],[5,3,1],[5,4,9],[6,2,4],[6,5,6],[6,6,1],[6,7,7],[7,6,9],[8,0,8],[8,3,4],[8,4,7],[8,5,3],[8,7,5])
    # S = Solving_sudoku([0,0,8], [0,1,9],[0,4,7],[0,5,5],[0,7,4],[1,3,9],[2,1,3],[2,8,6],[3,3,2],[3,7,1],[4,1,8],[4,4,1],[4,5,9],[4,6,3],[5,0,9],[5,3,4],[6,4,2],[7,0,5],[7,4,8],[7,5,1],[7,7,7],[8,2,7],[8,6,4])
    # S= Solving_sudoku([0,2,1],[0,3,9],[0,6,6],[1,1,4],[1,2,9],[1,6,8],[2,5,3],[2,6,5],[2,7,4],[3,0,1],[3,3,4],[3,5,9],[3,8,3],[4,0,3],[4,7,2],[5,0,9],[5,1,6],[5,2,2],[5,3,3],[5,4,7],[5,8,5],[6,2,6],[7,0,7],[7,3,1],[7,5,6],[7,6,2],[7,7,8],[8,6,3])
    print(*S.completing_sudoku(), sep='\n')
    print('---------------------------')
    print(*S.sudoku_solution(), sep='\n')
    R = Validate_sudoku(S.empty_sudoku)
    print(R.is_valid())
