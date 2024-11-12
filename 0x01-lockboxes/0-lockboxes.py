#!/usr/bin/python3
''' Lockboxes'''


def canUnlockAll(boxes):
    '''determines if all boxes can be opened
    Returns:
    True: if all boxes are opened
    False: if not all boxes are opened
    '''
    position = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in box:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False
