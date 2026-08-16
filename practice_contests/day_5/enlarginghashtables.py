"""
Problem Title: Enlarging Hash Tables
Platform: Kattis
Problem URL: https://open.kattis.com/problems/enlarginghashtables
Difficulty: Easy
Categories: Number Theory, Prime Numbers, Prime Testing


Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
For each value n, find the smallest prime number strictly greater
than 2 * n.

Start checking from:

    2 * n + 1

and continue until a prime number is found.

We also need to check whether the original value n is prime.
If it is not, print:

    (n is not prime)

after the new hash table size.


Notes:
To test whether a number is prime, we only need to try divisors
up to sqrt(n).

After checking divisibility by 2, we only need to test odd divisors.

Input ends when n = 0.

Prime test complexity: O(sqrt(n))
Memory complexity: O(1)
"""

import sys
from math import isqrt


def is_prime(n):
    # Numbers below 2 are not prime.
    if n < 2:
        return False

    # 2 is the only even prime number.
    if n == 2:
        return True

    # Any other even number is composite.
    if n % 2 == 0:
        return False

    # If n has a factor larger than sqrt(n),
    # it must also have a factor smaller than sqrt(n).
    limit = isqrt(n)

    # We already checked divisibility by 2,
    # so only test odd possible factors.
    for divisor in range(3, limit + 1, 2):
        if n % divisor == 0:
            return False

    return True


def main():
    input = sys.stdin.buffer.readline

    while True:
        n = int(input())

        # A single 0 marks the end of the input.
        if n == 0:
            break

        # The new hash table must be larger than twice
        # the size of the current table.
        candidate = 2 * n + 1

        # Except for 2, prime numbers are odd.
        # 2*n + 1 is already odd, so we can check
        # only odd candidates by increasing by 2.
        while not is_prime(candidate):
            candidate += 2

        # Print the new prime hash table size first.
        if is_prime(n):
            print(candidate)

        else:
            print(f"{candidate} ({n} is not prime)")


main()
