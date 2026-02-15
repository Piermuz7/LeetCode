"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        v = []
        prev = [1,1]
        for i in range(0,numRows):
            if i < 2:
                v.append([1]*(i+1))
            else:
                tmp = []
                for j in range(1, len(prev)):
                    if j == len(prev) - 1:
                        tmp.append(prev[len(prev) - 2] + 1)
                    else:
                        tmp.append(prev[j - 1] + prev[j])
                tmp.insert(0,1)
                tmp.append(1)
                v.insert(i,tmp)
                prev = tmp.copy()
        return v
            
            
s = Solution()
print(s.generate(5))