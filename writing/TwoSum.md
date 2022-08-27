# [Problem](https://leetcode.com/problems/two-sum/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:  nums = [2,7,11,15], target = 9 then return [0,1] because 2+7 = 9

# Idea

The idea is to look out for the complement. So, we store the complement as a key in a dictionary (called d here) and have the value be the index of num because we are returning indices in a list.

As we continue to loop through the list and get new nums, we check if num is a complement for any number before it by checking if num is a key in the dictionary. If num is a complement, we have found a pair and return the index of num and the index stored as value in d[num]. If not, we add its complement (target - num) into the dictionary as a key.

# Code 

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in d: #num is a complement to a number before it in the array
                return [i, d[num]]
            else:
                d[target-num] = i
```

# Time Complexity

Time: O(n)
Space: O(1)