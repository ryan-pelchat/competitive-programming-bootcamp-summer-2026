"""
Problem Title: flagquiz
Platform: Kattis
Problem URL: https://open.kattis.com/problems/flagquiz
Difficulty: 3.0 Medium
Categories: 2.2 d. Array Manipulation, Harder

Author: Ryan Pelchat
Date Solved (DD-MM-YYYY): 13-08-2026
Language: Python3

Approach:
    - ingest input
    - it is a 2D array
    - Need to compare each answer with every other answer is it feasible?
        - 1 second is 10^8 computations
        - We have 1 second limit
        - 100 max answers, 50 words per answer therefore: 100*100*50=50^5 ok!
    - Check each answer with each other answers then do as the output says in problem
    - Output the alternative that requires the smallest maximum amount of changes
    to be turned into any other answer. If there are several least incongruous alternatives,
    output them all in the same order as in the input.

Notes:
"""

import sys


def countDifferences(ans1, ans2):
    count = 0
    for op1, op2 in zip(ans1, ans2):
        if op1 != op2:
            count += 1
    return count


data = sys.stdin.read().split("\n")

N = int(data[1])
output = []
answers = []

for line in data[2 : N + 2]:
    answers.append(line.split(", "))

lowest = float("inf")
for i1 in range(len(answers)):
    instanceGreatest = float("-inf")
    for i2 in range(len(answers)):
        if i1 != i2 and answers[i1] == answers[i2]:
            instanceGreatest = 0
        else:
            diffTest = countDifferences(answers[i1], answers[i2])
            if diffTest > instanceGreatest:
                instanceGreatest = diffTest
    if instanceGreatest < lowest:
        lowest = instanceGreatest
        output = [", ".join(list(map(str, answers[i1])))]
    elif instanceGreatest == lowest:
        output.append(", ".join(list(map(str, answers[i1]))))

sys.stdout.write("\n".join(output))
