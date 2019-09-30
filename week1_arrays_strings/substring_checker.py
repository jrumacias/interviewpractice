def substring_checker(substring, my_string):
    if len(substring) < 1 or len(my_string) < 1 \
            or len(substring) > len(my_string):
        return -1
    ptr1 = 0
    ptr2 = 0
    for i, char in enumerate(my_string):
        if char == substring[0]:
            ptr1 = i
            ptr2 = ptr1
            for char2 in substring:
                if char2 == my_string[ptr2]:
                    ptr2 += 1
                else:
                    ptr2 = ptr1
            if ptr2 - ptr1 == len(substring):
                return ptr1
    return -1




print(substring_checker("for", "folksforgeeks"))
                