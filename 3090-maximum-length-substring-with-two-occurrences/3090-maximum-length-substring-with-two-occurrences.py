class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        frq = [0]*26
        j= 0
        maxi = 0
        i = 0
        #for i in range(len(s)):
        while i<len(s):
            ind = ord(s[i])-ord('a')
            frq[ind] +=1
                
            while frq[ind]>2:
                frq[ord(s[j])-ord('a')] -=1
                j +=1

            maxi = max(maxi,i-j+1)
            i+=1
        return maxi
