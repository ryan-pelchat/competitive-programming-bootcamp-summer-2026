"""
Problem Title: Classrooms
Platform: Kattis
Problem URL: https://open.kattis.com/problems/classrooms
Difficulty: Medium
Categories: Greedy, Priority Queue, Sorting


Author: Ryan Pelchat
Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Sort all activities by starting time.

Keep track of the activities currently using classrooms.

If more than k activities overlap, remove the activity that ends
the latest. Keeping activities that finish earlier leaves more room
for future activities.

Two priority queues are used:
- A min-heap to find activities that have already finished.
- A max-heap to remove the activity with the latest ending time.

Activities whose ending time equals another activity's starting time
still overlap, so a classroom becomes free only when end < start.


Notes:
Whenever there are more than k overlapping activities, removing the
one with the latest ending time is the best choice because it frees
a classroom as early as possible.

Time complexity: O(n log n)
Memory complexity: O(n)
"""

import sys
import heapq


def main():
    input = sys.stdin.buffer.readline

    n, k = map(int, input().split())

    activities = []

    for i in range(n):
        start, end = map(int, input().split())
        activities.append((start, end, i))

    # Process activities in order of starting time
    activities.sort()

    # Min-heap: earliest ending activity first
    min_heap = []

    # Max-heap: latest ending activity first
    # Python only has a min-heap, so store negative ending times
    max_heap = []

    # status:
    # 0 = removed
    # 1 = currently active
    # 2 = finished and accepted
    status = [0] * n

    active = 0
    accepted = 0

    for start, end, index in activities:

        # Remove activities that finished before this one starts
        while min_heap and min_heap[0][0] < start:
            old_end, old_index = heapq.heappop(min_heap)

            if status[old_index] == 1:
                status[old_index] = 2
                active -= 1

        # Tentatively accept this activity
        status[index] = 1

        heapq.heappush(min_heap, (end, index))
        heapq.heappush(max_heap, (-end, index))

        active += 1
        accepted += 1

        # Too many activities are using classrooms
        if active > k:

            # Remove the active activity that ends the latest
            while max_heap:
                neg_end, remove_index = heapq.heappop(max_heap)

                if status[remove_index] == 1:
                    status[remove_index] = 0
                    active -= 1
                    accepted -= 1
                    break

    print(accepted)


main()
