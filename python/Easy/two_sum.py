# Brute force - O(n2)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


#Dict using enumerate
class Solution(object):
    def twoSum(self, nums, target):
        lookup_table = {}
        for index, num in enumerate(nums):
            req_num = target - num
            if req_num in lookup_table:
                return [lookup_table[req_num], index]
            lookup_table[num] = index