/*
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
*/
#include<stdio.h>
#include<stdlib.h>

char* longestCommonPrefix(char **strs, int strsSize)
{
    char* lcp = (char*)malloc(200);
    if (strsSize == 0)
        return "";
    if (strsSize == 1)
        return strs[0];
    int i = 0, j = 0, k = 0;
    while(strs[i][j] != '\0' && k == 0)
    {
        if(i < strsSize - 1){
            if(strs[i][j] == strs[i+1][j] && k == 0){
                lcp[j] = strs[i][j];
                i++;
            }
            else{
                k = 1;
                lcp[j] = '\0';
            }
        }
        else
        {
            i = 0;
            j++;
        }
    }
    lcp[j] = '\0';
    return lcp;
}

int main()
{
    char *str[] = {"pie", "piermuz", "piermichele"};
    //char *str[] = {"flower","flow","flight"};
    //char *str[] = {"a"};
    //char *str[] = {"flower","flower","flower","flower"};
    printf("%s\n", longestCommonPrefix(str, 3));
    return 0;
}