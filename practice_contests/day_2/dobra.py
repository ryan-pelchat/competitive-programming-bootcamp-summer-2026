"""
Problem Title: Dobra
Platform: Kattis
Problem URL: https://open.kattis.com/problems/dobra
Difficulty: Medium
Categories: Recursion, Backtracking

Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Use recursive backtracking to build the word from left to right.

At each position, keep track of:
- The number of consecutive vowels
- The number of consecutive consonants
- Whether an L has appeared

For each underscore, we try three possibilities:
- A vowel: 5 possible letters
- A consonant other than L: 20 possible letters
- The letter L: 1 possibility

If we ever get 3 vowels or 3 consonants in a row,
that branch is invalid and we stop exploring it.

When we reach the end, the word is valid only if it contains an L.


Notes:
This is a pure recursive backtracking solution with no memoization.

Instead of trying all 26 letters for every underscore, letters are grouped
based on whether they are a vowel, a consonant, or L.
"""

import sys

word = sys.stdin.readline().strip()

VOWELS = "AEIOU"


def backtrack(pos, vowels, consonants, has_l):
    # Three vowels or consonants in a row is invalid
    if vowels >= 3 or consonants >= 3:
        return 0

    # Reached the end of the word
    if pos == len(word):
        return 1 if has_l else 0

    char = word[pos]

    if char == "_":
        total = 0

        # Try one of the 5 vowels
        total += 5 * backtrack(pos + 1, vowels + 1, 0, has_l)

        # Try one of the 20 consonants other than L
        total += 20 * backtrack(pos + 1, 0, consonants + 1, has_l)

        # Try L
        total += backtrack(pos + 1, 0, consonants + 1, True)

        return total

    elif char in VOWELS:
        # Fixed vowel
        return backtrack(pos + 1, vowels + 1, 0, has_l)

    else:
        # Fixed consonant
        return backtrack(pos + 1, 0, consonants + 1, has_l or char == "L")


print(backtrack(0, 0, 0, False))
