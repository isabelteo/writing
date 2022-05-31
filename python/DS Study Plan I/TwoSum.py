class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in d: #num is a complement to a number before it in the array
                return [i, d[num]]
            else:
                d[target-num] = i