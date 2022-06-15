#isBadVersion was considered to be provided

class Solution:
    def firstBadVersion(self, n: int) -> int:
        earliestBadVersion = 0
        start, end = 1,n
        while start <= end:
            mid = (start+end)//2
            if isBadVersion(mid):
                #there is a bad version to the left
                earliestBadVersion = mid
                end = mid - 1
            else:
                #there COULD be a bad version to the right
                start = mid + 1
        return earliestBadVersion