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
        start_column, end_column = 0, 0
        start_row, end_row = 0, 0

        def __init__(self, row_index: int, column_index: int):
            self.row_index = row_index
            self.column_index = column_index
            self.definition(self.row_index, self.column_index)

        def definition(self, row_index: int, column_index: int):
            if column_index < 3:
                self.start_colum, self.end_column = 0, 3
            elif column_index >= 3 and column_index < 6:
                self.start_column, self.end_column = 3, 6
            elif column_index >= 6:
                self.start_column, self.end_column = 6, 9

            if row_index < 3:
                self.start_row, self.end_row = 0, 3
            elif row_index >= 3 and row_index < 6:
                self.start_row, self.end_row = 3, 6
            elif row_index >= 6:
                self.start_row, self.end_row = 6, 9


    def finding_available_numbers_in_point(self, index_row: int, index_column: int) -> set:
        ''' function for checking columns, rows and individual squares '''
        full_set_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        possible_numbers = set()

        for row_num in self.empty_sudoku[index_row]:
            if row_num != 0:
                possible_numbers.add(row_num)

        for column_num in self.empty_sudoku:
            if column_num[index_column] != 0:
                possible_numbers.add(column_num[index_column])

        definition = self.square_definition_interface(index_row, index_column)
        for index in range(definition.start_row, definition.end_row):
            for number in self.empty_sudoku[index][definition.start_column: definition.end_column]:
                if number != 0:
                    possible_numbers.add(number)
        return full_set_numbers - possible_numbers
# ----------------------------------------------------------------------------------------------------------------------

