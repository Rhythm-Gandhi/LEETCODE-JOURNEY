class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        pres = 0
        loop = 1 + l//8
        for i in range(1,loop):
            pres += i*8
        pres += loop * (l%8)

        return pres
