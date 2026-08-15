class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        j=0
        maxi =0
        i = 0
        while i < len(s):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

            while freq[s[i]]>1:
                freq[s[j]] -= 1
                j+=1
            maxi = max(maxi,i-j+1)
            i+=1
        return maxi