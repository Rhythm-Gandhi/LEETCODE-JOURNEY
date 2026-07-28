class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0]*26
        for char in s:
            freq[ord(char) - ord("a")] += 1
        mid = ""
        for i in range(26):
            if freq[i]%2 != 0:  
                mid = chr(i+ord('a'))
                break

        left  = ""
        for i in range(26):
            char  = chr(i + ord("a"))
            left += char * (freq[i]//2)

        return left+mid+left[::-1]
