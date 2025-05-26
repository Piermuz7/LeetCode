"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0 and len(b) == 0:
            return ""
        if len(a) == 0:
            a = "0"
        if len(b) == 0:
            b = "0"
        if a[-1] == "1" and b[-1] == "1":
            return self.addBinary(self.addBinary("1",a[:-1]),b[:-1]) + "0"
        elif a[-1] == "0" and b[-1] == "0":
            return self.addBinary(a[:-1],b[:-1]) + "0"
        elif a[-1] == "0" and b[-1] == "1" or a[-1] == "1" and b[-1] == "0":
            return self.addBinary(a[:-1],b[:-1]) + "1"
        else:
            return "0"
        
s = Solution()

print(s.addBinary("1010","1011"))

# 111 = 7
# 110 = 6

# 1101 = 13