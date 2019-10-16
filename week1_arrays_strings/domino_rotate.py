def rotate(A, B):
    # write your code in Python 3.6
    a_dict = {}
    b_dict = {}
    swap_count = 0
    a_key = -1
    b_key = -1

    # count instances in A and B
    for num in A:
        if num in a_dict:
            a_dict[num] += 1
        else:
            a_dict[num] = 1
    for num in B:
        if num in b_dict:
            b_dict[num] += 1
        else:
            b_dict[num] = 1
    # get the max appearances from each dictionary
    a_max_appearances = -1
    b_max_appearances = -1
    for k, v in a_dict.items():
        if v > a_max_appearances:
            a_max_appearances = v
            a_key = k
    for k, v in b_dict.items():
        if v > b_max_appearances:
            b_max_appearances = v
            b_key = k

    if a_max_appearances >= b_max_appearances and a_max_appearances >= len(A) / 2:
        # max key is in A
        for i, num in enumerate(A):
            if num != a_key:
                # check if B[i] == a_max
                if B[i] == a_key:
                    swap_count += 1
                else:
                    return -1
    elif b_max_appearances >= a_max_appearances and b_max_appearances >= len(A) / 2:
        # max key is in B
        for i, num in enumerate(B):
            if num != b_key:
                # check if B[i] == a_max
                if A[i] == b_key:
                    swap_count += 1
                else:
                    return -1
    else: return -1 #no sufficient key
    return swap_count

print(rotate([1, 2, 3, 6, 3, 2], [2, 1, 2, 2, 2, 4]))