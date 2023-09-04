def solve_puzzle(board, source, destination):
    """
    :param board: M X N matrix, representing a Puzzle with obstacles
    :param source: tuple of starting cell
    :param destination: tuple of ending cell
    :return: directions in the form of "LRUD" and a list
    of tuples representing the path taken
    """

    # create output variables and BFS queue
    visited = [(source[0], source[1])]
    path = ''
    q = [(source[0], source[1], path)]
    if source == destination:
        return [source], path
    shortest_path = None

    # traverse through queue to neighboring cells
    while q:
        r, c, path = q.pop(0)
        if (r, c) == destination:
            shortest_path = path
            break

        # possible path options, will verify move is within bounds
        moves = [(r, c - 1, 'L'), (r, c + 1, 'R'), (r - 1, c, 'U'), (r + 1, c, 'D')]
        for i, j, k in moves:
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                if board[i][j] != '#':
                    if (i, j) not in visited:
                        q.append((i, j, path + k))
                        visited.append((i, j))

    if not shortest_path:
        return None
    # retrace path from source
    res = []
    move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    res.append((source[0], source[1]))
    x = source[0]
    y = source[1]
    for letter in range(len(shortest_path)):
        d = shortest_path[letter]
        e, f = move[d]
        resB = (x + e, f + y)
        x, y = resB[0], resB[1]
        res.append(resB)

    return res, shortest_path


puzzle = [
    ['-', '-', '#'],
    ['#', '-', '-'],
    ['-', '#', '-']
]

Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]
start = (0, 2)
end = (2, 2)
