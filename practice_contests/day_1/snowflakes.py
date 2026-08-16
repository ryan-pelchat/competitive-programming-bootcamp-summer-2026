"""
Problem Title: Snowflakes
Platform: Kattis
Problem URL: https://open.kattis.com/problems/snowflakes
Difficulty: Medium
Categories: Sliding Window, Two Pointers, Hash Map

Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Use a sliding window to keep track of the current sequence of unique snowflakes.

A dictionary stores the last position where each snowflake was seen.
If a duplicate appears inside the current window, move the left side of
the window to just after the previous occurrence.

Keep track of the largest valid window found.


Notes:
Each snowflake is processed once, giving an O(n) expected time complexity.
The dictionary can contain up to O(n) snowflake IDs.
"""

import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0

    test_cases = data[pos]
    pos += 1

    answers = []

    for _ in range(test_cases):
        n = data[pos]
        pos += 1

        last_seen = {}
        left = 0
        best = 0

        for right in range(n):
            snowflake = data[pos]
            pos += 1

            # Move left past the previous copy if it is in our window
            if snowflake in last_seen and last_seen[snowflake] >= left:
                left = last_seen[snowflake] + 1

            last_seen[snowflake] = right

            best = max(best, right - left + 1)

        answers.append(str(best))

    print("\n".join(answers))


solve()
