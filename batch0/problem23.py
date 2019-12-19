'''
You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
'''
def find_shortest_path(map, start, end):
    coords = [(index_r, index_c) for index_r, row in enumerate(map)
              for index_c, element in enumerate(row) if not element]

    current_distance = 0
    distances = [[None for col in range(len(map[0]))] for row in range(len(map))]
    distances[start[0]][start[1]] = 0
    while True:

        wavefront = [coord for coord in coords if distances[coord[0]][coord[1]] == current_distance]
        if not wavefront:
            break

        current_distance += 1
        for node in wavefront:

            neighbours = [coord for coord in coords if (abs(node[0] - coord[0]) + abs(node[1] - coord[1])) == 1]
            for n in neighbours:
                if distances[n[0]][n[1]] is None:
                    distances[n[0]][n[1]] = current_distance

    return distances[end[0]][end[1]]


def main():
    map = [[False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]]
    print(find_shortest_path(map, (3, 0), (0, 0)))


if __name__ == '__main__':
    main()