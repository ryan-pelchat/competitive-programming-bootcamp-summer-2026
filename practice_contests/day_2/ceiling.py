"""
Problem Title: Ceiling Function
Platform: Kattis
Problem URL: https://open.kattis.com/problems/ceiling
Difficulty: Easy
Categories: Binary Search Tree, Trees, Sets, Recursion

Date Solved (DD-MM-YYYY): 16-08-2026
Language: Python3


Approach:
Build a Binary Search Tree for each sequence by inserting the values
in the order they are given.

The actual values in the tree do not matter. We only care about the
shape of the tree.

After building each tree, recursively convert its shape into a tuple.
Trees with the same structure will produce the same tuple.

Store each shape in a set and output the number of unique shapes.


Notes:
A set automatically removes duplicate tree shapes.

In the worst case, inserting into an unbalanced BST takes O(k^2)
for each sequence, which is fast enough for this problem.
"""

import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    # Insert the value using normal BST rules
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
        else:
            insert(root.left, value)

    else:
        if root.right is None:
            root.right = Node(value)
        else:
            insert(root.right, value)


def get_shape(root):
    # None marks an empty child
    if root is None:
        return None

    # Ignore the values and only record the left/right structure
    return (get_shape(root.left), get_shape(root.right))


def main():
    input = sys.stdin.buffer.readline

    n, k = map(int, input().split())

    shapes = set()

    for _ in range(n):
        values = list(map(int, input().split()))

        # First value becomes the root
        root = Node(values[0])

        # Insert the remaining values into the BST
        for value in values[1:]:
            insert(root, value)

        # Store the structure of the tree
        shapes.add(get_shape(root))

    # print(shapes)
    print(len(shapes))


main()
