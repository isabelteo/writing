class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[1,2,3,4,5] with k = 3
        shift_num = k % len(nums)
        #[3,4,5]
        start_values = nums[len(nums) - shift_num: len(nums)]
        #[1,2]
        end_values = nums[:len(nums)-shift_num]
        nums[:shift_num] = start_values
        nums[shift_num:] = end_values
        #return [3,4,5,1,2]