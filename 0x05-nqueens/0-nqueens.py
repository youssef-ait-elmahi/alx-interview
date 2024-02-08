#!/usr/bin/python3
""" N Queens problem using backtracking """
import sys


def nqueens(n):
    """ N Queens problem using backtracking """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    queens = [-1] * n

    backtrack(n, 0, queens, solutions)

    for solution in solutions:
        print_solution(solution)


def backtrack(n, depth, queens, solutions):
    """ Backtracking algorithm """
    if depth == n:
        solutions.append(list(queens))
        return

    for i in range(n):
        queens[depth] = i
        if is_valid(queens, depth):
            backtrack(n, depth + 1, queens, solutions)


def is_valid(queens, row):
    """ Check if a queen can be placed in a row """
    for i in range(row):
        if queens[i] == queens[row] or abs(queens[i] - queens[row]) == row - i:
            return False
    return True


def print_solution(solution):
    """ Print the solution """
    formatted_solution = [[i, col] for i, col in enumerate(solution)]
    print(formatted_solution)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

nqueens(n)