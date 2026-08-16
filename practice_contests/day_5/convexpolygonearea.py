"""
Problem Title: Convex Polygon Area
Platform: Kattis
Problem URL: https://open.kattis.com/problems/convexpolygonarea
Difficulty: Easy
Categories: Geometry, Polygons, Shoelace Formula


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Use the Shoelace Formula to calculate the area of each polygon.

For every pair of consecutive vertices:

    (x1, y1)
    (x2, y2)

add:

    x1 * y2 - y1 * x2

The last vertex must also connect back to the first vertex.

After adding all of these values, take the absolute value and
divide by 2 to get the polygon's area.


Notes:
The vertices are already given in order around the polygon, so we
can apply the Shoelace Formula directly.

The sum before dividing by 2 is sometimes called twice the area.

Time complexity: O(N) per polygon
Memory complexity: O(N)
"""

import sys


def main():
    input = sys.stdin.buffer.readline

    test_cases = int(input())

    for _ in range(test_cases):

        # Each polygon is given on one line:
        #
        # n x1 y1 x2 y2 ... xn yn
        values = list(map(int, input().split()))

        n = values[0]

        points = []

        # Convert the coordinate values into (x, y) pairs.
        for i in range(n):
            x = values[1 + 2 * i]
            y = values[2 + 2 * i]

            points.append((x, y))

        # area2 stores twice the signed area.
        #
        # We wait until the end to divide by 2.
        area2 = 0

        for i in range(n):
            x1, y1 = points[i]

            # The modulo makes the last vertex connect
            # back to the first vertex.
            x2, y2 = points[(i + 1) % n]

            # Shoelace Formula contribution from this edge.
            area2 += x1 * y2 - y1 * x2

        # Depending on whether the vertices are clockwise or
        # counter-clockwise, area2 may be negative.
        area2 = abs(area2)

        # Since all coordinates are integers, the final area
        # will end in either .0 or .5.
        if area2 % 2 == 0:
            print(f"{area2 // 2}.0")
        else:
            print(f"{area2 // 2}.5")


main()
