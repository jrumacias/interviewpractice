def reverseQueue(q):
    if not q:
        return q
    my_q = []
    for elem in q[::-1]:
        my_q.append(q.popleft())
    return my_q

print(reverseQueue([4,3,1,10,2,6]))