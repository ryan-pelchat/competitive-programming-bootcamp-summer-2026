"""
Problem Title: 10 Kinds of People
Platform: Kattis
Problem URL: https://open.kattis.com/problems/10kindsofpeople
Difficulty: Easy
Categories: Graphs, DFS, Flood Fill, Connected Components


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Treat each cell in the grid as a node in a graph.

Cells are connected if they:
- Are directly beside each other (up, down, left, right)
- Contain the same value

We run DFS over the grid and give every connected region a unique ID.

Then each query becomes very simple:
- Same component + value 0 -> binary
- Same component + value 1 -> decimal
- Different components -> neither


Notes:
Instead of running DFS for every query, we process the whole grid once.

This makes each query O(1) after preprocessing.

Time complexity: O(R * C + Q)
Memory complexity: O(R * C)
"""

import sys


def main():
    input = sys.stdin.buffer.readline

    rows, cols = map(int, input().split())

    # Read the grid.
    #
    # Example:
    #
    # 11001
    # 11101
    # 00100
    #
    # Each character represents either a binary person (0)
    # or a decimal person (1).
    grid = []

    for _ in range(rows):
        grid.append(input().strip().decode())

    # component[r][c] will store which connected region
    # the cell at row r, column c belongs to.
    #
    # For example, a component grid might eventually look like:
    #
    # 0 0 1 1
    # 0 0 1 2
    # 3 3 1 2
    #
    # Cells with the same number belong to the same connected region.
    #
    # -1 means the cell has not been visited yet.
    component = [[-1] * cols for _ in range(rows)]

    # Every new connected region gets a new component ID.
    component_id = 0

    # We are only allowed to move in four directions.
    #
    # Diagonal movement is NOT allowed.
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up  # down  # left  # right

    def dfs(start_row, start_col, current_id):
        # Remember whether this region contains 0s or 1s.
        #
        # Every cell visited during this DFS must have
        # exactly this same value.
        value = grid[start_row][start_col]

        # We use a stack for iterative DFS.
        #
        # A recursive DFS could also work logically, but if the
        # connected region is very large, Python could exceed
        # its recursion limit.
        stack = [(start_row, start_col)]

        # Mark the starting cell immediately so we do not
        # accidentally add it to the stack again later.
        component[start_row][start_col] = current_id

        while stack:
            # Remove one cell from the stack and explore it.
            row, col = stack.pop()

            # Check all four possible neighbours.
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # First make sure the neighbouring cell
                # is still inside the grid.
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                    continue

                # If the cell already belongs to a component,
                # then we have already visited it.
                if component[new_row][new_col] != -1:
                    continue

                # We can only move through cells with the same value.
                #
                # A 0 cannot travel through a 1,
                # and a 1 cannot travel through a 0.
                if grid[new_row][new_col] != value:
                    continue

                # This neighbour is part of the same connected region.
                #
                # Give it the same component ID and explore it later.
                component[new_row][new_col] = current_id
                stack.append((new_row, new_col))

    # ------------------------------------------------------------
    # PREPROCESS THE GRID
    # ------------------------------------------------------------
    #
    # We go through every cell once.
    #
    # Whenever we find a cell that has not been visited,
    # that means we have discovered a new connected component.
    #
    # We then run DFS to label the entire region.
    for row in range(rows):
        for col in range(cols):

            if component[row][col] == -1:
                dfs(row, col, component_id)

                # The next new region should receive a different ID.
                component_id += 1

    # ------------------------------------------------------------
    # ANSWER QUERIES
    # ------------------------------------------------------------

    queries = int(input())

    output = []

    for _ in range(queries):
        r1, c1, r2, c2 = map(int, input().split())

        # Kattis gives coordinates starting from 1.
        #
        # Python lists start from 0, so convert:
        #
        # Kattis (1, 1) -> Python (0, 0)
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1

        # If the two cells have different component IDs,
        # there is no valid path between them.
        #
        # Even if they both contain 0 or both contain 1,
        # they may still be separated by the opposite value.
        if component[r1][c1] != component[r2][c2]:
            output.append("neither")

        # If they have the same component ID, we know:
        #
        # 1. A path exists between them.
        # 2. Every cell along that path has the same value.
        #
        # So we only need to check whether that component
        # contains 0 or 1.
        elif grid[r1][c1] == "0":
            output.append("binary")

        else:
            output.append("decimal")

    # Printing everything at once is faster than calling
    # print() separately for every query.
    sys.stdout.write("\n".join(output))


main()
