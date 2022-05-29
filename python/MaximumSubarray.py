import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarr_sum = 0
        max_sum =  -math.inf
        for num in nums:
            subarr_sum = max(num, subarr_sum + num)
            max_sum = max(subarr_sum, max_sum)
        return max_sum
