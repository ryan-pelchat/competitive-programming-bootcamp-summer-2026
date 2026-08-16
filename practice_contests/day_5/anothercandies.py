"""
Problem Title: Another Candies
Platform: Kattis
Problem URL: https://open.kattis.com/problems/anothercandies
Difficulty: Easy
Categories: Mathematics, Modular Arithmetic, Divisibility


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
For each test case, add up the number of candies belonging to all
of the children.

The candies can be redistributed equally if the total number of
candies is divisible by the number of children.

So we check:

    total_candies % number_of_children == 0

If it is divisible, print "YES".
Otherwise, print "NO".


Notes:
We do not need to simulate actually moving candies between children.

Only the total number of candies matters.

Time complexity: O(N) per test case
Memory complexity: O(1)
"""

import sys


def main():
    input = sys.stdin.buffer.readline

    test_cases = int(input())

    for _ in range(test_cases):

        # The input contains a blank line before each test case.
        input()

        n = int(input())

        total_candies = 0

        # Add up all candies owned by the children.
        for _ in range(n):
            candies = int(input())
            total_candies += candies

        # If the total is divisible by the number of children,
        # everyone can end up with exactly the same amount.
        if total_candies % n == 0:
            print("YES")
        else:
            print("NO")


main()
