class Solution:
    def spiralOrder(self, matrix):
        shift = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction = x = y = 0
        spiral_ordering = []
        for _ in range(len(matrix) * len(matrix[0])):
            spiral_ordering.append(matrix[x][y])
            matrix[x][y] = 101
            next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            if next_x  < 0  or next_x >= len(matrix) or next_y < 0 or next_y >= len(matrix[0]) or matrix[next_x][next_y] == 101:
                direction = (direction + 1) % 4
                next_x, next_y = x + shift[direction][0], y + shift[direction][1]
            x, y = next_x, next_y
        return spiral_ordering
