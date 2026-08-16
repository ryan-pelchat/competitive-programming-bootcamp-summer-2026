"""
Problem Title: Firefly
Platform: Kattis
Problem URL: https://open.kattis.com/problems/firefly
Difficulty: Easy
Categories: Binary Search, Sorting, Arrays

Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Separate the obstacles into two lists:
- Stalagmites growing from the bottom
- Stalactites hanging from the top

Sort both lists.

For each possible flying height, use binary search to find how many
bottom and top obstacles are long enough to hit the firefly.

For the bottom obstacles, an obstacle hits if:
    length >= height

For the top obstacles, an obstacle hits if:
    length >= H - height + 1

Keep track of the minimum number of obstacles hit and how many heights
produce that minimum.


Notes:
bisect_left finds the first obstacle with length greater than or equal
to the required length.

If that position is i, then len(list) - i obstacles will be hit.

Time complexity is O(N log N + H log N).
"""

import sys
from bisect import bisect_left


def main():
    input = sys.stdin.buffer.readline

    n, h = map(int, input().split())

    bottom = []
    top = []

    # Obstacles alternate between bottom and top
    for i in range(n):
        length = int(input())

        if i % 2 == 0:
            bottom.append(length)
        else:
            top.append(length)

    # Binary search requires sorted lists
    bottom.sort()
    top.sort()

    minimum = n
    count = 0

    # Try every possible flying height
    for height in range(1, h + 1):

        # Bottom obstacles hit if their length >= height
        index = bisect_left(bottom, height)
        bottom_hits = len(bottom) - index

        # Top obstacles must reach down far enough to hit this height
        required_length = h - height + 1

        index = bisect_left(top, required_length)
        top_hits = len(top) - index

        hits = bottom_hits + top_hits

        if hits < minimum:
            minimum = hits
            count = 1

        elif hits == minimum:
            count += 1

    print(minimum, count)


main()
