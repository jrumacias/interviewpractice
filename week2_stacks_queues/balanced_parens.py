def is_balanced(parens):
    my_stack = []
    for elem in parens:
        my_stack.append(elem)

    for elem in parens:
        if (elem == '(' and my_stack[-1] == ')') or \
        (elem == ')' and my_stack[-1] == '(') or \
        (elem == '{' and my_stack[-1] == '}') or \
        (elem == '}' and my_stack[-1] == '{') or \
        (elem == '[' and my_stack[-1] == ']') or \
        (elem == ']' and my_stack[-1] == '['):
            my_stack.pop()
        else:
            return False
    return True

def balance_check(s):
    chars = []
    matches = {")":"(", "]":"[", "}":"{"}
    for c in s:
        if c in matches:
            if chars.pop() != matches[c]:
                return False
        else:
            chars.append(c)
    return chars == []


print(balance_check("({[]})"))
