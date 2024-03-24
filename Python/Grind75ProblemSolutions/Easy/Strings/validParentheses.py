"""
Theory:
    Push the open bracket onto the stack. When you encounter a closed bracket, check if its the same as
    the top of the stack, if it is, pop the stack, and continue iterating. If it is not the same
    then it is not a valid string, cancel iteration, return false. If otherwise, then return true. 

Possible Test Cases:
    ([{}]) ([]{}[][{[]}])
    )
    ([)]

Big-O:
    time complexity: O(n) - because I iterate once through the array. Therefore, time increases with array size. 
    space complexity: O(n) - because I use one array, and one dictionary map. The Bracketmap is O(1), as it is constant
                             no matter how big the string is. But stack will always be n/2. Therefore it increases with
                             the size of the string, making it O(n). 

"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for character in s:

            if character in ('(', '[', '{'):
                stack.append(character)
            elif character in (')', ']', '}') and len(stack) > 0 and stack[-1] == bracketMap[character]:
                    stack.pop()
            else:
                return False

        if len(stack) == 0:
            return True
        else:
             return False



p = Solution()
print(p.isValid("[[[[["))

"""
Cleaner Solution, mildly the same thought process, with small variation:
"""

class Solution2:
    def isValid(self, s: str) -> bool:
        approved_char_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []

    
        for char in s:
            if char in approved_char_dict:
                stack.append(char)
            elif char in approved_char_dict.values():
                print(approved_char_dict[stack.pop()])
                if not stack or approved_char_dict[stack.pop()] != char:
                    return False

        return not stack  # If the stack is empty, all parentheses are matched

p2 = Solution2()
print(p2.isValid("[[[[[]]]]]"))

