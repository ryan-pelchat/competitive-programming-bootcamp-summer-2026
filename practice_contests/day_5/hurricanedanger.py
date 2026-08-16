"""
Problem Title: Hurricane Danger!
Platform: Kattis
Problem URL: https://open.kattis.com/problems/hurricanedanger
Difficulty: Medium
Categories: Geometry, Point-Line Distance


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
The hurricane travels along an infinite straight line determined by
the two locations where it was spotted.

For every city, calculate how close the city is to that line.

The distance from a point (x, y) to the line through
(x1, y1) and (x2, y2) is:

    |(y2-y1)x - (x2-x1)y + x2*y1 - y2*x1|
    ------------------------------------------------
         sqrt((y2-y1)^2 + (x2-x1)^2)

The denominator is the same for every city in the same test case,
so we only need to compare the numerator.

Keep track of the smallest value found.
If multiple cities have the same value, they are equally close to
the hurricane path and must all be printed.


Notes:
The hurricane path is an infinite line, not just the segment between
the two given hurricane positions.

Using only the numerator avoids floating-point precision problems when
checking if two cities are exactly the same distance from the path.

Time complexity: O(M) per test case
Memory complexity: O(M) in the worst case for tied cities
"""

import sys


def main():
    input = sys.stdin.buffer.readline

    test_cases = int(input())

    for _ in range(test_cases):
        x1, y1, x2, y2 = map(int, input().split())

        cities = int(input())

        # These values come from the point-to-line distance formula.
        #
        # The line can be written as:
        #
        # A*x + B*y + C = 0
        A = y2 - y1
        B = -(x2 - x1)
        C = x2 * y1 - y2 * x1

        best_distance = None
        answer = []

        for _ in range(cities):
            data = input().split()

            name = data[0].decode()
            x = int(data[1])
            y = int(data[2])

            # Actual perpendicular distance would be:
            #
            # abs(A*x + B*y + C) / sqrt(A^2 + B^2)
            #
            # The denominator is identical for every city,
            # so comparing just the numerator gives the same result.
            distance = abs(A * x + B * y + C)

            # Found a city closer than every city seen so far.
            if best_distance is None or distance < best_distance:
                best_distance = distance
                answer = [name]

            # Same distance means both cities are in equal danger.
            # Keep them in input order as required by the problem.
            elif distance == best_distance:
                answer.append(name)

        print(" ".join(answer))


main()
