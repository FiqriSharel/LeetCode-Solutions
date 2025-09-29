# Problem 9

class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversedHalf = 0    
        while x > reversedHalf:
            reversedHalf = reversedHalf * 10 + x % 10
            x //= 10
        
        return x == reversedHalf or x == reversedHalf // 10


        
