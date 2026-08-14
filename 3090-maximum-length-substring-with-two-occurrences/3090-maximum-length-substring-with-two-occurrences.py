class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        frq = {}
        j= 0
        maxi = 0
        for i in range(len(s)):
            if s[i] in frq:
                frq[s[i]] += 1
            else:
                frq[s[i]] = 1

            while frq[s[i]]>2:
                frq[s[j]] -=1
                j +=1

            maxi = max(maxi,i-j+1)
        return maxi
