def remove_adjacent_dups(my_word):
    if my_word == "":
        return my_word
    my_stack = []
    for char in my_word:
        if not my_stack:
            my_stack.append(char)
        elif char == my_stack[len(my_stack)-1]:
            my_stack.pop()
        else:
            my_stack.append(char)
    return str(my_stack)

print(remove_adjacent_dups("abbaca"))