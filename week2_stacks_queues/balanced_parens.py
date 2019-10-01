def is_balanced(parens):
    my_stack = []
    for elem in parens:
        my_stack.append(elem)
    my_dict = {"[":"]", "]":"[", "(":")", ")":"(", "{":"}", "}":"{"}

    for elem in parens:
        ## TODO: implement


print(is_balanced("({[]})"))
