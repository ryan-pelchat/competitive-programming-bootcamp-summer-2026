"""
Problem Title: Spiderman's Workout
Platform: Kattis
Problem URL: https://open.kattis.com/problems/spiderman
Difficulty: Medium
Categories: Dynamic Programming, Path Reconstruction

Date Solved (DD-MM-YYYY): 19-08-2026
Language: Python3


Approach:
Use a 2D dynamic programming table to track Spiderman's workout.
At each step of the workout, Spiderman can either climb UP or climb DOWN.
We need to track every possible height he could be at.

Since we want to minimize the *maximum* height he reaches during the workout,
our DP table will store the "lowest peak height" encountered on the way to
any specific state.

dp[step][height] = The lowest peak height Spiderman had to reach to get
                   to this 'height' exactly after this many 'step's.

Because we need to output the exact sequence of U and D moves, we keep a
second table (`parent`) that remembers exactly which choice brought us to
each state. Once the DP is finished, we start at the end (Step M, Height 0)
and trace our breadcrumbs backwards.


Notes:
This version prioritizes explicit, narrative variable names over compactness.
The simulation is broken down into highly readable choices ("Climb UP" vs
"Climb DOWN") making the state transitions easy to follow.

Time complexity: O(M * S) where M is the number of distances and S is the max possible height.
Memory complexity: O(M * S) to store the DP and parent tables.
"""

import sys


def solve(distances):
    num_moves = len(distances)

    # If Spiderman climbs UP on every single move, this is the absolute highest he can go.
    max_possible_height = sum(distances)

    # Use infinity to represent states (heights) that Spiderman cannot reach.
    INF = float("inf")

    # dp[step][height] stores the minimum "peak height" reached to get to this state.
    dp = [[INF for _ in range(max_possible_height + 1)] for _ in range(num_moves + 1)]

    # breadcrumbs[step][height] stores a tuple: (previous_height, move_direction)
    # We use this to trace our steps backwards at the end.
    breadcrumbs = [
        [None for _ in range(max_possible_height + 1)] for _ in range(num_moves + 1)
    ]

    # PHASE 1: SETUP
    # Before he starts, Spiderman is at step 0, height 0, and his peak height is 0.
    dp[0][0] = 0

    # PHASE 2: SIMULATE THE WORKOUT (Moving Forwards)
    for step in range(num_moves):
        workout_dist = distances[step]

        # Check every single height Spiderman might currently be at
        for current_height in range(max_possible_height + 1):

            peak_height_so_far = dp[step][current_height]

            # If this height is unreachable at the current step, skip it
            if peak_height_so_far == INF:
                continue

            # ---------------------------------------------------------
            # CHOICE A: CLIMB UP
            # ---------------------------------------------------------
            height_after_climbing_up = current_height + workout_dist

            if height_after_climbing_up <= max_possible_height:
                # Climbing up might establish a new peak height for this route
                new_peak = max(peak_height_so_far, height_after_climbing_up)

                # If this route gives us a lower peak than any previous route that
                # ended up at this exact height and step, we save it!
                if new_peak < dp[step + 1][height_after_climbing_up]:
                    dp[step + 1][height_after_climbing_up] = new_peak
                    breadcrumbs[step + 1][height_after_climbing_up] = (
                        current_height,
                        "U",
                    )

            # ---------------------------------------------------------
            # CHOICE B: CLIMB DOWN
            # ---------------------------------------------------------
            height_after_climbing_down = current_height - workout_dist

            # Spiderman cannot go below street level (height 0)
            if height_after_climbing_down >= 0:

                # Climbing down never creates a new peak height
                new_peak = peak_height_so_far

                # Check if this route is better (lower peak) than previous routes to this state
                if new_peak < dp[step + 1][height_after_climbing_down]:
                    dp[step + 1][height_after_climbing_down] = new_peak
                    breadcrumbs[step + 1][height_after_climbing_down] = (
                        current_height,
                        "D",
                    )

    # PHASE 3: RECONSTRUCT THE PATH (Working Backwards)

    # Spiderman MUST finish back at street level (height 0) after all moves
    if dp[num_moves][0] == INF:
        return "IMPOSSIBLE"

    path = []
    current_height = 0

    # Trace backwards from the final move down to the first move
    for step in range(num_moves, 0, -1):
        # Look at our breadcrumb trail to see how we got to the current height
        previous_height, move_taken = breadcrumbs[step][current_height]

        # Record the move
        path.append(move_taken)

        # Move our tracker back to where we came from for the next loop iteration
        current_height = previous_height

    # Because we traced backwards, our path is reversed. Flip it to the correct order.
    path.reverse()

    return "".join(path)


