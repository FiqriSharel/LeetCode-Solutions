# Problem 20

class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {
            ')' : '(',
            ']' : '[', 
            '}' : '{'
        }

        for elem in s:
            if elem in mapping:
                top = stack.pop() if stack else '!'
                if mapping[elem] != top:
                    return False
                
            else:
                stack.append(elem)
        
        return not stack
                

        
