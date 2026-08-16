"""
Problem Title: Reseto
Platform: Kattis
Problem URL: https://open.kattis.com/problems/reseto
Difficulty: Easy
Categories: Number Theory, Prime Numbers, Sieve of Eratosthenes, Simulation


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Simulate the Sieve of Eratosthenes exactly as described in the problem.

Start with all numbers from 2 to N marked as not crossed out.

Beginning at 2:
- Find the smallest number that has not been crossed out.
- Cross out that number and all of its multiples that are still available.
- Count each number as it is crossed out.

As soon as we cross out the K-th number, print it and stop.


Notes:
A number should only be counted the first time it is crossed out.

For example, 6 is first crossed out as a multiple of 2.
When we later process 3, we do not count 6 again.

Time complexity: O(N log log N) for the sieve process.
Memory complexity: O(N)
"""

import sys


def main():
    input = sys.stdin.buffer.readline

    n, k = map(int, input().split())

    # crossed[i] tells us whether i has already
    # been removed by the sieve.
    crossed = [False] * (n + 1)

    # Count how many numbers have been crossed out so far.
    count = 0

    # Try every possible prime candidate starting from 2.
    for p in range(2, n + 1):

        # If p was already crossed out, then it is not the
        # next prime and we can skip it.
        if crossed[p]:
            continue

        # Cross out p and all of its multiples.
        #
        # We start at p itself because the problem counts
        # the prime number as being crossed out too.
        for multiple in range(p, n + 1, p):

            # A number may already have been crossed out
            # by a smaller prime.
            if crossed[multiple]:
                continue

            crossed[multiple] = True
            count += 1

            # As soon as we reach the K-th crossed number,
            # we have found the answer.
            if count == k:
                print(multiple)
                return


main()
