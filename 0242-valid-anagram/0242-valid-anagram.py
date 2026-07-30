class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        count ={}
        for i in s:
            if i in count:
                count[i] = count[i]+1
            else:
                count[i] = 1
        for i in t:
            if i not in count:
                return False
            count[i] = count[i]-1
            if count[i] <0:
                return False
        return True

