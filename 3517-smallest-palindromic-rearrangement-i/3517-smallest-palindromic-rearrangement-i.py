class Solution:
    def smallestPalindrome(self, s: str) -> str:
        left = []
        mid = ""
        for code in range(ord("a"), ord("z") + 1):
            char = chr(code)
            count = s.count(char) 
            if count > 0:
                if count % 2 != 0:
                    mid = char 
                left.append(char * (count // 2))
        left_str = "".join(left)
        return left_str + mid + left_str[::-1]