def canUnlockAll(boxes):
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
