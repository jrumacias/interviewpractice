#TODO: Add edge case coverage

def move_duplicates(nums):
    ptr1 = 0
    ptr2 = 1
    while ptr2 < len(nums):
        if nums[ptr1] == nums[ptr2]:
            ptr2 += 1
        else:
            ptr1 += 1
            nums[ptr1] = nums[ptr2]
    print(nums)
    return ptr1 + 1

print(move_duplicates([3,3,3,4,4,5,6,6]))
print(move_duplicates([1,1,2,3,3,3,5]))