import pprint

from checker import check_solution


pp = pprint.PrettyPrinter(indent=4)


def puzz_astar(start, end):
    """
    A* algorithm
    """
    start = str(start)
    front = [[manhattan_distance(start, end), start]]
    expanded = []
    expanded_nodes = 0
    while front:
        i = 0
        for j in range(1, len(front)):
            if front[i][0] > front[j][0]:
                i = j
        path = front[i]
        front = front[:i] + front[i + 1:]
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in expanded:
            continue
        for k in moves(endnode):
            if k in expanded:
                continue
            newpath = [path[0] + manhattan_distance(k, end) - manhattan_distance(endnode, end)] + path[1:] + [k]
            front.append(newpath)
            expanded.append(endnode)
        expanded_nodes += 1

    print ("Expanded nodes:", expanded_nodes)
    print ("Solution: in", len(path)/4, 'moves')
    pp.pprint(path)


def moves(mat):
    """
    Returns a list of all possible moves
    """
    output = []
    m = eval(mat)
    i = 0
    while 0 not in m[i]:
        i += 1
    j = m[i].index(0)     # blank space (zero)

    if i > 0:
        m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]     # move up
        output.append(str(m))
        m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]

    if i < 3:
        m[i][j], m[i + 1][j] = m[i + 1][j], m[i][j]     # move down
        output.append(str(m))
        m[i][j], m[i + 1][j] = m[i + 1][j], m[i][j]

    if j > 0:
        m[i][j], m[i][j - 1] = m[i][j - 1], m[i][j]     # move left
        output.append(str(m))
        m[i][j], m[i][j - 1] = m[i][j - 1], m[i][j]

    if j < 3:
        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]     # move right
        output.append(str(m))
        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]

    return output


def manhattan_distance(puzz, end):
    """
    Manhettan distance heuristic
    """
    m = eval(puzz)
    a = eval(end)
    lst = []
    result = 0

    for x in range(4):
        for y in range(4):
            if a[x][y] == 0:
                continue
            lst.append([[x, y], a[x][y]])

    for i in range(4):
        for j in range(4):
            if m[i][j] == 0:
                continue
            for s in lst:
                if s[1] == m[i][j]:
                    x = s[0][0]
                    y = s[0][1]

            result += abs(i - x) + abs(j - y)
    return result


if __name__ == '__main__':
    puzzle = [[1, 2, 6, 3], [4, 9, 5, 7], [8, 13, 11, 15], [12, 10, 14, 0]]
    end = str([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    if check_solution(list(puzzle)):
        puzz_astar(puzzle, end)
