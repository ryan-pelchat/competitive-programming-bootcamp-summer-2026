"""
Problem Title: Single Source Shortest Path, Non-Negative Weights
Platform: Kattis
Problem URL: https://open.kattis.com/problems/shortestpath1
Difficulty: Medium
Categories: Graphs, Dijkstra, Shortest Path, Priority Queue


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Build an adjacency list for the directed graph.

Run Dijkstra's algorithm once from the given source vertex s.
Since all edge weights are non-negative, Dijkstra will find the
shortest distance from s to every reachable vertex.

After Dijkstra finishes, answer each query using the distance array.

If a queried vertex cannot be reached from s, print "Impossible".

There can be multiple test cases. Input ends when:

    0 0 0 0


Notes:
The graph is directed, so an edge from u to v does not automatically
give us an edge from v to u.

The priority queue stores pairs:

    (distance from s, vertex)

A vertex can appear in the priority queue more than once, so the
check:

    if d > dist[u]: continue

is important for skipping old entries.

Time complexity: O((V + E) log V)
Memory complexity: O(V + E)
"""

import sys
from heapq import heappush, heappop


def main():
    input = sys.stdin.buffer.readline

    # Use a very large number to represent an unreachable vertex.
    INF = int(1e18)

    output = []

    while True:
        V, E, q, s = map(int, input().split())

        # 0 0 0 0 marks the end of the input.
        if V == 0 and E == 0 and q == 0 and s == 0:
            break

        # AL[u] contains all directed edges leaving vertex u.
        #
        # Each edge is stored as:
        # (destination, weight)
        AL = [[] for u in range(V)]

        for _ in range(E):
            u, v, w = map(int, input().split())

            # Directed graph: only add u -> v.
            AL[u].append((v, w))

        # --------------------------------------------------------
        # Dijkstra's algorithm
        # --------------------------------------------------------

        # dist[u] stores the shortest distance currently known
        # from the source s to vertex u.
        dist = [INF for u in range(V)]

        # Distance from the source to itself is always 0.
        dist[s] = 0

        # The priority queue stores:
        # (distance from source, vertex)
        pq = []
        heappush(pq, (0, s))

        # Process vertices in non-decreasing distance from s.
        while len(pq) > 0:
            d, u = heappop(pq)

            # A vertex may appear in the priority queue multiple times.
            #
            # If this distance is worse than the best distance we
            # already know, this is an old entry and can be skipped.
            if d > dist[u]:
                continue

            # Check every edge leaving u.
            for v, w in AL[u]:

                # Going from s -> ... -> u -> v would have
                # this total distance.
                new_distance = dist[u] + w

                # If this does not improve the shortest path
                # to v, there is nothing to update.
                if new_distance >= dist[v]:
                    continue

                # Relax the edge.
                dist[v] = new_distance

                # Add the improved distance to the priority queue.
                heappush(pq, (dist[v], v))

        # --------------------------------------------------------
        # Answer queries
        # --------------------------------------------------------

        for _ in range(q):
            vertex = int(input())

            # INF means Dijkstra never found a path to this vertex.
            if dist[vertex] == INF:
                output.append("Impossible")
            else:
                output.append(str(dist[vertex]))

        # Kattis requires a blank line after each test case.
        output.append("")

    sys.stdout.write("\n".join(output))


main()
