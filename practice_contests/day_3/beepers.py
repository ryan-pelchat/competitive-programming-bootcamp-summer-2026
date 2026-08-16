"""
Problem Title: Collecting Beepers
Platform: Kattis
Problem URL: https://open.kattis.com/problems/beepers
Difficulty: Medium
Categories: Dynamic Programming, Bitmask DP, TSP, Manhattan Distance


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Treat the problem like a small Travelling Salesman Problem.

The robot starts at one position and must:
1. Visit every beeper.
2. Visit each beeper only once.
3. Return to the starting position.

Use a bitmask to keep track of which beepers have already been visited.

dp(current, mask) represents the minimum distance needed when:
- We are currently at position "current".
- "mask" tells us which beepers have already been collected.

From the current position, try travelling to every unvisited beeper.
When all beepers have been visited, return directly to the starting point.


Notes:
Movement is horizontal and vertical, so the distance between two points
is their Manhattan distance:

    abs(x1 - x2) + abs(y1 - y2)

Bit i in the mask is 1 if beeper i has already been visited.

Time complexity: O(B^2 * 2^B)
Memory complexity: O(B * 2^B)

where B is the number of beepers.
"""

import sys
from functools import lru_cache


def distance(a, b):
    # Manhattan distance between two coordinates
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve_case():
    # Grid dimensions are not actually needed for the calculation
    width, height = map(int, input().split())

    # Starting position of the robot
    start_x, start_y = map(int, input().split())

    num_beepers = int(input())

    # points[0] will always be the starting position
    # points[1], points[2], ... will be the beepers
    points = [(start_x, start_y)]

    for _ in range(num_beepers):
        x, y = map(int, input().split())
        points.append((x, y))

    # If there are B beepers, then a mask of B ones means
    # that every beeper has been visited.
    #
    # Example with 3 beepers:
    # 111 in binary = 7
    all_visited = (1 << num_beepers) - 1

    @lru_cache(None)
    def dp(current, mask):
        """
        Return the minimum remaining distance.

        current:
            Index in the points list of where the robot currently is.
            0 means the starting location.
            1..B means one of the beepers.

        mask:
            Bitmask showing which beepers have already been visited.
        """

        # If every beeper has been collected, the only thing left
        # to do is return to the starting position.
        if mask == all_visited:
            return distance(points[current], points[0])

        best = float("inf")

        # Try visiting every beeper that has not been visited yet
        for beeper in range(num_beepers):

            # Check whether this beeper's bit is already turned on
            if mask & (1 << beeper):
                continue

            # Beeper 0 is stored at points[1],
            # beeper 1 is stored at points[2], etc.
            next_point = beeper + 1

            # Turn on this beeper's bit to mark it as visited
            new_mask = mask | (1 << beeper)

            # Cost to travel to this beeper
            travel = distance(points[current], points[next_point])

            # Then recursively find the best route from there
            total = travel + dp(next_point, new_mask)

            best = min(best, total)

        return best

    # Start at points[0] with no beepers visited
    return dp(0, 0)


def main():
    global input
    input = sys.stdin.buffer.readline

    test_cases = int(input())

    for _ in range(test_cases):
        answer = solve_case()
        print(answer)


main()
