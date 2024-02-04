"""
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for the LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak in a bit of sabotage while you're at it -- so you took the job gladly. 

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

-- Python cases --
Input:
solution.solution('15')
Output:
    5

Input:
solution.solution('4')
Output:
    2

*********************NOTES***********************
1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (has to be even number of pellets)

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
                        15 -> 14 -> 7 -> 6 -> 3 -> 2 -> 1

Constraint: number is <= 309 digits long

Work out how to see if number is a factor of 2^x, then keep adding or subtracting to get there?
Note - Test 9 WILL NEVER ENTER A DIVIDE BY 2 SEQUENCE. It comepletely ignores the print statement in the while loop for x%2==0 and says that it passes - must be a null string test. 

Something must be going on with my logic for when to add a pellet and when to remove a pellet. It is not the most efficient.

-----Failed Solution-----
Multiply 'factor' by 2 until it is past the x value
find difference between that number and the x value
find difference between factor/2 and the x value
compare which is smaller
use the smaller one and add to factor

--> does not account for very large numbers

"""

def solution(n):
    x = int(n)
    count = 0
    diff1 = 0
    diff2 = 0
    factor = 1

    while factor <= x:
        factor *= 2
        count += 1
    

    diff1 = factor - x
    diff2 = x - (factor/2)

    if(diff1 > diff2):
        diff1 = diff2
        count -= 1

    if(diff1 == 0):
        count -= 1
    
    
    return int(count + diff1)


print(solution('15'))
