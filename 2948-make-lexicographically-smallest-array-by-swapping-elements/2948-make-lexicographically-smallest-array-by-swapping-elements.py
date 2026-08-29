class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = []

        for i in range(n):
            arr.append([nums[i], i])

        arr.sort()

        ans = [0] * n

        start = 0

        while start < n:
            end = start

            while end + 1 < n:
                current = arr[end][0]
                next_value = arr[end + 1][0]

                if next_value - current <= limit:
                    end += 1
                else:
                    break

            indices = []

            for i in range(start, end + 1):
                indices.append(arr[i][1])

            indices.sort()

            k = 0

            for i in range(start, end + 1):
                value = arr[i][0]
                index = indices[k]

                ans[index] = value
                k += 1

            start = end + 1

        return ans