def main():
    # Read all input data at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    num_test_cases = int(input_data[0])
    current_index = 1

    for _ in range(num_test_cases):
        num_moves = int(input_data[current_index])
        current_index += 1

        # Extract the list of distances for this specific test case
        distances = []
        for _ in range(num_moves):
            distances.append(int(input_data[current_index]))
            current_index += 1

        result = solve(distances)
        print(result)


if __name__ == "__main__":
    main()


# """
# Problem Title: Spiderman's Workout
# Platform: Kattis
# Problem URL: https://open.kattis.com/problems/spiderman
# Difficulty: Medium
# Categories: Dynamic Programming, Path Reconstruction


# Date Solved (DD-MM-YYYY): 16-08-2026
# Language: Python3


# Approach:
# Use dynamic programming to keep track of every height Spiderman can
# reach after each workout distance.

# For each move, Spiderman can either:
# - Go UP by the given distance
# - Go DOWN by the given distance

# He is never allowed to go below height 0.

# For each reachable height, store the smallest maximum height reached
# along the path used to get there.

# After processing every move, we must end at height 0.

# We also store the previous height and whether we moved U or D so that
# we can reconstruct the final path.


# Notes:
# dp[i][h] represents the smallest maximum height reached after completing
# the first i moves and ending at height h.

# If dp[m][0] is unreachable, then the answer is IMPOSSIBLE.

# Time complexity: O(M * S)
# Memory complexity: O(M * S)

# where S is the sum of all workout distances.
# """

# import sys


# def solve(distances):
#     m = len(distances)

#     # The highest possible height is if every move goes upward.
#     max_height = sum(distances)

#     INF = float("inf")

#     # dp[i][h] = minimum possible highest point reached
#     # after completing i moves and ending at height h.
#     dp = [[INF] * (max_height + 1) for _ in range(m + 1)]

#     # parent[i][h] stores:
#     # (previous_height, move)
#     #
#     # This lets us reconstruct how we reached each state.
#     parent = [[None] * (max_height + 1) for _ in range(m + 1)]

#     # Before making any moves, Spiderman starts at height 0.
#     dp[0][0] = 0

#     # Process each workout distance one at a time.
#     for i in range(m):
#         distance = distances[i]

#         # Try every height that may have been reached
#         # after the first i moves.
#         for height in range(max_height + 1):

#             # If this state was never reachable, skip it.
#             if dp[i][height] == INF:
#                 continue

#             # -------------------------
#             # Option 1: Move UP
#             # -------------------------

#             new_height = height + distance

#             if new_height <= max_height:

#                 # Moving upward may create a new highest point.
#                 highest = max(dp[i][height], new_height)

#                 # Only keep this path if it gives us a lower
#                 # maximum height than what we already found.
#                 if highest < dp[i + 1][new_height]:
#                     dp[i + 1][new_height] = highest

#                     parent[i + 1][new_height] = (height, "U")

#             # -------------------------
#             # Option 2: Move DOWN
#             # -------------------------

#             new_height = height - distance

#             # Spiderman is not allowed to go below ground.
#             if new_height >= 0:

#                 # Moving down cannot increase the maximum height.
#                 highest = dp[i][height]

#                 if highest < dp[i + 1][new_height]:
#                     dp[i + 1][new_height] = highest

#                     parent[i + 1][new_height] = (height, "D")

#     # Spiderman must finish back at height 0.
#     if dp[m][0] == INF:
#         return "IMPOSSIBLE"

#     # -------------------------
#     # Reconstruct the path
#     # -------------------------

#     path = []
#     height = 0

#     # Start from the final state and work backwards.
#     for i in range(m, 0, -1):

#         previous_height, move = parent[i][height]

#         path.append(move)

#         # Move to the state we came from.
#         height = previous_height

#     # We reconstructed backwards, so reverse the moves.
#     path.reverse()

#     return "".join(path)


# def main():
#     input = sys.stdin.buffer.readline

#     test_cases = int(input())

#     for _ in range(test_cases):
#         m = int(input())

#         distances = list(map(int, input().split()))

#         print(solve(distances))


# main()
