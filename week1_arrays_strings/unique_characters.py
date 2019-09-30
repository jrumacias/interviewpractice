# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def unique_char_check(my_string):
    seen = []
    for char in my_string:
        if char in seen:
            return "Not unique"
        else:
            seen.append(char)
    return "Unique"

print(unique_char_check("abcdefghijklmnopqrstuvwxyz"))
