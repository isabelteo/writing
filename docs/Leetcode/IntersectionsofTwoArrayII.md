# Intersection of Two Arrays II

# [Problem](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order

# Examples

NOTE: Output does not have to be in order

* Both arrays have same number of match: [1,1] [1,1] --> [1,1]
* One array has smaller amount for a match: [1,1,1,1] [1,1] --> [1,1]
* No match: [2,2] [1,1] --> []
* At least one is empty: [] [1] --> []
 
# My First Code: Dictionary Method
```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictionary_nums1 = {}
        # keeps track of the counts of distinct values in nums1
        for num in nums1:
            if num in dictionary_nums1:
                dictionary_nums1[num] += 1
            else:
                dictionary_nums1[num] = 1

        result = []

        for num in nums2:
            # match with nums1
            if num in dictionary_nums1 and dictionary_nums1[num] > 0:
                result.append(num)
                dictionary_nums1[num] -= 1
            else:
                continue

        return result
```

# Improvements after viewing [discussion](https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82247/Three-Python-Solutions)

How does Counter work?
* Counter([1,3,4,2,4,3]) --> {1:1,2:1,3:2,4:2} --> returns a dictionary where the value is the key and the value is the count of the key
* Counter([1,3,2,3]).elements() --> [1,2,3,3,4,4]
 
From [pawelsubko](https://leetcode.com/pawelsubko)
```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        return (Counter(nums1) & Counter(nums2)).elements()
```
