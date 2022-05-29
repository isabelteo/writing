class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d:
                return True #a value has appeared twice
            else:
                d[num] = 1 #a value has appeared once
        return False
