class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        left_pointer, right_pointer = 0, len(nums) - 1
        # add from the back
        for i in range(len(nums) - 1, -1, -1):
            # if both are equal, then they will be added side by side so still sorted
            left_val, right_val = abs(nums[left_pointer]), abs(nums[right_pointer])
            # then add squared left value to the back since larger
            if left_val > right_val:
                answer[i] = left_val * left_val
                left_pointer += 1
            else:
                answer[i] = right_val * right_val
                right_pointer -= 1

        return answer