class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)
        
        halfCount = [0] * 26
        midLetter = ''
        for c, freq in count.items():
            halfCount[ord(c) - ord('a')] = freq // 2
            if freq % 2 == 1:
                midLetter = c

        MAX_K = 10**6 + 1

        def nCk(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            res = 1
            for i in range(1, min(r, n - r) + 1):
                res = res * (n - i + 1) // i
                if res >= MAX_K:
                    return MAX_K
            return res

        def countArrangements(counts: list[int]) -> int:
            total = sum(counts)
            res = 1
            for freq in counts:
                if freq > 0:
                    res *= nCk(total, freq)
                    if res >= MAX_K:
                        return MAX_K
                    total -= freq
            return res

        if k > countArrangements(halfCount):
            return ""

        halfLen = sum(halfCount)
        leftHalf = []

        for _ in range(halfLen):
            for i in range(26):
                if halfCount[i] == 0:
                    continue
                halfCount[i] -= 1
                arrangements = countArrangements(halfCount)
                if arrangements >= k:
                    leftHalf.append(chr(i + ord('a')))
                    break
                else:
                    k -= arrangements
                    halfCount[i] += 1

        first_half = "".join(leftHalf)
        return first_half + midLetter + first_half[::-1]