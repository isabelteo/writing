# Contain Duplicates

# Problem

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## My solution 

Loop through the array and keep track of counts using a dictionary. The time complexity and space complexity is O(n).

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d:
                return True #a value has appeared twice
            else:
                d[num] = 1 #a value has appeared once
        return False 
```

## Other Python Solutions in Discussion

The idea is that a set will contain the distinct elements of the array. So, if the number of elements in set is same as array then all elements are distinct.

Credits: [airksh](https://leetcode.com/problems/contains-duplicate/discuss/819888/Python-One-Line-Easy)

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False
    
    # TC: O(n)
    # SC: O(n)
```

## Follow Up Questions

Try returning the items that are distinct/not distinct
