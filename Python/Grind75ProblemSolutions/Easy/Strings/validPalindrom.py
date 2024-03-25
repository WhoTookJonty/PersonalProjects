

"""
Notes:
    Convert all letters to lowercase.
    Remove all spaces, commas, and special characters that are not alphanumeric
    Then create two pointers, to the left and right. 
    Increment/decrement till they reach the middle, comparing to see if the same the whole time.    
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        sAlphaValues = list([val for val in s if val.isalnum()]) #get only alphanumeric list of letters
        s = "".join(sAlphaValues) #join all these letters into one string

        left = 0
        right = len(s)-1

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                return False
        return True



p1 = Solution()
print(p1.isPalindrome("A man, a plan, a canal: Panama"))


"""
Slighlty more optimized version without a loop by using a built in string reversal technique from python
"""

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s="".join([val for val in s if val.isalnum()]) #get only alphanumeric list of letters, join this list into a string
       
        if s ==s [::-1]:
            return True
        else:
            return False



p2 = Solution2()
print(p2.isPalindrome("A man, a plan, a canal: Panama"))