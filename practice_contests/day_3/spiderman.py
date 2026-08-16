"""
Problem Title: Spiderman's Workout
Platform: Kattis
Problem URL: https://open.kattis.com/problems/spiderman
Difficulty: Medium
Categories: Dynamic Programming, Path Reconstruction


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Use dynamic programming to keep track of every height Spiderman can
reach after each workout distance.

For each move, Spiderman can either:
- Go UP by the given distance
- Go DOWN by the given distance

He is never allowed to go below height 0.

For each reachable height, store the smallest maximum height reached
along the path used to get there.

After processing every move, we must end at height 0.

We also store the previous height and whether we moved U or D so that
we can reconstruct the final path.


Notes:
dp[i][h] represents the smallest maximum height reached after completing
the first i moves and ending at height h.

If dp[m][0] is unreachable, then the answer is IMPOSSIBLE.

Time complexity: O(M * S)
Memory complexity: O(M * S)

where S is the sum of all workout distances.
"""

import sys


def solve(distances):
    m = len(distances)

    # The highest possible height is if every move goes upward.
    max_height = sum(distances)

    INF = float("inf")

    # dp[i][h] = minimum possible highest point reached
    # after completing i moves and ending at height h.
    dp = [[INF] * (max_height + 1) for _ in range(m + 1)]

    # parent[i][h] stores:
    # (previous_height, move)
    #
    # This lets us reconstruct how we reached each state.
    parent = [[None] * (max_height + 1) for _ in range(m + 1)]

    # Before making any moves, Spiderman starts at height 0.
    dp[0][0] = 0

    # Process each workout distance one at a time.
    for i in range(m):
        distance = distances[i]

        # Try every height that may have been reached
        # after the first i moves.
        for height in range(max_height + 1):

            # If this state was never reachable, skip it.
            if dp[i][height] == INF:
                continue

            # -------------------------
            # Option 1: Move UP
            # -------------------------

            new_height = height + distance

            if new_height <= max_height:

                # Moving upward may create a new highest point.
                highest = max(dp[i][height], new_height)

                # Only keep this path if it gives us a lower
                # maximum height than what we already found.
                if highest < dp[i + 1][new_height]:
                    dp[i + 1][new_height] = highest

                    parent[i + 1][new_height] = (height, "U")

            # -------------------------
            # Option 2: Move DOWN
            # -------------------------

            new_height = height - distance

            # Spiderman is not allowed to go below ground.
            if new_height >= 0:

                # Moving down cannot increase the maximum height.
                highest = dp[i][height]

                if highest < dp[i + 1][new_height]:
                    dp[i + 1][new_height] = highest

                    parent[i + 1][new_height] = (height, "D")

    # Spiderman must finish back at height 0.
    if dp[m][0] == INF:
        return "IMPOSSIBLE"

    # -------------------------
    # Reconstruct the path
    # -------------------------

    path = []
    height = 0

    # Start from the final state and work backwards.
    for i in range(m, 0, -1):

        previous_height, move = parent[i][height]

        path.append(move)

        # Move to the state we came from.
        height = previous_height

    # We reconstructed backwards, so reverse the moves.
    path.reverse()

    return "".join(path)


def main():
    input = sys.stdin.buffer.readline

    test_cases = int(input())

    for _ in range(test_cases):
        m = int(input())

        distances = list(map(int, input().split()))

        print(solve(distances))


main()