# -------------------------------- COUNT AVAILABLE NUMBER --------------------------------------------------------------

    def count_ava_num_in_row(self, index_row: int) -> dict:
        ''' function to count the available numbers in a row '''
        count_number_in_row = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for index_column in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)

                numbers_meet_twice_at_two_points_in_squares: set = self.finding_numbers_meet_twice_at_two_points_in_squares(index_row, index_column)
                if list(numbers_meet_twice_at_two_points_in_squares)[0] in ava_num_in_point:
                    ava_num_in_point = ava_num_in_point & numbers_meet_twice_at_two_points_in_squares

                numbers_meet_twice_at_two_points_in_row = self.finding_numbers_meet_twice_at_two_points_in_row(index_row)
                ls_nm_row = list(numbers_meet_twice_at_two_points_in_row)
                if len(ls_nm_row) != 0:
                    if ls_nm_row[0] in ava_num_in_point and ls_nm_row[1] in ava_num_in_point:
                        ava_num_in_point = ava_num_in_point & numbers_meet_twice_at_two_points_in_row

                coordinates_numbers_meet_twice_given_squares_in_column: dict = self.finding_coordinates_numbers_meet_twice_given_squares_in_column(index_column)
                if len(coordinates_numbers_meet_twice_given_squares_in_column) != 0:
                    for n_c in ava_num_in_point:
                        if n_c in coordinates_numbers_meet_twice_given_squares_in_column:
                            if [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_column[n_c][0] and \
                                    [index_row,index_column] != coordinates_numbers_meet_twice_given_squares_in_column[n_c][1]:
                                ava_num_in_point = ava_num_in_point - {n_c}

                numbers_meet_twice_in_row_and_column_for_squares = self.finding_numbers_meet_twice_in_row_and_column_for_squares(index_row, index_column)
                if len(numbers_meet_twice_in_row_and_column_for_squares) != 0:
                    for number in ava_num_in_point:
                        if number in numbers_meet_twice_in_row_and_column_for_squares:
                            if [index_row, index_column] != numbers_meet_twice_in_row_and_column_for_squares[number][0] and \
                                    [index_row, index_column] != numbers_meet_twice_in_row_and_column_for_squares[number][1]:
                                ava_num_in_point = ava_num_in_point - {number}

                for number in ava_num_in_point:
                    count_number_in_row[number] += 1
        return count_number_in_row


    def count_ava_num_in_column(self, index_column: int) -> dict:
        ''' function to count the available numbers in a colum '''
        count_number_in_column = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for index_row in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)

                numbers_meet_twice_at_two_points_in_squares: set = self.finding_numbers_meet_twice_at_two_points_in_squares(index_row, index_column)
                if list(numbers_meet_twice_at_two_points_in_squares)[0] in ava_num_in_point:
                    ava_num_in_point = ava_num_in_point & numbers_meet_twice_at_two_points_in_squares

                numbers_meet_twice_at_two_points_in_column = self.finding_numbers_meet_twice_at_two_points_in_column(index_column)
                ls_nm_co = list(numbers_meet_twice_at_two_points_in_column)
                if len(ls_nm_co) != 0:
                    if ls_nm_co[0] in ava_num_in_point and ls_nm_co[1] in ava_num_in_point:
                        ava_num_in_point = ava_num_in_point & numbers_meet_twice_at_two_points_in_column

                coordinates_numbers_meet_twice_given_squares_in_row: dict = self.finding_coordinates_numbers_meet_twice_given_squares_in_row(index_row)
                if len(coordinates_numbers_meet_twice_given_squares_in_row) != 0:
                    for a_r in ava_num_in_point:
                        if a_r in coordinates_numbers_meet_twice_given_squares_in_row:
                            if [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_row[a_r][0] and \
                                    [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_row[a_r][1]:
                                ava_num_in_point = ava_num_in_point - {a_r}

                numbers_meet_twice_in_row_and_column_for_squares = self.finding_numbers_meet_twice_in_row_and_column_for_squares(index_row, index_column)
                if len(numbers_meet_twice_in_row_and_column_for_squares) != 0:
                    for number in ava_num_in_point:
                        if number in numbers_meet_twice_in_row_and_column_for_squares:
                            if [index_row, index_column] != numbers_meet_twice_in_row_and_column_for_squares[number][0] and \
                                    [index_row, index_column] != numbers_meet_twice_in_row_and_column_for_squares[number][1]:
                                ava_num_in_point = ava_num_in_point - {number}

                for number in ava_num_in_point:
                    count_number_in_column[number] += 1
        return count_number_in_column
# ----------------------------------------------------------------------------------------------------------------------

# -------------------------------- FINDING DOUBLE PAIRS ----------------------------------------------------------------

    def finding_double_pairs_in_squares(self, row_index: int, column_index: int) -> set:
        ''' function for finding duplicate pairs in a square '''
        definition = self.square_definition_interface(row_index, column_index)
        count_zero = 0
        duplicate_pairs = []
        for index_row in range(definition.start_row, definition.end_row):
            for index_column in range(definition.start_column, definition.end_column):
                if self.empty_sudoku[index_row][index_column] == 0:
                    count_zero += 1
                    ava_num = self.finding_available_numbers_in_point(index_row, index_column)
                    if len(ava_num) == 2:
                        duplicate_pairs.append(tuple(ava_num))

        for pair in duplicate_pairs:
            if duplicate_pairs.count(pair) == 2 and count_zero != 2:
                return set(pair)
        return set()


    def finding_double_pairs_in_row(self, index_row: int) -> set:
        ''' function for finding duplicate pairs in a row '''
        duplicate_pairs = []
        for index_column in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point = self.finding_available_numbers_in_point(index_row, index_column)
                double_pairs_in_squares = self.finding_double_pairs_in_squares(index_row, index_column)
                ava_num = ava_num_in_point - double_pairs_in_squares
                if len(ava_num) == 2:
                    duplicate_pairs.append(tuple(ava_num))
                elif len(ava_num) == 0:
                    duplicate_pairs.append(tuple(ava_num_in_point))

        for pair in duplicate_pairs:
            if duplicate_pairs.count(pair) == 2:
                return set(pair)
        return set()


    def finding_double_pairs_in_column(self, index_column: int) -> set:
        ''' function for finding duplicate pairs in a column '''
        duplicate_pairs = []
        for index_row in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point = self.finding_available_numbers_in_point(index_row, index_column)
                doub_num_in_squar = self.finding_double_pairs_in_squares(index_row, index_column)
                ava_num = ava_num_in_point - doub_num_in_squar
                if len(ava_num) == 2:
                    duplicate_pairs.append(tuple(ava_num))
                elif len(ava_num) == 0:
                    duplicate_pairs.append(tuple(ava_num_in_point))

        for pair in duplicate_pairs:
            if duplicate_pairs.count(pair) == 2:
                return set(pair)
        return set()
# ----------------------------------------------------------------------------------------------------------------------

# ------------------------------- FINDING NUMBERS MEET TWICE AT TWO POINT ----------------------------------------------

    def finding_numbers_meet_twice_at_two_points_in_squares(self, row_index: int, column_index: int):
        ''' the function finds numbers that occur twice in two points in a square '''
        definition = self.square_definition_interface(row_index, column_index)
        Count_squares = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for index_row in range(definition.start_row, definition.end_row):
            for index_column in range(definition.start_column, definition.end_column):
                if self.empty_sudoku[index_row][index_column] == 0:
                    ava_num = self.finding_available_numbers_in_point(index_row, index_column)
                    if len(ava_num) != 1:
                        for number in ava_num:
                            Count_squares[number] += 1
                    else:
                        Count_squares[list(ava_num)[0]] += 10
        double_pairs = []
        for index_row in range(definition.start_row, definition.end_row):
            for index_column in range(definition.start_column, definition.end_column):
                if self.empty_sudoku[index_row][index_column] == 0:
                    number_meet_twice = []
                    ava_num_in_point = self.finding_available_numbers_in_point(index_row, index_column)
                    double_pairs_squares = self.finding_double_pairs_in_squares(index_row, index_column)
                    for number in ava_num_in_point:
                        if Count_squares[number] == 2:
                            number_meet_twice.append(number)

                    if len(number_meet_twice) > 1 and set(number_meet_twice) != double_pairs_squares:
                        double_pairs.append(set(number_meet_twice))
                    elif len(number_meet_twice) == 1:
                        Count_squares[number_meet_twice[0]] += 10
                        if len(double_pairs) != 0:
                            if number_meet_twice[0] in double_pairs[0]:
                                double_pairs[0] -= set(number_meet_twice)
        if len(double_pairs) == 2 and double_pairs[0] == double_pairs[1]:
            return double_pairs[0]
        else:
            return {0}


    def finding_numbers_meet_twice_at_two_points_in_column(self, index_column: int) -> set:
        ''' the function finds numbers that occur twice in column '''
        ava_colum_num = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for index_row in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)

                numbers_meet_twice_at_two_points_in_squares: set = self.finding_numbers_meet_twice_at_two_points_in_squares(index_row, index_column)
                list_number_appented_twice_in_square = list(numbers_meet_twice_at_two_points_in_squares)
                if list_number_appented_twice_in_square[0] in ava_num_in_point and \
                        list_number_appented_twice_in_square[1] in ava_num_in_point:
                    ava_num_in_point = ava_num_in_point & numbers_meet_twice_at_two_points_in_squares

                double_pairs_in_row = self.finding_double_pairs_in_row(index_row)
                ls_double_pairs_in_row = list(double_pairs_in_row)
                if len(ls_double_pairs_in_row) != 0 and len(ava_num_in_point) != 1:
                    if ls_double_pairs_in_row[0] in ava_num_in_point and ls_double_pairs_in_row[
                        1] in ava_num_in_point and len(ava_num_in_point) == 2:
                        ava_num_in_point = ava_num_in_point & double_pairs_in_row
                    elif ls_double_pairs_in_row[0] in ava_num_in_point or ls_double_pairs_in_row[1] in ava_num_in_point:
                        ava_num_in_point = ava_num_in_point - double_pairs_in_row

                for number in ava_num_in_point:
                    ava_colum_num[number] += 1

        double_pairs = []
        for index_row in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                number_meet_twice = []
                ava_num_in_point = self.finding_available_numbers_in_point(index_row, index_column)

                double_bets_in_column = self.finding_double_pairs_in_column(index_column)
                ava_num = ava_num_in_point - double_bets_in_column

                double = self.finding_double_pairs_in_row(index_row)
                ls_double_pairs = list(double)
                if len(ls_double_pairs) != 0 and len(ava_num) != 1:
                    if ls_double_pairs[0] in ava_num and ls_double_pairs[1] in ava_num and len(ava_num) == 2:
                        ava_num = ava_num & double
                    elif ls_double_pairs[0] in ava_num or ls_double_pairs[1] in ava_num:
                        ava_num = ava_num - double

                for num in ava_num:
                    if ava_colum_num[num] == 2:
                        number_meet_twice.append(num)
                    elif ava_colum_num[num] == 1:
                        number_meet_twice = []
                if len(number_meet_twice) >= 2 and set(number_meet_twice) != double_bets_in_column:
                    double_pairs.append(set(number_meet_twice))
                elif len(number_meet_twice) == 1:
                    ava_colum_num[number_meet_twice[0]] += 10
        if len(double_pairs) == 2 and double_pairs[0] == double_pairs[1]:
            return double_pairs[0]
        else:
            return set()


    def finding_numbers_meet_twice_at_two_points_in_row(self, index_row: int) -> set:
        ''' the function finds numbers that occur twice in row '''
        ava_row_num = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for index_column in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)

                numbers_meet_twice_at_two_points_in_squares: set = self.finding_numbers_meet_twice_at_two_points_in_squares(index_row, index_column)
                list_number_appented_twice_in_square = list(numbers_meet_twice_at_two_points_in_squares)
                if list_number_appented_twice_in_square[0] in ava_num_in_point and \
                        list_number_appented_twice_in_square[1] in ava_num_in_point:
                    ava_num_in_point = ava_num_in_point & numbers_meet_twice_at_two_points_in_squares

                double_pairs_in_column = self.finding_double_pairs_in_column(index_column)
                ls_double_pairs_in_column = list(double_pairs_in_column)
                if len(ls_double_pairs_in_column) != 0 and len(ava_num_in_point) != 1:
                    if ls_double_pairs_in_column[0] in ava_num_in_point and ls_double_pairs_in_column[1] in ava_num_in_point and len(ava_num_in_point) == 2:
                        ava_num_in_point = ava_num_in_point & double_pairs_in_column
                    elif ls_double_pairs_in_column[0] in ava_num_in_point or ls_double_pairs_in_column[1] in ava_num_in_point:
                        ava_num_in_point = ava_num_in_point - double_pairs_in_column

                for number in ava_num_in_point:
                    ava_row_num[number] += 1
        double_pairs = []
        for index_column in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                number_meet_twice = []
                ava_num = self.finding_available_numbers_in_point(index_row, index_column)

                double_bets_in_row = self.finding_double_pairs_in_row(index_row)
                ava_num = ava_num - double_bets_in_row

                double = self.finding_double_pairs_in_column(index_column)
                ls_double_pairs = list(double)
                if len(ls_double_pairs) != 0 and len(ava_num) != 1:
                    if ls_double_pairs[0] in ava_num and ls_double_pairs[1] in ava_num and len(ava_num) == 2:
                        ava_num = ava_num & double
                    elif ls_double_pairs[0] in ava_num or ls_double_pairs[1] in ava_num:
                        ava_num = ava_num - double

                for num in ava_num:
                    if ava_row_num[num] == 2:
                        number_meet_twice.append(num)
                if len(number_meet_twice) >= 2 and set(number_meet_twice) != double_bets_in_row:
                    double_pairs.append(set(number_meet_twice))
                elif len(number_meet_twice) == 1:
                    ava_row_num[number_meet_twice[0]] += 10
        if len(double_pairs) == 2 and list(double_pairs[0])[0] in double_pairs[1] and list(double_pairs[0])[1] in double_pairs[1]:
            double_pairs[0] = double_pairs[0] & double_pairs[1]
            return double_pairs[0]
        else:
            return set()
