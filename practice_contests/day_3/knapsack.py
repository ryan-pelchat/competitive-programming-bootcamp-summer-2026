"""
Problem Title: Knapsack
Platform: Kattis
Problem URL: https://open.kattis.com/problems/knapsack
Difficulty: Medium
Categories: Dynamic Programming, 0/1 Knapsack, Reconstruction

Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Use a 2D dynamic programming table where dp[i][w] stores the maximum
value that can be obtained using a subset of the first 'i' items and
a knapsack capacity of 'w'.

For each item and each capacity, we evaluate two choices:
1. Leave the item (take the value from the row directly above).
2. Take the item (add its value to the best value of the remaining capacity).
The DP table stores the maximum of these two choices.

To reconstruct the chosen items, we start at the bottom-right of the table.
If dp[i][w] is different from dp[i-1][w], it means item i was taken. We
record the item, subtract its weight from our current capacity, and move up.


Notes:
This is the classic, readable 2D array implementation of the 0/1 Knapsack
problem. While less memory-efficient than the 1D backwards-looping approach,
it explicitly maps out the decision-making process and makes the item
reconstruction phase highly intuitive.

Time complexity: O(n * C) where n is the number of items and C is the capacity.
Memory complexity: O(n * C) to store the 2D DP table.
"""

import sys


def solve(max_capacity, num_items, items):
    # Create a 2D grid filled with 0s.
    # Rows (0 to num_items) represent how many items we are allowed to consider.
    # Columns (0 to max_capacity) represent the current weight capacity of the bag.
    # dp[i][w] = The maximum value we can get using the first 'i' items with a bag of size 'w'.
    dp = [[0 for _ in range(max_capacity + 1)] for _ in range(num_items + 1)]

    # 1. BUILD THE DP TABLE (Moving Forwards)
    for i in range(1, num_items + 1):
        # We use i-1 because our items list is 0-indexed, but our DP table is 1-indexed
        item_value, item_weight = items[i - 1]

        for current_capacity in range(1, max_capacity + 1):

            # Case A: The item is too heavy to fit in the current bag
            if item_weight > current_capacity:
                # We are forced to leave it. Our best value is whatever we had
                # before we considered this item.
                dp[i][current_capacity] = dp[i - 1][current_capacity]

            # Case B: The item fits! We have a choice to make.
            else:
                # Option 1: Leave it
                leave_value = dp[i - 1][current_capacity]

                # Option 2: Take it (Value of item + best value of the remaining space)
                remaining_space = current_capacity - item_weight
                take_value = item_value + dp[i - 1][remaining_space]

                # The DP table stores whichever choice gave us more value
                dp[i][current_capacity] = max(leave_value, take_value)

    # 2. RECONSTRUCT THE CHOSEN ITEMS (Working Backwards)
    # The bottom-right cell of our grid now holds the absolute best value possible.
    # To find out WHICH items got us there, we trace our steps backward.

    chosen_items = []
    current_cap = max_capacity

    for i in range(num_items, 0, -1):
        # If the value changed from the row above it, it means we MUST have chosen it.
        if dp[i][current_cap] != dp[i - 1][current_cap]:
            item_index = i - 1
            chosen_items.append(item_index)

            # Subtract the item's weight from our capacity as we move up
            item_weight = items[item_index][1]
            current_cap -= item_weight

    # We found them in reverse order, so flip the list to print them in original order
    chosen_items.reverse()

    return chosen_items


def main():
    # Read all inputs at once (cleaner for Kattis EOF parsing)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    while True:
        try:
            capacity = int(next(iterator))
            n = int(next(iterator))

            items = []
            for _ in range(n):
                val = int(next(iterator))
                weight = int(next(iterator))
                items.append((val, weight))

            result = solve(capacity, n, items)

            print(len(result))
            print(" ".join(map(str, result)))

        except StopIteration:
            break  # No more test cases left


if __name__ == "__main__":
    main()
