class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        numss = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i == j  or j==k or k == i:
                        continue
                    if digits[i] == 0 :
                        continue
                    if digits[k]%2 !=0 :
                        continue
                    num = digits[i]*100 + digits[j] * 10 +digits[k]
                    numss.add(num)
        return len(numss)
