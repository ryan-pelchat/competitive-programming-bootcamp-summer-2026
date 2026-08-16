"""
Problem Title: Fenwick Tree
Platform: Kattis
Problem URL: https://open.kattis.com/problems/fenwick
Difficulty: Medium
Categories: Fenwick Tree, Prefix Sums, Data Structures


Author: Ryan Pelchat
Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Use a Fenwick Tree to efficiently process updates and prefix sum queries.

The Fenwick Tree uses 1-based indexing, while the Kattis problem uses
0-based indexing. Therefore, update index i in Kattis becomes i + 1
inside the Fenwick Tree.

For "? i", Kattis asks for the sum of elements from index 0 up to
but not including index i. In the 1-based Fenwick Tree, this is
equivalent to querying positions 1 through i.


Notes:
Both update and query operations take O(log n) time.
The Fenwick Tree uses O(n) memory.
"""

import sys


class FTree:
    def __init__(self, f):
        self.n = len(f)
        self.ft = [0] * (self.n + 1)

        # Build the Fenwick Tree from the initial array
        for i in range(1, self.n + 1):
            self.ft[i] += f[i - 1]

            parent = i + self.lsone(i)

            if parent <= self.n:
                self.ft[parent] += self.ft[i]

    # Returns the value of the least significant set bit
    def lsone(self, s):
        return s & (-s)

    # Returns the sum from index i to j
    def query(self, i, j):
        # Range query using two prefix sums
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)

        s = 0

        # Move upward through the Fenwick Tree
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)

        return s

    # Add v to position i
    def update(self, i, v):
        while i <= self.n:
            self.ft[i] += v
            i += self.lsone(i)

    # Finds the smallest index whose prefix sum is at least k
    # Not needed for this problem, but part of the FTree library
    def select(self, k):
        p = 1

        while (p * 2) <= self.n:
            p *= 2

        i = 0

        while p > 0:
            if i + p <= self.n and k > self.ft[i + p]:
                k -= self.ft[i + p]
                i += p

            p //= 2

        return i + 1


def main():
    input = sys.stdin.buffer.readline

    n, q = map(int, input().split())

    # The array starts entirely filled with zeroes
    ft = FTree([0] * n)

    output = []

    for _ in range(q):
        command = input().split()

        if command[0] == b"+":
            index = int(command[1])
            value = int(command[2])

            # Kattis uses 0-based indexing.
            # Our Fenwick Tree uses 1-based indexing.
            ft.update(index + 1, value)

        else:
            index = int(command[1])

            # "? i" asks for A[0] + A[1] + ... + A[i - 1].
            # This corresponds to positions 1 through i
            # in our 1-based Fenwick Tree.
            output.append(str(ft.query(1, index)))

    sys.stdout.write("\n".join(output))


main()
