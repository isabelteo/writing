# [Problem](https://leetcode.com/problems/maximum-subarray/)

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

## My solution

Because the subarray is contiguous in this case, so the key question when looping will be: To start a new list here or to add this number to the current list? 

The factor to decide whether to start a new list is: if the number is >= the current sum + num. 

The reason is because if the number is larger or equal to current sum + num, it means that current sum is pulling the value of num down (e.g. has negatives). e.g. num = 4 and current sum = -3 

If array starts from num, then there is no loss to max_sum regardless since num >= current sum + num 

Thus, we will track two variables: current sum and max sum

### Why track with two variables?

e.g. why not just max_sum = max(num, max_sum+num)

Because using that formula doesn't ensure contiguous subarrays

#### Case Example

e.g. for [5,4,-1,7,8] 

at -1: 
- max_sum = 5+4 not 5+4+(-1)
- at 7: max_sum = 5+4+7 [NOT CONTIGUOUS]

But if use two variables,
- subarr_sum =  --> tracking [5,4,-1] because -1 < 9+(-1) [num < current sum + num]
- max_sum = 9 --> tracking [5,4]

subarr_sum "explores" the possibility of a longer contiguous subarray


## Code

```python
import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarr_sum, max_sum =  0 
        for num in nums:
            subarr_sum = max(num, subarr_sum + num)
            max_sum = max(subarr_sum, max_sum)
        return max_sum
```

## Iteratation of Code

-2: 
- subarr_sum = max(num, subarr_sum + num) = max(-2, 0 + -2) = -2 --> currently [-2]
- max_sum = max(subarr_sum, max_sum) = max(-2,0) = 0 --> currently [-2]

1: 
- subarr_sum = max(num, subarr_sum + num) = max(1, -2+1) = 1 --> restart list so now tracking [1] and not [-2,1]
- max_sum = max(subarr_sum, max_sum) = max(1,0) = 1

-3: subarr = [1] 
- subarr_sum = max(num, subarr_sum + num) = max(-3, 1 + -3) = -2 --> add to the list so now tracking [1,-3]
- max_sum = max(subarr_sum, max_sum) = max(-2,1) = 1 --> max contiguous subarray is currently: [1]
 
4: subarr = [4] max_sum = 4
- subarr_sum = max(num, subarr_sum + num) = max(4, -2+4) = 4 --> restart list so now tracking [4]
- max_sum = max(subarr_sum, max_sum) = max(-2,1) = 1 --> max contiguous subarray is currently: [4]

      
## Other solutions in Python

### Thinking of problem by focusing on negative numbers

[ramineedi](https://leetcode.com/problems/maximum-subarray/discuss/2049244/Python-or-Time-O(n)-or-Space-O(1))
- If all the numbers are negative, return the max num from the input list.
- If a neg num is seen, it should be a part of subarray only if by adding it, the sum of subarray is NOT less than 0.

```python
# Time: O(n), space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum = 0
        max_sum = float('-inf')
        
        for num in nums:
            if curr_sum + num > 0:
                curr_sum += num
                max_sum = max(max_sum, curr_sum)
            else:
                curr_sum = 0
                
        return max_sum if max_sum != float('-inf') else max(nums)
```

[GeeksForGeeks](https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/)

### Divide and Conquer Approach -- To be added soon 
