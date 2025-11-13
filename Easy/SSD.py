def SSD (a, b):
    combination = {
        0: ['a', 'b', 'c', 'd', 'e', 'f'],
        1: ['b', 'c'],
        2: ['a', 'b', 'd', 'e', 'f'],
        3: ['a', 'b', 'c', 'd', 'f'],
        4: ['b', 'c', 'f', 'g'],
        5: ['a', 'c', 'd', 'f', 'g'],
        6: ['a', 'c', 'd', 'e', 'f', 'g'],
        7: ['a', 'b', 'c'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g']
    }

    segA = combination[a]
    segB = combination[b]

    diff = set(segA).symmetric_difference(set(segB))

    return len(diff)

print(SSD(4, 5))  # Example usage
