#!/usr/bin/python3
"""
Module that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Prototype that determines if all the boxes can be opened.
    """
    size = len(boxes)  # size of the list of boxes.
    checkbox = {}  # dictionary that will contain the boxes that can be opened.
    index = 0  # index of the box that will be checked.

    for keys in boxes:  # for each box in the list of boxes.
        if len(keys) == 0 or index == 0:
            checkbox[index] = -1
        for key in keys:
            if key < size and key != index:
                checkbox[key] = key  # the box is added to the dictionary.
        if len(checkbox) == size:
            return True  # all the boxes can be opened.
        index += 1
    return False
