#!/usr/bin/python3
"""
You have n number of locked boxes in front of you
Each box is numbered sequentially from 0 to n - 1
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened
    """
    if not boxes or type(boxes) is not list:
        return False
    unLocked = [0]
    for n in unLocked:
        for key in boxes[n]:
            if key not in unLocked and key < len(boxes):
                unLocked.append(key)
    if len(unLocked) == len(boxes):
        return True
    return False
