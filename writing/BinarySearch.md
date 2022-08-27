# [Problem](https://leetcode.com/problems/binary-search/)

## Breakdown

The idea is to apply divide-and-conquer. Rather than just looping through the list from start to end to find the target number, we can start in the middle of the sorted list. 

If target is smaller than number in the middle, we should search the left of the array (values smaller than middle). 

Else, if target is larger than the number in the middle, we should search to the right of the array (values larger than middle). 

If the target value is at the middle, we can return the index of middle.

## Code

[Source: cenkay](https://leetcode.com/problems/binary-search/discuss/148840/Python-typical-solutions-beat-100)
```python
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1
```

**Why use l <= r?**

There is a edge case where e.g. nums = [9] and target = 9, then l = 0 and r = 0. If we set the terminating condition of the loop to be l < r, then the loop will not end even though it should (by returning mid immediately).

But, if you define r = len(nums), then you should use l < r as for the same e.g., l = 0 and r = 1.

**How do we know that the condition will not end in an infinite loop?**

E.g. nums = [2,4,6,8,10]

Case 1: target is not inside the array and target is larger/smaller than all the elements
* If target is larger than all elements, then we will keep searching to the right and l > r eventually because l keeps increasing
* If target is smaller than all elements, then we will keep searching to the left and l > r eventually because r keeps decreasing

Case 2: target is not inside the array and target's value is in between elements (such as target = 5 for the e.g.)

In this case:

mid = 2 so nums[mid] = 6 so search left with r = 2 - 1 = 1

mid = 0 so nums[mid] = 2 so search right with l = 1

mid = 1 so nums[mid] = 4 so search right with l = 2 and r = 1 --> l > r --> terminate


### A more succinct Python code with Bisect

[Source: cenkay](https://leetcode.com/problems/binary-search/discuss/148840/Python-typical-solutions-beat-100)
```python
class Solution:
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
```
**What is bisect?**

Locate the insertion point for target in nums to maintain sorted order. 

bisect_left: If target is already present in nums, returns the leftmost index to insert.

bisect_right: If target is already present in nums, returns the rightmost index to insert.

bisect: Is bisect_right

The only condition where bisect_left and bisect_right will return the same result is if the element does exist in the array.

Example: li = [1, 3, 4, 4, 4, 6, 7] [From: GeeksForGeeks](https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/)

The leftmost index to insert, so list remains sorted is  : 2

The rightmost index to insert, so list remains sorted is  : 4

**Why check index < len(nums) and nums[index] == target**

When would index = len(nums) with bisect_left: It would occur when e.g. nums = [1,1,1] and target = 2 then to maintain sorted order we add at index 3, which is = len(nums). So, it occurs when target is the max and does not exist in the array.
> If [1,1,1,2] and target = 2, then target is max but it exists in the array. Then, index = 3, which is smaller than len(nums) = 4

### Take Note of Corner Cases (Java Code)

[Source: qqqzhouhk](https://leetcode.com/problems/binary-search/discuss/151320/concise-Java-solution-beats-100)
```java
    public int search(int[] nums, int target) {
        // corner case
        if (nums == null || nums.length == 0) return -1;
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] > target) right = mid - 1;
            else left = mid + 1;
        }
        return -1;
    }
```



