# [Problem](https://leetcode.com/problems/squares-of-a-sorted-array/)

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Breakdown of Problem

nums is sorted in ascending order and for squared terms: the _most negative and the most positive values will be largest when squared_

Therefore, we should evaluate from the two ends of the array using **two pointers** so O(n) with one pass.

# Python Solution

[From: clarencechee](https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100)
```python
def sortedSquares(self, A):
    answer = [0] * len(A)
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer[r - l] = left * left
            l += 1
        else:
            answer[r - l] = right * right
            r -= 1
    return answer

#with deque

def sortedSquares(self, A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)
```

Note: deque is like a double ended queue

append():- This function is used to insert the value in its argument to the right end of the deque.

appendleft():- This function is used to insert the value in its argument to the left end of the deque.

pop():- This function is used to delete an argument from the right end of the deque.

popleft():- This function is used to delete an argument from the left end of the deque.

# Java Solution

[From: wangzi6147](https://leetcode.com/problems/squares-of-a-sorted-array/discuss/221922/Java-two-pointers-O(N))

```java
class Solution {
    public int[] sortedSquares(int[] A) {
        int n = A.length;
        int[] result = new int[n];
        int i = 0, j = n - 1;
        for (int p = n - 1; p >= 0; p--) { //loop from the back
            if (Math.abs(A[i]) > Math.abs(A[j])) { 
                result[p] = A[i] * A[i];
                i++;
            } else {
                result[p] = A[j] * A[j];
                j--;
            }
        }
        return result;
    }
}
```

# Javascript Solution

[From: bt4r9](https://leetcode.com/problems/squares-of-a-sorted-array/discuss/285251/Javascript-two-pointers-solution)

```javascript
/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortedSquares = function(A) {
    let result = [];
    let l = 0;
    let r = A.length - 1;
    let p = r;

    while (l <= r) {
        if (A[l] ** 2 > A[r] ** 2) {
            result[p--] = A[l++] ** 2;
        } else {
            result[p--] = A[r--] ** 2;
        }
    }
    
    return result;
};
```