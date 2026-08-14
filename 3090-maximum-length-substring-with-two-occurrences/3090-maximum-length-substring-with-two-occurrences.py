from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        #frq = [0]*26
        frq = defaultdict(int)
        j= 0
        maxi = 0
        i = 0
        #for i in range(len(s)):
        while i<len(s):
            #ind = ord(s[i])-ord('a')
            frq[s[i]] +=1
                
            while frq[s[i]]>2:
                #frq[ord(s[j])-ord('a')] -=1
                frq[s[j]] -=  1
                j +=1

            maxi = max(maxi,i-j+1)
            i+= 1
        return maxi
