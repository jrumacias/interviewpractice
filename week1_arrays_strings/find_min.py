# Find min in O(n^2) time
def find_min_n2(nums):
    current_min = 99999999
    for num1 in nums:
        for num2 in nums:
            if num1 < current_min:
                current_min = num1
            elif num2 < current_min:
                current_min = num2
    return current_min

# Find min in O(n) time
def find_min_n(nums):
    current_min = nums[0]
    for num in nums:
        if num < current_min:
            current_min = num
    return current_min


print(find_min_n2([90,63,25,34,54,16,67]))
print(find_min_n([90,63,16,25,34,54,67]))