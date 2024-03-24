from typing import List

# index a + index b == target? 
# If not, then b+1, repeat. 
# If loop is finished, and a+b != target, then repeat the loop with a+1. 
# Keep doing this until the target is found. 
"""
Big-O: 
    time complexity = O(n^2)
    Space Complexity = O(1)
""" 

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexA = 0
        indexB = 1
        
        while indexA < len(nums):
            while indexB < len(nums):
                if nums[indexA] + nums[indexB] == target:
                    return indexA, indexB
                indexB = indexB+1
            indexA = indexA+1
            indexB = indexA+1
        return indexA, indexB
    
p1 = Solution1()

print(p1.twoSum([3, 2, 4], 6))


"""
Another solution, trading space for lower time compelxity:

Iterate through nums: 
minus each number from the target, and check if its complement is in an array of seen items. 
If not, add the number to seen, and iterate further. 

Big-O: 
time complexity: O(n)
space complexity: O(n)
"""

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, numsValue in enumerate(nums):
            complement = target - numsValue
            print(complement)
            if complement in numMap:
                return [numMap[complement], i]
            else:
                numMap[numsValue] = i 
                print(numMap)
        return []


p2 = Solution2()
print(p2.twoSum([3, 2, 4], 6))

            
            

        