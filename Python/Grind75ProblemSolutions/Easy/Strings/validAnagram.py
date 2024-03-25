"""
Notes:
    Keep a count of each character in the string. If they are equal, then it is an anagram. 
    This will take O(n) time because you go through each string once. 
    This will take O(1) space as while there is a dictionary being used, it is restricted to 26 latin characters.

PseudoCode:
    Loop through s, for each character.
        If the character already exists in a KV dictionary, then update its value by 1
        if not, then add it, and set its value to 1. 

    Repeat the same for t. 

    Once complete, compare each string's character count.

A cleaner way to do it:
    increment a dictionary in the same way, then decrement each character value pair. 
    If, at the end of the loop, each KV pair is equal to zero, then the string is not an anagram.
    This is implemented below.
"""



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}

        for x in s:
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1

        for x in t:
            if x in dictionary:
               dictionary[x] -= 1
            else:
               return False
        
        for x in dictionary:
            if dictionary[x] != 0:
                return False
        
        return True



p1 = Solution()
print(p1.isAnagram(s = "anagram", t = "naagram"))