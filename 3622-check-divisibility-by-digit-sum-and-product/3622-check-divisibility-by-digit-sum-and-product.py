class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0 
        prod = 1
        org = n
        while n>0:
            x = n%10
            sum +=x
            prod*=x
            n = n//10

        sum2 = sum+prod
        if org % sum2 == 0:
            return True
        return False

    