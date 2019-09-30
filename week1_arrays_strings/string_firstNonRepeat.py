def first_nonrepeat(my_word):
    #edge cases
    my_word = my_word.lower().strip()
    if my_word is None or my_word is "":
        return -1
    if len(my_word) < 2:
        return 0
    #begin work
    char_list = []
    seen = []
    #convert string to array
    for char in my_word:
        char_list.append(char)
    for char in char_list:
        if char in seen:
            seen.remove(char)
        else:
            seen.append(char)
    return char_list.index(seen[0])


print(first_nonrepeat("%%%5"))
#TODO: Use a hashmap instead and then iterate
#       over the string again to return the first
#       non repeat