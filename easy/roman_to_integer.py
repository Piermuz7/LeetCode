
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
def romanToInt(s: str) -> int:
    n = 0
    skip = False
    for i, c in enumerate(s):
        if skip:
            skip = not skip
            continue
        if c == "I":
            if (i+1) < len(s):
                if s[i+1] == "V":
                    n += 4
                    skip = True
                elif s[i+1] == "X":
                    n += 9
                    skip = True
                else:
                    n += 1
                    skip = False
            else:
                n += 1
                skip = False
        elif c == "V":
            n += 5
            skip = False
        elif c == "X":
            if (i+1) < len(s):
                if s[i+1] == "L":
                    n += 40
                    skip = True
                elif s[i+1] == "C":
                    n += 90
                    skip = True
                else:
                    n += 10
                    skip = False
            else:
                n += 10
                skip = False
        elif c == "L":
            n += 50
            skip = False
        elif c == "C":
            if (i+1) < len(s):
                if s[i+1] == "D":
                    n += 400
                    skip = True
                elif s[i+1] == "M":
                    n += 900
                    skip = True
                else:
                    n += 100
                    skip = False
            else:
                n += 100
                skip = False
        elif c == "D":
            n += 500
            skip = False
        elif c == "M":
            n += 1000
            skip = False
    return n