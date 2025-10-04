# Problem 13

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        nums = list(s)
        integer = 0
        for i in range (len(nums)):
            first = nums[i]
            
            if i < len(nums) - 1 and roman[first] < roman[nums[i+1]]:
                integer -= roman[first]
            else:
                integer += roman[first]
       
            # if roman[first] < roman[second]:
            #     newRom = roman[second] - roman[first]
            #     integer += newRom
            # else:
            #     integer += roman[first]
        
        return integer
