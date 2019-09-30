def palindrome_check(my_word):
    p1 = 0
    p2 =len(my_word) - 1

    while p1 <= p2:
        if my_word[p1] != my_word[p2]:
            return False
        p1 += 1
        p2 -= 1

    return True


print(palindrome_check("racecsar"))


