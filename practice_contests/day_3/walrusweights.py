"""
Problem Title: Walrus Weights
Platform: Kattis
Problem URL: https://open.kattis.com/problems/walrusweights
Difficulty: Medium
Categories: Dynamic Programming, Subset Sum


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Use subset-sum dynamic programming to keep track of which combined
weights can be made using the available weight plates.

dp[w] is True if it is possible to create a total weight of exactly w.

For every plate, go through the possible weights backwards and mark
the new weights that can be created by adding that plate.

We only need to consider weights up to 2000 because our target is 1000.
Anything above 2000 would be more than 1000 away from the target and
therefore cannot be the best answer.

After building the DP array, search outward from 1000 until we find
a reachable weight.

If two weights are equally close to 1000, choose the larger one.


Notes:
We loop through the DP array backwards when adding each plate.
This makes sure that each plate is only used once.

Time complexity: O(n * 2000)
Memory complexity: O(2000)
"""

import sys


def main():
    input = sys.stdin.buffer.readline

    n = int(input())

    weights = []

    for _ in range(n):
        weights.append(int(input()))

    # dp[w] tells us whether it is possible to create
    # a combined weight of exactly w.
    #
    # We only care about weights from 0 to 2000.
    dp = [False] * 2001

    # Before using any plates, a total weight of 0 is possible.
    dp[0] = True

    # Process each weight plate one at a time.
    for weight in weights:

        # Go backwards through the possible totals.
        #
        # Going backwards is important because each plate
        # can only be used once.
        for current in range(2000 - weight, -1, -1):

            # If we could already make this weight,
            # then adding the current plate creates
            # another possible weight.
            if dp[current]:
                dp[current + weight] = True

    # Now find the reachable weight closest to 1000.
    #
    # distance = 0 checks 1000
    # distance = 1 checks 1001 and 999
    # distance = 2 checks 1002 and 998
    # and so on.
    for distance in range(1001):

        higher = 1000 + distance
        lower = 1000 - distance

        # Check the higher value first because if both
        # are equally close, the problem wants the larger one.
        if higher <= 2000 and dp[higher]:
            print(higher)
            return

        if lower >= 0 and dp[lower]:
            print(lower)
            return


main()
