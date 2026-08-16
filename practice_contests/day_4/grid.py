"""
Problem Title: Grid
Platform: Kattis
Problem URL: https://open.kattis.com/problems/grid
Difficulty: Easy
Categories: Graphs, BFS, Shortest Path, Grid


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Treat every cell in the grid as a node in a graph.

The number inside a cell tells us exactly how far we must move.
From a cell containing d, we can try moving:
- d spaces up
- d spaces down
- d spaces left
- d spaces right

Each move has the same cost of 1, so BFS can be used to find the
minimum number of moves from the top-left corner to the bottom-right.

Keep a distance array where distance[r][c] stores the minimum number
of moves needed to reach that cell.

If the bottom-right cell is never reached, print -1.


Notes:
BFS works because every move has the same cost.

A cell only needs to be added to the queue once because the first
time BFS reaches it will always be using the shortest path.

Time complexity: O(R * C)
Memory complexity: O(R * C)
"""

import sys
from collections import deque


def main():
    input = sys.stdin.buffer.readline

    rows, cols = map(int, input().split())

    grid = []

    for _ in range(rows):
        # Decode the bytes into a normal string first.
        # For example, b"2123" becomes "2123".
        row = input().strip().decode()

        # Convert each character into an integer.
        # "2123" becomes [2, 1, 2, 3].
        grid.append([int(char) for char in row])

    # distance[r][c] stores the minimum number of moves
    # needed to reach that cell.
    #
    # -1 means the cell has not been visited yet.
    distance = [[-1] * cols for _ in range(rows)]

    # Start BFS from the top-left corner.
    queue = deque([(0, 0)])
    distance[0][0] = 0

    # Four possible directions.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up  # down  # left  # right

    while queue:
        row, col = queue.popleft()

        # The value in this cell tells us exactly
        # how far we must move.
        jump = grid[row][col]

        # Try jumping in all four directions.
        for dr, dc in directions:
            new_row = row + dr * jump
            new_col = col + dc * jump

            # Ignore moves that leave the grid.
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                continue

            # If this cell was already visited, BFS has
            # already found the shortest path to it.
            if distance[new_row][new_col] != -1:
                continue

            # This jump counts as one move.
            distance[new_row][new_col] = distance[row][col] + 1

            queue.append((new_row, new_col))

    # Bottom-right cell contains the answer.
    # If it was never reached, it will still be -1.
    print(distance[rows - 1][cols - 1])


main()
