"""
Problem Title: Smallest Multiple
Platform: Kattis
Problem URL: https://open.kattis.com/problems/smallestmultiple
Difficulty: Medium
Categories: Number Theory, GCD, LCM, Euclidean Algorithm


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Read each line of input as a separate test case.

For every line, find the Least Common Multiple (LCM) of all the
numbers on that line.

The LCM of two numbers can be calculated using their GCD:

    lcm(a, b) = (a * b) // gcd(a, b)

Start with the first number, then repeatedly combine it with the
next number until every number on the line has been included.

Print the final LCM for each line.


Notes:
The GCD is calculated using Python's built-in gcd function, which
uses the Euclidean algorithm.

We do not know how many test cases there are beforehand, so input
is read until EOF.

Time complexity: O(K * log M) per line
Memory complexity: O(K)

where K is the number of integers on a line and M is the size
of the numbers.
"""

import sys
from math import gcd


def lcm(a, b):
    # Use the relationship between GCD and LCM:
    #
    # gcd(a, b) * lcm(a, b) = a * b
    return (a * b) // gcd(a, b)


def main():
    # Each line is a separate test case.
    # Reading directly from sys.stdin continues until EOF.
    for line in sys.stdin:

        # Convert all numbers on this line into integers.
        numbers = list(map(int, line.split()))

        # Skip an empty line if one appears.
        if not numbers:
            continue

        # Start with the first number.
        answer = numbers[0]

        # Combine the current LCM with each remaining number.
        #
        # Example:
        # 2 3 4
        #
        # lcm(2, 3) = 6
        # lcm(6, 4) = 12
        for i in range(1, len(numbers)):
            answer = lcm(answer, numbers[i])

        print(answer)


main()
