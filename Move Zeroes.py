class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tar = 0
        for dest in range(len(nums)):
            if nums[dest] != 0 and nums[tar] == 0:
                nums[tar], nums[dest] = nums[dest], nums[tar]

            if nums[tar] != 0:
                tar += 1