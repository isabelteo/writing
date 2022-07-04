class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #let l point to 0 and r point to non-zero to swap non-zero to the left of arr
        l = 0
        for r in range(len(nums)):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], 0
            if nums[l] != 0:
                l += 1
        #if all 0, then R pointer goes ahead while L pointer stays
        #if all non-0, then L pointer goes same pace with R pointer
        # so L pointer is always <= R