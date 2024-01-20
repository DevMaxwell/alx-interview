#!/usr/bin/python3
'''A module for lockboxes.
'''


def canUnlockAll(boxes):
    '''You have n number of locked boxes in front of you. Each box is numbered sequentially
    from 0 to n - 1 and each box may contain keys to the other boxes.
    Write a method that determines if all the boxes can be opened.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
    