# ----------------------------------------------------------------------------------------------------------------------

# ------------------------------- FINDING NUMBER MEET TWICE GIVEN SQUARES ----------------------------------------------

    def finding_coordinates_numbers_meet_twice_in_line_for_square(self, row_index: int, colum_index: int):
        ''' the function finds a number that appears twice in one line in a given square '''
        definition = self.square_definition_interface(row_index, colum_index)
        Count_squares = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for index_row in range(definition.start_row, definition.end_row):
            for index_column in range(definition.start_column, definition.end_column):
                if self.empty_sudoku[index_row][index_column] == 0:
                    ava_num = self.finding_available_numbers_in_point(index_row, index_column)
                    for number in ava_num:
                        Count_squares[number] += 1
        number_and_cord = {}
        for index_row in range(definition.start_row, definition.end_row):
            for index_column in range(definition.start_column, definition.end_column):
                if self.empty_sudoku[index_row][index_column] == 0:
                    available_numbers_in_point = self.finding_available_numbers_in_point(index_row, index_column)
                    double_pairs_in_squares = self.finding_double_pairs_in_squares(index_row, index_column)
                    numbers_meet_twice_at_two_points_in_squares = self.finding_numbers_meet_twice_at_two_points_in_squares(index_row, index_column)
                    for num in available_numbers_in_point:
                        if Count_squares[num] == 2 and available_numbers_in_point != double_pairs_in_squares and \
                                                        available_numbers_in_point != numbers_meet_twice_at_two_points_in_squares:
                            if num not in number_and_cord:
                                number_and_cord[num] = []
                                number_and_cord[num] += [[index_row, index_column]]
                            else:
                                number_and_cord[num] += [[index_row, index_column]]
        result = {}
        for nm in number_and_cord:
            if len(number_and_cord[nm]) == 2:
                for i in number_and_cord[nm]:
                    if number_and_cord[nm][0][0] == number_and_cord[nm][1][0] or number_and_cord[nm][0][1] == number_and_cord[nm][1][1]:
                        if nm not in result:
                            result[nm] = []
                            result[nm] += [i]
                        else:
                            result[nm] += [i]
        return result


    def finding_coordinates_numbers_meet_twice_given_squares_in_column(self, index_column: int) -> dict:
        ''' the function finds a number that appears twice in a column in a given square '''
        number_and_cord = {}
        for index_row in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)
                coordinates_numbers_meet_twice_in_line_for_square: dict = self.finding_coordinates_numbers_meet_twice_in_line_for_square(index_row, index_column)
                for number in ava_num_in_point:
                    if number in coordinates_numbers_meet_twice_in_line_for_square:
                        if coordinates_numbers_meet_twice_in_line_for_square[number][0][1] == coordinates_numbers_meet_twice_in_line_for_square[number][1][1]:
                            if number not in number_and_cord:
                                number_and_cord[number] = []
                                number_and_cord[number] += [[index_row, index_column]]
                            else:
                                number_and_cord[number] += [[index_row, index_column]]
        return number_and_cord


    def finding_coordinates_numbers_meet_twice_given_squares_in_row(self, index_row: int) -> dict:
        ''' the function finds a number that appears twice in a row in a given square '''
        number_and_cord = {}
        for index_column in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)
                coordinates_numbers_meet_twice_in_line_for_square: dict = self.finding_coordinates_numbers_meet_twice_in_line_for_square(index_row, index_column)
                for number in ava_num_in_point:
                    if number in coordinates_numbers_meet_twice_in_line_for_square:
                        if coordinates_numbers_meet_twice_in_line_for_square[number][0][0] == coordinates_numbers_meet_twice_in_line_for_square[number][1][0]:
                            if number not in number_and_cord:
                                number_and_cord[number] = []
                                number_and_cord[number] += [[index_row, index_column]]
                            else:
                                number_and_cord[number] += [[index_row, index_column]]
        return number_and_cord
