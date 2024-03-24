from typing import List

"""
**************SOLUTION 1*****************
O(n^2) solution (I would not use this, but if I did):
    Take the ith element, subtract its value from these future elements, if the value is negative then store a zero. 
    If the value is positive, and is greater than the current greatest difference, then store the new value. 
    Continue until the second to last element is checked. 
    Return the greatest difference (which if there were no transactions, a zero will return)

Is not accepted in LeetCode because it exceeds the time limit, passing 197 tests, as expected. 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        greatestDifference = 0
        i = 0
        while i < len(prices)-1:
            j = i+1
            while j < len(prices):
                if prices[i] < prices[j] and prices[j] - prices[i] > greatestDifference:
                    greatestDifference = prices[j] - prices[i]

                j += 1
            i += 1
        return greatestDifference

"""
p1 = Solution()
print(p1.maxProfit([7,1,5,3,6,4])) # = 5
print(p1.maxProfit([7,5,4,3,2,1])) # = 0
"""




"""
*****************SOLUTION 2******************
Notes:
    Keep track of smallest number found so far. Keep track of largest number following this smallest number. 
    if a number larger than the smallest number cannot be found, return 0
    But keep track of the greatest difference so far.

Big-O:
    time complexity:
        it is not O(1), as the runtime does not remain constant regardless of the array size n. 
        
        It is not O(log n) because it does not increase according to half the input size, where for every
        iteration the input size reduces by half. 

        It is not O(n^2) because the program does not iterate n^2 times. 

        It is not O(2^n) becuase the number of operations executed do not double with each additional 
        increase of the size of n by 1. 
       
        Therefore, it increases linearly with the size of the array. 
        This means it is O(n).
    
    space complexity:
        it is O(1) because it is constant no matter the size of n. 
    
    LeetCode runtime: 692ms, beats 90.32%
             memory: 27.49mb, beats 35.25%

    The way Leetcode executes code makes using a filewrite significantly faster. This logic 
    is not different to the top leetcode solution, except for a cleaner order of operations,
    and is ~15ms in difference to its logic without the filewrite hack. 

"""

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        largest = prices[0]
        greatestDifference = 0

        for i, value in enumerate(prices):
            
            if value < smallest:
                smallest = value
                largest = smallest
            elif value > largest:
                largest = value
                        
            if greatestDifference < largest - smallest and largest - smallest > 0:
                greatestDifference = largest - smallest

        return greatestDifference
            
        


# p2 = Solution2()
# print(p2.maxProfit([1,2])) # = 5
# print(p2.maxProfit([7,5,4,3,2,1])) # = 0



"""
****************LEETCODE SOLUTION****************
LeetCode runtime: 676ms, beats 98%
         memory: 27.39mb, beats 72%

Now this is not even all that different in runtime. Or even memory. The difference is incredibly small. 
Leetcode solution 2 really changes the runtime for this problem. 
"""

class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for value in prices:
            
            if value < min_price:
                min_price = value
            elif value - min_price > max_profit:
                max_profit = value - min_price

        return max_profit
            
        


p3 = Solution3()
print(p3.maxProfit([1,2])) # = 5
print(p3.maxProfit([7,5,4,3,2,1])) # = 0


"""
****************LEETCODE SOLUTION 2****************
LeetCode runtime: 102ms, beats 99%
         memory: 23.39mb, beats 99%

Someone figured out that using file writes vastly improved runtime just based off of how LeetCode executes its code. 
Go figure. Nothing profound here.   
"""

class Solution3:
    def maxProfit(prices):
        min_price, max_profit = float('inf'), 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit

    # with open('user.out', 'w') as f:
    #     for case in map(loads, stdin):
    #         f.write(f"{maxProfit(case)}\n")
    # exit(0)  
            
        


p3 = Solution3()
print(p3.maxProfit([1,2])) # = 5
print(p3.maxProfit([7,5,4,3,2,1])) # = 0