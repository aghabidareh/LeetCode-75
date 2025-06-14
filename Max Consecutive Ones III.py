class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n): preSum[i + 1] = preSum[i] + nums[i]

        def getSum(l, r):
            return preSum[r + 1] - preSum[l]

        def binarySearch(start):
            left, right, ans = start, n-1, start - 1
            while left <= right:
                mid = (left + right) >> 1
                size = mid - start + 1
                cntOne = getSum(start, mid)
                if cntOne + k >= size:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        ans = 0
        for i in range(n):
            j = binarySearch(i)
            ans = max(ans, j - i + 1)
        return ans