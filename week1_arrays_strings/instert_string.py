def solution(S, K):
    # write your code in Python 3.6
    my_list = []
    for char in S:
        if char != '-':
            my_list.append(char)
    counter = 1
    for char in my_list[::-1]:
        if counter % K == 0 and my_list.index(char) != 0:
            my_list.insert(my_list.index(char), '-')
        counter += 1
    ret_str = ''.join(my_list)
    ret_str = ret_str.upper()
    return ret_str

print(solution("r", 1))