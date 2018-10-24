
def check_sudoku(file_name):
    'Limited Sudoku solution verifier.  Verifies uniqueness of rows and columns.'

    # Load a Sudoku solution from a text file and separate lines
    input_file = open(file_name)
    lines = input_file.readlines()
    input_file.close()
    
    # Verification content
    verified = True

    # Data loaded into a 2-dimensional list
    lines_to_string = ''.join(lines).splitlines()
    line_length = len(lines_to_string)
    solution_list = list()

    for row in range(line_length):
        solution_list.append([])
        for col in range(line_length):
            solution_list[row].append(lines_to_string[row].split()[col])

    verified = check_rows(solution_list, verified)
    verified = check_col(solution_list, verified)

    if verified:
        print('Sudoku Verified.')


def check_rows(solution_list, is_verified):
    'Verifies that each row contains all digits 1 thru 9. If not, displays each bad column and indicates the first bad digit in the row.'
    
    row_solution_counter = 0
    for row in solution_list:       ##
        a_set = set(row)
        if len(row) == len(a_set):
            # print('Sudoku Verified')
            row_solution_counter += 1
        else:
            print('Row {} bad: {}  '.format(solution_list.index(row)+1, ' '.join(str(num) for num in row)), end='') 
            tmp_row = list(row)
            for c in a_set:
                tmp_row.remove(c)
            print('1st Bad Value: ' + str(tmp_row[0]))

    if row_solution_counter == len(solution_list):
        is_verified = False
    
    return is_verified

def check_col(solution_list, is_verified):
    'Verifies that each column contains all digits 1 thru 9. If not, displays each bad row and indicates the first bad digit in the column.'

    col_solution_counter = 0
    num_cols = len(solution_list[0])

    for index in range(num_cols):
        a_list = list()
        a_set = set()
        for row in solution_list:
            a_set.add(row[index])
            a_list.append(row[index])
        if len(solution_list) == len(a_set):
            col_solution_counter +=1
        else:
            print('Col {} bad: {}  '
                .format(index+1, 
                    ' '.join(str(num) for num in [solution_list[k][index] for k in range(num_cols)]), end=''))
            for c in a_set:
                a_list.remove(c)
            print('1st Bad Value: {}'.format(a_list[0]) )
     
    if col_solution_counter == len(solution_list[0]):
        is_verified = False
        return is_verified

    
user_filename = input('Enter filename: ')
check_sudoku(user_filename)

# /Users/crystalcontreras/Desktop/DePaul/CSC401 Intro to Programming/hw/Assignment_5/sudoku_bad.txt
