package easy;
/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type. 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
 */

import java.util.Stack;

class ValidParentheses {
    Stack<Character> stack = new Stack<>();

    public boolean isValid(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{')
                stack.push(s.charAt(i));
            if (s.charAt(i) == ')') {
                if (!stack.isEmpty() && stack.peek() == '(')
                    stack.pop();
                else
                    return false;
            }
            if (s.charAt(i) == ']') {
                if (!stack.isEmpty() && stack.peek() == '[')
                    stack.pop();
                else
                    return false;
            }
            if (s.charAt(i) == '}') {
                if (!stack.isEmpty() && stack.peek() == '{')
                    stack.pop();
                else
                    return false;
            }
        }
        return stack.isEmpty();
    }
}