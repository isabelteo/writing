# Maximum Area of Island 

## DFS

The key is to use DFS. DFS uses recursion so starting at grid[0][0] when we find '1', we run DFS to search in 4 directions for another 1. But, to prevent redundancy, we can keep a set of spots in the grid that we have visited and only run DFS on spots that are not visited.

Cases where we don't run DFS:
* Out of bounds 
* grid[r][c] = 0 (water)
* (r,c) in visited

As we have to check every value in the grid, this leads to a time complexity of O(mn) where m is rows and n is column with the same space complexity

### [Python Implementation](https://www.youtube.com/watch?v=iJGr1OtmH0c)
![image](https://user-images.githubusercontent.com/83572953/186273870-1a525350-40b1-4312-b5e1-91aea0ee5a06.png)
