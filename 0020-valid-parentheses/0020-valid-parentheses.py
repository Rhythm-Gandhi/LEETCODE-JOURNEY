class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        m = { ")":"(","]":"[","}":"{"}
        for char in s:
            if char in m:
                top = stack.pop() if stack else '#'
                if m[char] != top:
                    return  False 
            else:
                stack.append(char)
        return not stack 





        