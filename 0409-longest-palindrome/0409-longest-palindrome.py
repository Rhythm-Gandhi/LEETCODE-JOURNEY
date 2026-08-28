class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0)+1

        ans = 0
        has_odd = False
        for count in freq.values():
            if count%2 ==0:
                ans += count 
            else:
                ans += count -1
                has_odd = True 
        if has_odd :
            ans += 1

        return ans


        