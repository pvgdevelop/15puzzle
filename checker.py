def check_solution(matrix):
    """
    function to check solvable puzzle or not.
    can use with 3x3, 4x4, 5x5, e.t.c.
    """
    matrix_to_list = []
    game_type = len(matrix)
    for row in matrix:
        for item in row:
            if item == 0:
                zero_pos = matrix.index(row) + 1   # what row zero cell is.
        matrix_to_list += row
    sum_of_swaps = 0  # count of swaps
    sorting_iters = 1  # count of iters for bubble sort
    matrix_to_list.remove(0)
    while sorting_iters < len(matrix_to_list):
        for i in range(len(matrix_to_list) - 1):
            if matrix_to_list[i] > matrix_to_list[i + 1]:
                matrix_to_list[i], matrix_to_list[i + 1] = \
                    matrix_to_list[i + 1], matrix_to_list[i]
                sum_of_swaps += 1
        sorting_iters += 1

    if game_type % 2 == 0:
        sum_of_swaps += zero_pos
    if sum_of_swaps % 2 == 0:
        print('puzzle have solution')
        return True
    else:
        print('puzzle have not solution')
        return False


if __name__ == '__main__':
    solvable_matrix = [[1, 2, 6, 3], [4, 9, 5, 7], [8, 13, 11, 15], [12, 10, 14, 0]]
    unsolvable_matrix = [[1, 2, 6, 3], [4, 9, 5, 7], [8, 13, 11, 15], [12, 14, 0, 10]]

    print(check_solution(solvable_matrix))
    print(check_solution(unsolvable_matrix))