# ----------------------------------------------------------------------------------------------------------------------

# ------------------------------- FINDING NUMBER MEET TWICE ------------------------------------------------------------
    def finding_numbers_meet_twice_in_row_and_column_for_squares(self, row_index: int, column_index: int):
        ''' the function finds numbers that appear twice in a row and column for a given square '''
        definition = self.square_definition_interface(row_index, column_index)
        coord_number = dict()
        for index_row in range(definition.start_row, definition.end_row):
            for index_column in range(definition.start_column, definition.end_column):
                if self.empty_sudoku[index_row][index_column] == 0:

                    finding_coordinates_numbers_meet_twice_in_column = self.finding_coordinates_numbers_meet_twice_in_column(index_column)
                    if len(finding_coordinates_numbers_meet_twice_in_column) != 0:
                        for num_col , coord_col in finding_coordinates_numbers_meet_twice_in_column.items():
                            if coord_col[0][0] >= definition.start_row and coord_col[0][0] < definition.end_row:
                                if coord_col[0][1] >= definition.start_column and coord_col[0][1] < definition.end_column:
                                    if coord_col[1][0] >= definition.start_row and coord_col[1][0] < definition.end_row:
                                        if coord_col[1][1] >= definition.start_column and coord_col[1][1] < definition.end_column:
                                            coord_number[num_col] = coord_col

                    finding_coordinates_numbers_meet_twice_in_row = self.finding_coordinates_numbers_meet_twice_in_row(index_row)
                    if len(finding_coordinates_numbers_meet_twice_in_row) != 0:
                        for num_row , coord_row in finding_coordinates_numbers_meet_twice_in_row.items():
                            if coord_row[0][0] >= definition.start_row and coord_row[0][0] < definition.end_row:
                                if coord_row[0][1] >= definition.start_column and coord_row[0][1] < definition.end_column:
                                    if coord_row[1][0] >= definition.start_row and coord_row[1][0] < definition.end_row:
                                        if coord_row[1][1] >= definition.start_column and coord_row[1][1] < definition.end_column:
                                            coord_number[num_row] = coord_row
        return coord_number


    def finding_coordinates_numbers_meet_twice_in_column(self, index_column: int) -> dict:
        ''' the function finds coordinates numbers that appear twice in a column '''
        ava_colum_num = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for index_row in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)
                for number in ava_num_in_point:
                    ava_colum_num[number] += 1
        coordinates_number = {}
        for index_row in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)
                for num in ava_num_in_point:
                    if ava_colum_num[num] == 2:
                        if num not in coordinates_number:
                            coordinates_number[num] = []
                            coordinates_number[num] += [[index_row, index_column]]
                        else:
                            coordinates_number[num] += [[index_row, index_column]]
        return coordinates_number


    def finding_coordinates_numbers_meet_twice_in_row(self, index_row: int):
        ''' the function finds coordinates numbers that appear twice in a row '''
        count_ava_num_in_row = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for index_column in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)
                for number in ava_num_in_point:
                    count_ava_num_in_row[number] += 1
        coordinates_number = {}
        for index_column in range(9):
            if self.empty_sudoku[index_row][index_column] == 0:
                ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)
                for num in ava_num_in_point:
                    if count_ava_num_in_row[num] == 2:
                        if num not in coordinates_number:
                            coordinates_number[num] = []
                            coordinates_number[num] += [[index_row, index_column]]
                        else:
                            coordinates_number[num] += [[index_row, index_column]]
        return coordinates_number
