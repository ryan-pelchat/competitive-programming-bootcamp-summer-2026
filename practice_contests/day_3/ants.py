"""
Problem Title: Ants
Platform: Kattis
Problem URL: https://open.kattis.com/problems/ants
Difficulty: Easy
Categories: Greedy, Simulation, Mathematics


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
When two ants collide and turn around, we can think of them as simply
passing through each other. Since the ants are identical, this does not
change when ants fall off the pole.

For the earliest possible time, each ant should move toward its closest
end. The answer is the largest of these closest distances.

For the latest possible time, each ant should move toward its farthest
end. The answer is the largest of these farthest distances.


Notes:
No simulation of collisions is needed.

For an ant at position p:
- Distance to the left end is p
- Distance to the right end is length - p

Time complexity: O(n) per test case.
Memory complexity: O(1), apart from the input.
"""

import sys

data = sys.stdin.read().splitlines()
# print(data)
data = data[::-1]

caseNumber = int(data.pop())

while data:
    pole, antNum = map(int, data.pop().split())
    antPos = []

    while len(antPos) < antNum:
        antPos.extend(list(map(int, data.pop().split())))

    earliest = 0
    latest = 0

    for pos in antPos:
        left = pos
        right = pole - pos

        # For the earliest time, the ant takes the shorter path
        closest_end = min(left, right)
        earliest = max(earliest, closest_end)

        # For the latest time, the ant takes the longer path
        farthest_end = max(left, right)
        latest = max(latest, farthest_end)

    print(earliest, latest)


# import sys


# def main():
#     input = sys.stdin.buffer.readline

#     cases = int(input())

#     for _ in range(cases):
#         length, n = map(int, input().split())

#         # The positions may span multiple input lines
#         positions = []

#         while len(positions) < n:
#             positions.extend(map(int, input().split()))

#         earliest = 0
#         latest = 0

#         for position in positions:
#             left = position
#             right = length - position

#             # For the earliest time, the ant takes the shorter path
#             closest_end = min(left, right)
#             earliest = max(earliest, closest_end)

#             # For the latest time, the ant takes the longer path
#             farthest_end = max(left, right)
#             latest = max(latest, farthest_end)

#         print(earliest, latest)


# main()
