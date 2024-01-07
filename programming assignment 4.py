def main():
    # prints general information about the program's functions
    info()
    # opens and read the .txt file and stores it in sudo_data
    with open("x-sudoku.txt", 'r') as file:
        sudo_data = file.read().split()
    # initializing the matrix values
    index = 0
    number = int(sudo_data[index])
    # the -1 at the end of the file indicates its the end
    while (number != -1):
        # formatting the 9x9 matrix with a heading
        print("*" * 8, "Square", str(number), "*" * 8)
        # creating a nested for loop that reads and prints each 9x9 square
        square = [0] * 9
        for i in range(9):
            square[i] = [0] * 9
            for j in range(9):
                index += 1
                number = int(sudo_data[index])
                square[i][j] = number
                print(str(square[i][j]), end=" " * 2)
            print("")
        index += 1
        number = int(sudo_data[index])
        # calling each of the functions
        test_row(square)
        test_col(square)
        test_main_diag(square)
        test_anti_diag(square)
        test_sub_square(square)


# i is row index, j is column index
def test_row(square):
    # ensuring each value in the row satisfies the requirements
    row_status = [True] * 9
    # for loop getting each row of numbers
    for i in range(9):
        row_numbers = [0] * 9
        for j in range(9):
            row_numbers[j] = square[i][j]
        # testing if each number falls between 1-9 and is not repeated
        for number in range(1, 10):
            if number not in row_numbers:
                row_status[i] = False
    # prints statements if the row does or does not satisfy the sudoku requirements
    if False not in row_status:
        print("All rows satisfy the requirements!")
    else:
        for i in range(9):
            if row_status[i] == False:
                print("Row", i + 1, "violates the requirements!")


def test_col(square):
    # ensuring each value in the column satisfies the requirements
    col_status = [True] * 9
    # for loop getting each column of numbers
    for j in range(9):
        col_numbers = [0] * 9
        for i in range(9):
            col_numbers[i] = square[i][j]
        # testing if each number falls between 1-9 and is not repeated
        for number in range(1, 10):
            if number not in col_numbers:
                col_status[j] = False
    # prints statements if the column does or does not satisfy the sudoku requirements
    if False not in col_status:
        print("All columns satisfy the requirements!")
    else:
        for j in range(9):
            if col_status[j] == False:
                print("Column", j + 1, "violates the requirements!")


def test_main_diag(square):
    # ensuring each value in the diagonal satisfies the requirements
    main_diag_status = True
    main_diag_numbers = [0] * 9
    # for loop getting the values of the diagonal row
    for i in range(9):
        main_diag_numbers[i] = square[i][i]
    # testing if each number falls between 1-9 and is not repeated
    for number in range(1, 10):
        if number not in main_diag_numbers:
            main_diag_status = False
    # prints statements if the diagonal does or does not satisfy the sudoku requirements
    if main_diag_status:
        print("Main diagonal satisfies the requirements!")
    else:
        print("Main diagonal violates the requirements!")


def test_anti_diag(square):
    # ensuring each value in the anti-diagonal satisfies the requirements
    anti_diag_status = True
    anti_diag_numbers = [0] * 9
    # for loop getting the values of the anti-diagonal row, 8-i because it starts at the top right going to the
    # bottom left
    for i in range(9):
        anti_diag_numbers[i] = square[i][8-i]
    # testing if each number falls between 1-9 and is not repeated
    for number in range(1, 10):
        if number not in anti_diag_numbers:
            anti_diag_status = False
    # prints statements if the anti-diagonal does or does not satisfy the sudoku requirements
    if anti_diag_status:
        print("Anti diagonal satisfies the requirements!")
    else:
        print("Anti diagonal violates the requirements!")


def test_sub_square(square):
    # ensuring each value in the subsquare satisfies the requirements
    sub_square_numbers = [0] * 9
    # this nested for loop creates 9 separate 3x3 subsquares within the 9x9 squares
    for i in range(3):
        for j in range(3):
            sub_square_status = True
            k_limit = (i+1)*3
            m = 0
            for k in range(i * 3, k_limit):
                l_limit = (j+1)*3
                for l in range(j * 3, l_limit):
                    sub_square_numbers[m] = square[k][l]
                    m += 1
            # testing if each number in the subsquare falls between 1-9 and is not repeated
            for number in range(1, 10):
                if number not in sub_square_numbers:
                    sub_square_status = False
            # prints statements if the subsquare does or does not satisfy the sudoku requirements, i is the row value
            # and j is the column value
            if sub_square_status:
                print("Sub-square[", i, "][", j, "] satisfies the requirements!")
            else:
                print("Sub-square[", i, "][", j, "] violates the requirements!")

def info():
    # general information about the program and what it does
    print("*" * 100)
    print("This program takes a .txt file and validates if the 9x9 square meets the requirements of a completed \n"
          "Sudoku puzzle. It begins by testing the rows and columns, and then it tests the diagonal and anti-diagonal \n"
          "for containing numbers 1-9 with no repititions. Lastly, it tests each 3x3 square within the 9x9 square \n"
          "that meets the Sudoku requirements.")
    print("*" * 100)

main()

