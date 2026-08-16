"""
Problem Title: Imperfect GPS
Platform: Kattis
Problem URL: https://open.kattis.com/problems/imperfectgps
Difficulty: Medium
Categories: Geometry, Simulation, Linear Interpolation


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
First calculate the runner's actual distance by adding the distance
between every pair of consecutive positions.

The GPS records:
- The starting position at time 0
- A position every t seconds
- The final position, even if the ending time is not a multiple of t

A GPS recording may happen between two known positions.
Since the runner moves at constant speed between those positions,
use linear interpolation to calculate where the runner is at that time.

Add the distances between consecutive GPS recordings to get the
distance measured by the GPS.

Finally, calculate the percentage of the actual distance that was lost:

    (actual_distance - gps_distance) / actual_distance * 100


Notes:
Euclidean distance is calculated using math.hypot().

When a GPS recording happens between two known points, the fraction
of the segment completed is:

    (gps_time - start_time) / (end_time - start_time)

Time complexity: O(N + T/t)
Memory complexity: O(N)
"""

import sys
from math import hypot


def distance(x1, y1, x2, y2):
    # Euclidean distance between two points.
    return hypot(x2 - x1, y2 - y1)


def main():
    input = sys.stdin.buffer.readline

    n, interval = map(int, input().split())

    points = []

    for _ in range(n):
        x, y, time = map(int, input().split())
        points.append((x, y, time))

    # ------------------------------------------------------------
    # Calculate the actual distance travelled
    # ------------------------------------------------------------

    actual_distance = 0.0

    for i in range(1, n):
        x1, y1, _ = points[i - 1]
        x2, y2, _ = points[i]

        actual_distance += distance(x1, y1, x2, y2)

    # ------------------------------------------------------------
    # Simulate the GPS recordings
    # ------------------------------------------------------------

    # The GPS always records the starting position.
    previous_x = points[0][0]
    previous_y = points[0][1]

    gps_distance = 0.0

    # The first recording after time 0 happens after one interval.
    gps_time = interval

    # segment tells us which pair of known points the
    # current GPS recording falls between.
    segment = 0

    final_time = points[-1][2]

    # Process all regular GPS recordings before the end of the run.
    while gps_time < final_time:

        # Move forward until gps_time lies between:
        #
        # points[segment] and points[segment + 1]
        while points[segment + 1][2] < gps_time:
            segment += 1

        x1, y1, time1 = points[segment]
        x2, y2, time2 = points[segment + 1]

        # Find how far through this section of the run
        # the runner is at gps_time.
        #
        # Example:
        # start time = 3
        # end time   = 5
        # gps time   = 4
        #
        # ratio = (4 - 3) / (5 - 3) = 0.5
        #
        # So the runner is halfway between the two points.
        ratio = (gps_time - time1) / (time2 - time1)

        # Linearly interpolate the x and y coordinates.
        current_x = x1 + ratio * (x2 - x1)
        current_y = y1 + ratio * (y2 - y1)

        # The GPS assumes the runner travelled in a straight
        # line from the previous recording to this recording.
        gps_distance += distance(previous_x, previous_y, current_x, current_y)

        # This recording becomes the starting point for
        # the next GPS measurement.
        previous_x = current_x
        previous_y = current_y

        gps_time += interval

    # ------------------------------------------------------------
    # Add the final GPS recording
    # ------------------------------------------------------------

    # The GPS always records the final position, even if the
    # final time is not an exact multiple of the interval.
    final_x = points[-1][0]
    final_y = points[-1][1]

    gps_distance += distance(previous_x, previous_y, final_x, final_y)

    # ------------------------------------------------------------
    # Calculate the percentage lost
    # ------------------------------------------------------------

    lost_distance = actual_distance - gps_distance

    percentage_lost = (lost_distance / actual_distance) * 100

    print(percentage_lost)


main()