# ----------------------------------------------------------------------------------------------------------------------

# ------------------------------- FINDING THREE NUMBER -----------------------------------------------------------------
    def finding_three_numbers_in_line_on_squares(self, row_index: int, column_index: int):
        definition = self.square_definition_interface(row_index, column_index)
        coordinates_number = []
        total_number = set()
        for index_row in range(definition.start_row, definition.end_row):
            for index_column in range(definition.start_column, definition.end_column):
                if self.empty_sudoku[index_row][index_column] == 0:
                    ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)
                    total_number = total_number.union(ava_num_in_point)
                    coordinates_number.append([index_row, index_column])

        if len(coordinates_number) == 3:
            if coordinates_number[0][0] ==  coordinates_number[1][0] == coordinates_number[2][0]:
                return [coordinates_number[0][0], 10], total_number
            elif coordinates_number[0][1] ==  coordinates_number[1][1] == coordinates_number[2][1]:
                return [10, coordinates_number[0][1]], total_number
            else:
                return []
        return []


    def finding_three_numbers_in_column_on_squares(self, index_column: int) -> set:
        for index_row in range(0,9,3):
            for coefficient in range(3):
                if self.empty_sudoku[index_row + coefficient][index_column] == 0:
                    three_numbers_in_line_on_squares = self.finding_three_numbers_in_line_on_squares(index_row + coefficient, index_column)
                    if len(three_numbers_in_line_on_squares) != 0:
                        if index_column == three_numbers_in_line_on_squares[0][1]:
                            return three_numbers_in_line_on_squares[1]
                    break
        return set()


    def finding_three_numbers_in_row_on_squares(self, index_row: int) -> set:
        for index_column in range(0,9,3):
            for coefficient in range(3):
                if self.empty_sudoku[index_row][index_column + coefficient] == 0:
                    three_numbers_in_line_on_squares = self.finding_three_numbers_in_line_on_squares(index_row, index_column + coefficient)
                    if len(three_numbers_in_line_on_squares) != 0:
                        if index_row == three_numbers_in_line_on_squares[0][0]:
                            return three_numbers_in_line_on_squares[1]
                    break
        return set()
