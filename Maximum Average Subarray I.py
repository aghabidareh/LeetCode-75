class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsum=sum(nums[:k])
        maxsum=windowsum
        for i in range(k,len(nums)):
            windowsum=windowsum-nums[i-k]+nums[i]
            maxsum=max(maxsum,windowsum)
        maxavg=maxsum/k
        return maxavg