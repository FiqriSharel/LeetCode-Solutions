# Problem 643

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Firstly, find the sum of the first kth element in the array (ensuring its subarray form)
        groupedSum = sum(nums[:k]) 
        maxSum = groupedSum

        # moving the subarray to the right by adding the next element and substracting the the left element to the calculated sum
        for i in range (k, len(nums)):
            groupedSum += nums[i] - nums[i-k]
            maxSum = max(maxSum, groupedSum)

        return float(maxSum)/k            