# ----------------------------------------------------------------------------------------------------------------------


    def sudoku_solution(self) -> list:
        ''' function for solving sudoku (completes the sudoku puzzle only once) '''
        count_zero = 81 - len(self.cord_num)
        while count_zero > 0:
            number_done = 0
            start_row , end_row = 0 , 3
            # start_row, end_row = 6,9
            for step_level_1 in range(3):
                start_column , end_column = 0 , 3
                # start_column, end_column = 3,6
                for step_level_2 in range(3):
                    Count_squares = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
                    numbers_meet_twice_in_row_and_column_for_squares = self.finding_numbers_meet_twice_in_row_and_column_for_squares(start_row, start_column)
                    three_numbers_in_line_on_squares = self.finding_three_numbers_in_line_on_squares(start_row, start_column)
                    for step_level_3 in range(2):

                        for index_row in range(start_row, end_row):
                            for index_column in range(start_column, end_column):
                                if self.empty_sudoku[index_row][index_column] == 0:
                                    # -------------------------------------------------------------------------------------
                                    ava_num_in_point: set = self.finding_available_numbers_in_point(index_row, index_column)
                                    # -------------------------------------------------------------------------------------
                                    double_pairs_in_row: set = self.finding_double_pairs_in_row(index_row)
                                    double_pairs_in_column: set = self.finding_double_pairs_in_column(index_column)
                                    double_pairs_in_squares: set = self.finding_double_pairs_in_squares(index_row, index_column)
                                    numbers_meet_twice_at_two_points_in_squares: set = self.finding_numbers_meet_twice_at_two_points_in_squares(index_row, index_column)
                                    coordinates_numbers_meet_twice_given_squares_in_row: dict = self.finding_coordinates_numbers_meet_twice_given_squares_in_row(index_row)
                                    coordinates_numbers_meet_twice_given_squares_in_column: dict = self.finding_coordinates_numbers_meet_twice_given_squares_in_column(index_column)

                                    if len(three_numbers_in_line_on_squares) == 0:
                                        three_numbers_in_row_on_squares = self.finding_three_numbers_in_row_on_squares(index_row)
                                        if len(three_numbers_in_row_on_squares) != 0:
                                            ava_num_in_point = ava_num_in_point - three_numbers_in_row_on_squares

                                        three_numbers_in_column_on_squares = self.finding_three_numbers_in_column_on_squares(index_column)
                                        if len(three_numbers_in_column_on_squares) != 0:
                                            ava_num_in_point = ava_num_in_point - three_numbers_in_column_on_squares

                                    ls_double_pairs_in_squares = list(double_pairs_in_squares)
                                    if len(ls_double_pairs_in_squares) != 0 and len(ava_num_in_point) != 1:
                                        if ls_double_pairs_in_squares[0] in ava_num_in_point and ls_double_pairs_in_squares[1] in ava_num_in_point and len(ava_num_in_point) == 2:
                                            ava_num_in_point = ava_num_in_point & double_pairs_in_squares
                                        elif ls_double_pairs_in_squares[0] in ava_num_in_point or ls_double_pairs_in_squares[1] in ava_num_in_point:
                                            ava_num_in_point = ava_num_in_point - double_pairs_in_squares

                                    ls_double_pairs_in_row = list(double_pairs_in_row)
                                    if len(ls_double_pairs_in_row) != 0 and len(ava_num_in_point) != 1:
                                        if ls_double_pairs_in_row[0] in ava_num_in_point and ls_double_pairs_in_row[1] in ava_num_in_point and len(ava_num_in_point) == 2:
                                            ava_num_in_point = ava_num_in_point & double_pairs_in_row
                                        elif ls_double_pairs_in_row[0] in ava_num_in_point or ls_double_pairs_in_row[1] in ava_num_in_point:
                                            ava_num_in_point = ava_num_in_point - double_pairs_in_row

                                    ls_double_pairs_in_column = list(double_pairs_in_column)
                                    if len(ls_double_pairs_in_column) != 0 and len(ava_num_in_point) != 1:
                                        if ls_double_pairs_in_column[0] in ava_num_in_point and ls_double_pairs_in_column[1] in ava_num_in_point and len(ava_num_in_point) == 2:
                                            ava_num_in_point = ava_num_in_point & double_pairs_in_column
                                        elif ls_double_pairs_in_column[0] in ava_num_in_point or ls_double_pairs_in_column[1] in ava_num_in_point:
                                            ava_num_in_point = ava_num_in_point - double_pairs_in_column

                                    if tuple(numbers_meet_twice_at_two_points_in_squares)[0] in ava_num_in_point:
                                        ava_num_in_point = ava_num_in_point & numbers_meet_twice_at_two_points_in_squares

                                    if len(coordinates_numbers_meet_twice_given_squares_in_column) != 0:
                                        for n_c in ava_num_in_point:
                                            if n_c in coordinates_numbers_meet_twice_given_squares_in_column:
                                                if [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_column[n_c][0] and \
                                                        [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_column[n_c][1]:
                                                    ava_num_in_point = ava_num_in_point - {n_c}

                                    if len(coordinates_numbers_meet_twice_given_squares_in_row) != 0:
                                        for n_r in ava_num_in_point:
                                            if n_r in coordinates_numbers_meet_twice_given_squares_in_row:
                                                if [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_row[n_r][0] and \
                                                        [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_row[n_r][1]:
                                                    ava_num_in_point = ava_num_in_point - {n_r}

                                    if len(numbers_meet_twice_in_row_and_column_for_squares) != 0:
                                        for number in ava_num_in_point:
                                            if number in numbers_meet_twice_in_row_and_column_for_squares:
                                                if [index_row, index_column] != numbers_meet_twice_in_row_and_column_for_squares[number][0] and \
                                                        [index_row, index_column] != numbers_meet_twice_in_row_and_column_for_squares[number][1]:
                                                    ava_num_in_point = ava_num_in_point - {number}


                                    if step_level_3 == 0:
                                        stop_checking = False

                                        if len(ava_num_in_point) == 1:
                                            # ************ POINT STEK ***************
                                            self.empty_sudoku[index_row][index_column] = list(ava_num_in_point)[0]
                                            count_zero -= 1
                                            stop_checking = True
                                            number_done += 1
                                            # print(*self.empty_sudoku, sep='\n')
                                            # print(f'row - {index_row}')
                                            # print(f'colum - {index_column}')
                                            # print(f'ava_num_in_point==1 - {list(ava_num_in_point)[0]}')
                                        # # -----------------------------------------------------------------------------------------
                                        if stop_checking == False:
                                            # ************ ROW STEK ***************
                                            count_row_num: dict = self.count_ava_num_in_row(index_row)
                                            point_in_row: set = self.finding_available_numbers_in_point(index_row, index_column)
                                            # ***************************

                                            if tuple(numbers_meet_twice_at_two_points_in_squares)[0] in point_in_row:
                                                point_in_row = point_in_row & numbers_meet_twice_at_two_points_in_squares

                                            numbers_meet_twice_at_two_points_in_row: set = self.finding_numbers_meet_twice_at_two_points_in_row(index_row)
                                            ls_nm_row = list(numbers_meet_twice_at_two_points_in_row)
                                            if len(ls_nm_row) != 0:
                                                if ls_nm_row[0] in point_in_row and ls_nm_row[1] in point_in_row:
                                                    point_in_row = point_in_row & numbers_meet_twice_at_two_points_in_row

                                            if len(coordinates_numbers_meet_twice_given_squares_in_column) != 0:
                                                for n_c in point_in_row:
                                                    if n_c in coordinates_numbers_meet_twice_given_squares_in_column:
                                                        if [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_column[n_c][0] and \
                                                                [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_column[n_c][1]:
                                                            point_in_row = point_in_row - {n_c}

                                            if len(numbers_meet_twice_in_row_and_column_for_squares) != 0:
                                                for number in point_in_row:
                                                    if number in numbers_meet_twice_in_row_and_column_for_squares:
                                                        if [index_row, index_column] != numbers_meet_twice_in_row_and_column_for_squares[number][0] and \
                                                                [index_row, index_column] != numbers_meet_twice_in_row_and_column_for_squares[number][1]:
                                                            point_in_row = point_in_row - {number}

                                            if len(double_pairs_in_row) == 2:
                                                count_row_num.pop(list(double_pairs_in_row)[0])
                                                count_row_num.pop(list(double_pairs_in_row)[1])

                                            for number_row, count_num_row in count_row_num.items():
                                                if count_num_row == 1 and number_row in point_in_row:
                                                    self.empty_sudoku[index_row][index_column] = number_row
                                                    count_zero -= 1
                                                    stop_checking = True
                                                    number_done += 1
                                                    # print(*self.empty_sudoku, sep='\n')
                                                    # print(f'row - {index_row}')
                                                    # print(f'column - {index_column}')
                                                    # print(f'count_row_num==1 - {number_row}')
                                        #-----------------------------------------------------------------------------------------
                                        if stop_checking == False:
                                            # ************* COLUMN STEK **************
                                            count_column_num: dict = self.count_ava_num_in_column(index_column)
                                            point_in_col: set = self.finding_available_numbers_in_point(index_row, index_column)
                                            # ***************************

                                            if tuple(numbers_meet_twice_at_two_points_in_squares)[0] in point_in_col:
                                                point_in_col = point_in_col & numbers_meet_twice_at_two_points_in_squares

                                            numbers_meet_twice_at_two_points_in_column: set = self.finding_numbers_meet_twice_at_two_points_in_column(index_column)
                                            ls_nm_co = list(numbers_meet_twice_at_two_points_in_column)
                                            if len(ls_nm_co) != 0:
                                                if ls_nm_co[0] in point_in_col and ls_nm_co[1] in point_in_col:
                                                    point_in_col = ava_num_in_point & numbers_meet_twice_at_two_points_in_column

                                            if len(coordinates_numbers_meet_twice_given_squares_in_row) != 0:
                                                for a_r in point_in_col:
                                                    if a_r in coordinates_numbers_meet_twice_given_squares_in_row:
                                                        if [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_row[a_r][0] and \
                                                                [index_row, index_column] != coordinates_numbers_meet_twice_given_squares_in_row[a_r][1]:
                                                            point_in_col = point_in_col - {a_r}

                                            if len(numbers_meet_twice_in_row_and_column_for_squares) != 0:
                                                for number in point_in_col:
                                                    if number in numbers_meet_twice_in_row_and_column_for_squares:
                                                        if [index_row, index_column] != numbers_meet_twice_in_row_and_column_for_squares[number][0] and \
                                                                [index_row, index_column] != numbers_meet_twice_in_row_and_column_for_squares[number][1]:
                                                            point_in_col = point_in_col - {number}

                                            if len(double_pairs_in_column) == 2:
                                                count_column_num.pop(list(double_pairs_in_column)[0])
                                                count_column_num.pop(list(double_pairs_in_column)[1])

                                            for number_column, count_num_column in count_column_num.items():
                                                if count_num_column == 1 and number_column in point_in_col:
                                                    self.empty_sudoku[index_row][index_column] = number_column
                                                    count_zero -= 1
                                                    stop_checking = True
                                                    number_done += 1
                                                    # print(*self.empty_sudoku, sep='\n')
                                                    # print(f'row - {index_row}')
                                                    # print(f'colum - {index_column}')
                                                    # print(f'count_colum_num==1 - {number_column}')
                                        # -----------------------------------------------------------------------------------------
                                        if stop_checking == False:
                                            # ************ SQUARES STEK ***************
                                            for num in ava_num_in_point:
                                                Count_squares[num] += 1
                                        #------------------------------------------------------------------------------------------
                                        if stop_checking == True:
                                            recheck_numbers_meet_twice_in_row_and_column = self.finding_numbers_meet_twice_in_row_and_column_for_squares(start_row, start_column)
                                            if len(recheck_numbers_meet_twice_in_row_and_column) >= len(numbers_meet_twice_in_row_and_column_for_squares):
                                                numbers_meet_twice_in_row_and_column_for_squares = recheck_numbers_meet_twice_in_row_and_column

                                            recheck_three_numbers_in_line = self.finding_three_numbers_in_line_on_squares(start_row, start_column)
                                            if len(recheck_three_numbers_in_line) >= len(three_numbers_in_line_on_squares):
                                                three_numbers_in_line_on_squares = recheck_three_numbers_in_line


                                    elif step_level_3 == 1:
                                        for number in ava_num_in_point:
                                            if len(ava_num_in_point) == 2 and \
                                                    Count_squares[list(ava_num_in_point)[0]] == 1 and \
                                                    Count_squares[list(ava_num_in_point)[1]] == 1:
                                                pass
                                            elif Count_squares[number] == 1 and number not in double_pairs_in_squares:
                                                self.empty_sudoku[index_row][index_column] = number
                                                count_zero -= 1
                                                number_done += 1
                                                # print(*self.empty_sudoku, sep='\n')
                                                # print(f'row - {index_row}')
                                                # print(f'column - {index_column}')
                                                # print(f'Count_squares==1 - {number}')

                    start_column += 3
                    end_column += 3
                start_row += 3
                end_row += 3

            if number_done == 0:
                return self.empty_sudoku
        return self.empty_sudoku


if __name__ == '__main__':
    # S = Solving_sudoku([ 0 , 0 , 3 ], [0,7,2],[1,4,1],[1,5,7],[2,3,8],[2,5,9],[3,0,6],[3,4,2],[4,6,9],[4,8,5],[5,6,7],[6,1,7],[6,2,4],[6,6,8],[7,3,6],[7,7,1],[8,1,9])
    # S = Solving_sudoku([ 0 , 2 , 8 ], [0,4,3],[0,5,4],[0,7,6],[1,0,1],[1,4,8],[2,0,7],[2,4,1],[3,2,3],[4,1,2],[4,3,5],[4,6,9],[4,7,1],[5,0,9],[5,8,7],[6,2,6],[6,5,3],[6,6,8],[6,8,1],[7,0,3],[7,7,2],[8,3,9],[8,7,4])
    S = Solving_sudoku([0,0,4], [0,4,5],[0,6,8],[1,1,1],[1,2,8],[1,6,7],[2,2,3],[2,5,4],[3,0,9],[3,1,6],[4,2,5],[4,5,3],[5,1,7],[5,5,8],[5,7,6],[6,2,1],[6,3,6],[6,8,4],[7,3,5],[7,7,1],[7,8,3],[8,3,8])
    print(*S.completing_sudoku(), sep='\n')
    print('---------------------------')
    print(*S.sudoku_solution(), sep='\n')
    R = Validate_sudoku(S.empty_sudoku)
    print(R.is_valid())