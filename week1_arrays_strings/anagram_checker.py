def anagram(s, t):
    if s is None or t is None:
        return False
    if len(s) != len(t):
        return False

    for s_char in s:
        if s_char not in t:
            return False

    return True

print(anagram("this", ""))