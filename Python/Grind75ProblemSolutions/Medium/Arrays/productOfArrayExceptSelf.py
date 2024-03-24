from typing import List


"""
Notes:
    Limit is 32-bit integer: 4,294,967,296
    Use just string sequence of numbers, convert it into a mathematical equation, removing a number and 
    replacing a number each iteration, and merely computing the result? 

    Would a precomuptation hash table help? There is a solution with O(1) space however.

    Potentially could keep track of the product of all elements preceding the ith element. And
    the same for elements following it. But is there a way to remove a factor from the 
    suffix total without division? Or would I have to recalculate it everytime? that would be
    O(n^2) however, as I would need to iterate over the array n*n times. 

    
"""

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalArray = []
        totalProduct = 1

        for value in nums:
            totalProduct *= value

        for value in nums:
            finalArray.append(int(totalProduct/value))
        
        return finalArray

            

            


        



p1 = Solution()
print(p1.productExceptSelf([1,2,3,4]))
#print(p1.productExceptSelf([-1,1,0,-3,3]))