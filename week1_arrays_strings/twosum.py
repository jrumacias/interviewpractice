def twoSum(nums, target):
    seen_dict = {}

    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen_dict:
            print([seen_dict[difference], i])
            return [seen_dict[difference], i]
        seen_dict[num] = i
    return []


twoSum([3, 2, 3], 6)