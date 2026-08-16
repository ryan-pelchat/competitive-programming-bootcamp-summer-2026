"""
Problem Title: Texas Summers
Platform: Kattis
Problem URL: https://open.kattis.com/problems/texassummers
Difficulty: Medium
Categories: Graphs, Dijkstra, Shortest Path, Path Reconstruction


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Treat every shady spot as a vertex in a graph.

Also add:
- The dormitory as the source vertex.
- The classroom as the destination vertex.

Every point can connect directly to every other point, so the graph
is complete.

The weight between two points is their squared Euclidean distance:

    (x1 - x2)^2 + (y1 - y2)^2

Run Dijkstra's algorithm from the dormitory to the classroom.

Keep a parent array so that once the shortest path is found, we can
work backwards from the classroom and determine which shady spots
were used.


Notes:
The graph is complete, so we do not need to store an adjacency list.
Instead, when Dijkstra visits a vertex, we calculate its edge to every
other vertex.

The shady spots are numbered 0 through n - 1 in the same order they
appear in the input.

Time complexity: O(V^2 log V)
Memory complexity: O(V + priority queue)
"""

import sys
from heapq import heappush, heappop


def main():
    input = sys.stdin.buffer.readline

    INF = float("inf")

    n = int(input())

    points = []

    # Shady spots are stored first.
    # Their indices 0, 1, ..., n-1 are also the indices
    # that Kattis expects us to print.
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    # The last two points are the dorm and classroom.
    dorm = tuple(map(int, input().split()))
    classroom = tuple(map(int, input().split()))

    points.append(dorm)
    points.append(classroom)

    V = n + 2

    # Source is the dorm, destination is the classroom.
    s = n
    target = n + 1

    # Modified Dijkstra's routine.
    #
    # dist[u] stores the shortest distance found
    # from the dorm to vertex u.
    dist = [INF for u in range(V)]
    dist[s] = 0

    # parent[v] stores the vertex used immediately
    # before v on the shortest path.
    parent = [-1 for u in range(V)]

    pq = []
    heappush(pq, (0, s))

    # Sort pairs by non-decreasing distance from s.
    while len(pq) > 0:
        d, u = heappop(pq)  # shortest unvisited u

        # There may be an older, worse copy of u in the heap.
        if d > dist[u]:
            continue

        # Once the classroom is removed from the heap,
        # its shortest path is finalized.
        if u == target:
            break

        x1, y1 = points[u]

        # Normally the textbook code would use:
        #
        # for v, w in AL[u]:
        #
        # But this graph is complete, so every other point
        # is a neighbour of u. We calculate each edge here
        # instead of storing millions of edges.
        for v in range(V):

            if u == v:
                continue

            x2, y2 = points[v]

            # Squared Euclidean distance between u and v.
            w = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

            # If travelling through u does not improve
            # the shortest path to v, skip it.
            if dist[u] + w >= dist[v]:
                continue

            # Relax operation.
            dist[v] = dist[u] + w

            # Remember how we reached v so that we can
            # reconstruct the path later.
            parent[v] = u

            heappush(pq, (dist[v], v))

    # ------------------------------------------------------------
    # Reconstruct the shortest path
    # ------------------------------------------------------------

    path = []

    # Start one step before the classroom.
    current = parent[target]

    # Follow parent pointers until we reach the dorm.
    while current != s:

        # Anything before index n is a shady spot.
        path.append(current)

        current = parent[current]

    # We found the path backwards:
    #
    # classroom -> ... -> dorm
    #
    # Reverse it so the shady spots are in the order visited.
    path.reverse()

    # If no shady spots were needed, the best path was
    # directly from the dorm to the classroom.
    if len(path) == 0:
        print("-")

    else:
        # Kattis wants each shady spot index on its own line.
        for spot in path:
            print(spot)


main()
