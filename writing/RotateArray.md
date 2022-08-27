# [Problem](https://leetcode.com/problems/rotate-array/)

Given an array, rotate the array to the right by k steps, where k is non-negative.

# Code

Source: [jedihy](https://leetcode.com/problems/rotate-array/discuss/54426/Summary-of-solutions-in-Python)

E.g. nums = [1,2,3,4,5] and k = 3 so nums[:] = nums[5-3:] + nums[:5-3] = nums[2:] + nums[:2] = [3,4,5] + [1,2]

```python
# O(n) space solution
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
```

E.g. nums = [1,2,3,4,5] and k = 3 so output should be [3,4,5,1,2]

numReverse(0,n-1) --> [5,4,3,2,1] --> shifted by n

numReverse(0,k-1) --> numReverse(0,2) --> [3,4,5,2,1]

numReverse(k,n-1) --> numReverse(3,4) --> [3,4,5,1,2]

The key idea here is to understand e.g. [1,2,3,4,5] and k = 3, we want to shift [3,4,5] to the start and [1,2] to the back and we can treat them as seperate

So, to bring the numbers closer to their final position, I can do a full reversal of the array. For e.g. [1,2,3,4,5] to [5,4,3,2,1]

Then, I swap the values to their correct position by reversing within [5,4,3] and [2,1]

```python
# O(1) space solution
class Solution:
    def rotate(self, nums, k):
        def numReverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k, n = k % len(nums), len(nums)
        if k:
            numReverse(0, n - 1)
            numReverse(0, k - 1)
            numReverse(k, n - 1)
```

# Bonus: What if k is negative?

Source:[hi-malik](https://leetcode.com/problems/rotate-array/discuss/1730142/JavaC%2B%2BPython-A-very-very-well-detailed-explanation)

If k = 1, then e.g. nums = [1,2,3,4,5] --> [5,1,2,3,4] --> shift last value to the front

If k = -1, then e.g. nums = [1,2,3,4,5] --> [2,3,4,5,1] --> shift first value to the back

Another way of understanding this is that k = -1 means k = len(nums) + abs(-1). Then, we can apply the same approach.