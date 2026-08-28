class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = []
        for i in str(x):
            lst.append(i)
        left = 0
        right = len(lst) -1 
        while left<right:
            if lst[left] != lst[right]:
                return False

            left+=1
            right -= 1
        return True

