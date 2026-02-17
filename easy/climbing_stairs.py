"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

from typing import List

class Solution:        
        
    def climbStairs(self, n: int) -> int:
        return self.__getNumberOfWays(n, [-1]*(n+1))
        
    def __getNumberOfWays(self, n: int, mem: List) -> int: 
        # base case
        if n == 0 or n == 1:
            return 1
        # if the result has been arelady computed
        if mem[n] != -1:
            return mem[n]
        # each n-th stair could be reached either from the (n-1)th or from (n-2)nd one
        mem[n] = self.__getNumberOfWays(n-1,mem) + self.__getNumberOfWays(n-2,mem)
        return mem[n]
        
s = Solution()

#print(s._computeCombinations(2,1))

#print(s.climbStairs(4))

#print(s.climbStairs(3))