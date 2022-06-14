class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:  # search to the right
                start = mid + 1
            elif nums[mid] > target:  # search to the left
                end = mid - 1
            else:
                return mid
        return -1

