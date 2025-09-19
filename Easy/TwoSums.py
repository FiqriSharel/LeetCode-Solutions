class Solution(object):
    def twoSum(self, nums, target):
        indices = [0,0]
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
