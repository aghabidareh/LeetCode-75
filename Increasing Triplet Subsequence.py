class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        medium = float('inf')

        for number in nums:
            if number > medium:
                return True

            if number <= smallest:
                smallest = number
            else:
                medium = min(number, medium)

        return False