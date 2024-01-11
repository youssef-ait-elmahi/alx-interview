#!/usr/bin/python3
"""
This module contains a function that determines if all boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Function to check if all boxes can be opened.

    Parameters:
    boxes (list): A list of lists, where each inner list contains zero
    or more integers representing keys.

    Returns:
    bool: True if all boxes can be opened, else False.
    """

    total_boxes = len(boxes)
    unlocked = [False] * total_boxes
    unlocked[0] = True
    keys = [key for key in boxes[0]]

    while keys:
        key = keys.pop()
        if key < total_boxes and not unlocked[key]:
            unlocked[key] = True
            keys += boxes[key]

    return all(unlocked)
