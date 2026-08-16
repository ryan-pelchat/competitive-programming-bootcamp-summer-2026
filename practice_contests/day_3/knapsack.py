"""
Problem Title: Knapsack
Platform: Kattis
Problem URL: https://open.kattis.com/problems/knapsack
Difficulty: Medium
Categories: Dynamic Programming, 0/1 Knapsack, Reconstruction


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Use dynamic programming where dp[w] stores the maximum value that can
be obtained with a knapsack capacity of w.

For each item, go through the capacities backwards. Going backwards
ensures that each item can only be used once.

We also store whether each item was chosen when improving a DP state.
After finishing the DP, work backwards through the items to reconstruct
which item indices were used.


Notes:
The backwards loop is important for 0/1 Knapsack. If we looped forward,
the same item could be used multiple times.

Time complexity: O(n * C)
Memory complexity: O(n * C) for reconstructing the chosen items.
"""

import sys


def solve(capacity, n, items):
    # dp[w] = best value possible with capacity w
    dp = [0] * (capacity + 1)

    # chosen[i][w] tells us if item i was used
    # when we improved the answer for capacity w
    chosen = [bytearray(capacity + 1) for _ in range(n)]

    for i in range(n):
        value, weight = items[i]

        # Go backwards so this item cannot be used more than once
        for w in range(capacity, weight - 1, -1):
            new_value = dp[w - weight] + value

            if new_value > dp[w]:
                dp[w] = new_value
                chosen[i][w] = 1

    # Work backwards to find which items were chosen
    result = []
    remaining = capacity

    for i in range(n - 1, -1, -1):
        if chosen[i][remaining]:
            result.append(i)
            remaining -= items[i][1]

    result.reverse()

    return result


def main():
    input = sys.stdin.buffer.readline
    output = []

    # There can be multiple test cases until EOF
    while True:
        line = input()

        if not line:
            break

        if not line.strip():
            continue

        capacity, n = map(int, line.split())

        items = []

        for _ in range(n):
            value, weight = map(int, input().split())
            items.append((value, weight))

        result = solve(capacity, n, items)

        # First print how many items were selected
        output.append(str(len(result)))

        # Then print their original 0-based indices
        output.append(" ".join(map(str, result)))

    sys.stdout.write("\n".join(output))


main()
