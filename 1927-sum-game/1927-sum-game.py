class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        sum_left = 0
        cnt_left = 0
        for i in range(half):
            if num[i] == "?":
                cnt_left += 1
            else:
                sum_left += int(num[i])

        sum_right = 0
        cnt_right = 0
        for i in range(half, n):
            if num[i] == "?":
                cnt_right += 1
            else:
                sum_right += int(num[i])

        if (cnt_left + cnt_right) % 2 != 0:
            return True

        return (sum_left - sum_right) != (cnt_right - cnt_left) * 4.5
            



        '''
        lst = list(num)
        for i in range(len(lst)):
            if lst[i] == '?':
                lst[i] = str(random.randint(0, 9))
        n=len(lst)
        sum1 = 0
        sum2 = 0
        #p1 =[]
        for j in range(0,n//2):
            sum1 +=int(lst[j])
        #p2 =[]
        for k in range(n//2,-1):
            sum2 += int(lst[k])
        if sum1!=sum2:
            return True
        return False'''
