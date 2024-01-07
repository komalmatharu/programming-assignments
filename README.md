# programming-assignments

The code in this repository is a collection of Python assignments to showcase the range of my capabilities with the programming language.

**Programming Assignment 1:**

Coding the provided pattern displays proficiency in using nested loops, pattern recognition, mathematical logic, logical thinking, knowledge of basic Python syntax, problem-solving, and visualization skills to systematically generate the University of Arizona logo.

**Programming Assignment 2:**

This code utilizes a graphical library (e.g., DrawingPanel) and displays an understanding its functions to draw various shapes, including rectangles, ovals, lines, and arcs to create a turtle graphic.

**Programming Assignment 3:**

The 'gibberish' function in the provided code reads the content of the file "english_text.txt" and applies specific rules to transform the text. The transformation rules are as follows:

  1. If the character is a lowercase vowel (a, e, i, o, u), "egg" is added before that vowel in the result string.
  2. If the character is an uppercase vowel (A, E, I, O, U), "ldig" is added before that vowel in the result string after converting it to lowercase.
  3. If the character is not a vowel, it remains unchanged and is appended to the result string.

The resulting string, after applying these rules, is printed to the console. The code demonstrates proficiency in file handling, string manipulation, and conditional statements for character-based transformations.

**Programming Assignment 4:**

The main function reads a Sudoku puzzle from a text file named "x-sudoku.txt" and checks whether it satisfies the requirements of a completed Sudoku puzzle. The program performs the following tasks:

1. Display Information: Prints general information about the program's functions.
2. Read File Content: Opens and reads the "x-sudoku.txt" file, storing the content in sudo_data.
3. Initialize Matrix: Initializes a 9x9 matrix with values from the file.
4. Display Squares: Prints each 9x9 square in a formatted manner.
5. Call Test Functions: Calls various test functions to check the Sudoku requirements for rows, columns, diagonals, anti-diagonals, and sub-squares.

The test functions include:

test_row: Checks each row for numbers 1-9 with no repetitions.
test_col: Checks each column for numbers 1-9 with no repetitions.
test_main_diag: Checks the main diagonal for numbers 1-9 with no repetitions
test_anti_diag: Checks the anti-diagonal for numbers 1-9 with no repetitions.
test_sub_square: Checks each 3x3 sub-square within the 9x9 square for numbers 1-9 with no repetitions.

Display Results: Prints statements indicating whether each row, column, diagonal, anti-diagonal, and sub-square satisfies or violates the Sudoku requirements.
Info Function: Provides general information about the program's purpose.

This code demonstrates skills in file handling, nested loops, matrix manipulation, and functional decomposition to validate a Sudoku puzzle against specified requirements.

**Programming Assignment 5:**

The provided Python script utilizes the Pandas library to manipulate and analyze a dataset from a CSV file. Here's a breakdown of each task:

**Task a:**
- Reads a CSV file named 'review_phx_hw.csv' into a Pandas DataFrame (`review_df_a`).
- Fills missing values with -1.
- Converts the 'postal_code' column to integer and then to string.
- Prints the first and last 15 observations of the DataFrame.

**Task b:**
- Creates a new DataFrame (`review_df_b`) by copying the original (`review_df_a`).
- Excludes observations where 'stars' or 'review_count' is equal to -1.
- Prints the first and last 15 observations of the new DataFrame.
- Describes the 'review_count' and 'stars' columns.

**Task c:**
- Creates another DataFrame (`review_df_c`) by copying `review_df_b`.
- Filters for closed restaurants with 100-500 reviews and above 3.0 stars.
- Prints the filtered DataFrame.
- Calculates the average star rating and review count grouped by postal codes (`agg1`).

**Task d:**
- Creates a DataFrame (`review_df_d`) by selecting only postal codes 85004, 85006, and 85008 from `review_df_b`.

**Task e:**
- Concatenates `review_df_c` and `review_df_d` into a final DataFrame (`review_df_final`).
- Drops any duplicate values.
- Sorts the DataFrame by ascending postal code and descending rating.
- Includes only the columns of 'name', 'postal_code', 'stars', and 'review_count'.
- Converts the final DataFrame to a CSV file named 'komalmatharu_pa5.csv'.

Overall, the script demonstrates effective data cleaning, filtering, manipulation, and analysis using Pandas, and it concludes by saving the processed data to a CSV file.


