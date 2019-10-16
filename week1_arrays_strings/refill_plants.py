def refill_plants(plants, capacity1, capacity2):
    # write your code in Python 3.6
    c1 = capacity1
    c2 = capacity2
    p1 = 0
    p2 = len(plants) - 1
    refill_count = 2

    while p1 <= p2 and p2 >= p1:
        if p1 == p2:
            if (c1 + c2) < plants[p2]:
                refill_count += 1
                return refill_count
            else:
                return refill_count

        if c1 >= plants[p1]:
            c1 -= plants[p1]
        elif c1 < plants[p1]:
            refill_count += 1
            c1 = capacity1
            c1 -= plants[p1]

        if c2 >= plants[p2]:
            c2 -= plants[p2]
        elif c2 < plants[p2]:
            refill_count += 1
            c2 = capacity2
            c2 -= plants[p2]
        p1 += 1
        p2 -= 1

    return refill_count

print(refill_plants([2, 4, 5, 1, 2], 5, 7))