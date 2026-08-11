class Solution:
    def missingInteger(self, A: list[int]) -> int:
        n = len(A)
        sen = set(A)
        sum = A[0]
        for j in range(1,n):
            if A[j] == A[j-1]+1:
                sum+=A[j]
            else:
                break

        while sum in A:
            sum +=1

        return sum
