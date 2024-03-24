from typing import List


"""
Notes:
    Binary search operates like so: check middle of array, if target is equal to the number, return. 
    if not, then check if target is higher than middle number. If it is, split the array in half, and move
    to the higher half. If it is not, do the same for the lower half. 
    Keep going until only one element is left (worst case), and if it is not equal to target, return -1. 
    If it is, then return the index of the array. 

    To split the array in half use two pointers. One specifies the start of the array window, the other specifies 
    the end. 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:

            mid = int(left + (right-left)/2)

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
        return -1


p1 = Solution()
print(p1.search([-1,0,3,5,9,12], 9))