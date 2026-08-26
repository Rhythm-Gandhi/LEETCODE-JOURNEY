class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        MAXLEN = 100
        n = len(s)
        minlen = MAXLEN + 1
        lsbs = ""
        n1 = 0
        i = 0
        for j in range(n):
            if s[j] == "0":
                continue
            n1 += 1
            if n1 == k:
                while s[i] == "0":
                    i += 1
                ij_len = j - i + 1
                if ij_len < minlen:
                    minlen = ij_len
                    lsbs = s[i:j+1]
                elif ij_len == minlen:
                    if s[i:j+1] < lsbs:
                        lsbs = s[i:j+1]
                i += 1
                n1 -= 1
        return lsbs
                