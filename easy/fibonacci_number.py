"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
"""

from typing import List

class Solution:
    def fib(self, n: int) -> int:
        return self.__fibo_dp(n, [-1]*(n+1))
        
    def __fibo_dp(self, n : int, mem: List[int]) -> int:
        # base cases
        if n == 0:
            return n
        if n <= 2:
            return 1
        
        # return the output if it has already been computed
        if mem[n] != -1:
            return mem[n]
        
        # compute and store the output in the memoization
        mem[n] = self.__fibo_dp(n-1,mem) + self.__fibo_dp(n-2,mem)
        return mem[n]
    
# 1 1 2 3 5 8 13 21 34 55 89 144
    
s = Solution()

for i in range(15):
    print("i: ", s.fib(i))
        