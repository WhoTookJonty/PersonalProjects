"""
Bunny Worker Locations
======================

Keeping track of Commander Lambda's many bunny workers is starting to get tricky. You've been tasked with writing a 
program to match bunny worker IDs to cell locations.

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the work areas 
have an unusual layout.
 They are stacked in a triangular shape, and the bunny workers are given numerical IDs starting from the corner, as follows:

| 7
| 4 8
| 2 5 9
| 1 3 6 10

Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y 
being the height from the ground. 

For example, the bunny worker at (1, 1) has ID 1, the bunny worker at (3, 2) has ID 9, and the bunny worker at 
(2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been adding a LOT of workers). 

Write a function solution(x, y) which returns the worker ID of the bunny at location (x, y). 
Each value of x and y will be at least 1 and no greater than 100,000. Since the worker ID can be very large,
 return your solution as a string representation of the number.

-- Python cases --
Input:
solution.solution(5, 10)
Output:
    96

Input:
solution.solution(3, 2)
Output:
    9

*****************Notes****************
Summary: points (x, y), with x being the distance from the vertical wall, and y being the height from the ground, 
NOT zero-indexed, each value of x and y is at least 1, no greater than 100,000, 
return discovered ID of bunny as a string representation, NO array is given - pattern of numbers

| 7
| 4 8
| 2 5 9
| 1 3 6 10

pattern: counts down by 1 along diagonal edge, starting at the last index of the last list. 

How to find number by incrementing from bottom corner:
x is column, y is row

     x|y
    [1][1]: 1

    [1][2]: 2
    [2][1]: 3

    [1][3]: 4
    [2][2]: 5
    [3][1]: 6

    [1][4]: 7
    [2][3]: 8
    [3][2]: 9
    [4][1]: 10

    pattern of row and column: diagonalNumber=number of rows in pattern. e.g. diagonal=3, then pattern is present for 3 rows
                               The values of y are reversed in their order and placed in x, or vice versa

Find First Number in Each Diagonal Pattern:
      x|y
    [1][1]: 1
    [1][2]: 2
    [1][3]: 4
    [1][4]: 7

    diff between pattern: 1, 2, 3

    Therefore:
    [1][5]: 11 (diagonal 5)
    [1][6]: 16 (diagonal 6)
    etc. 

    pattern: increment difference between each diagonal by 1 and add to previous pattern start digit

    the pattern is called the Lazy Caterer's sequence

Find Which Diagonal you are in through X and Y:
    increment x and decrement y until y=1, then the diagonal number is = x

Find Final Value:
    Find difference between the givenX value and the startingX value, add this difference to the startingX value 
    (which is the starting digit of the current diagonal)

"""
from array import *

def solution(x, y):
    tmpX = x
    tmpY = y

#Find which diagonal you are in
    while tmpX != 1:
        tmpY += 1
        tmpX -= 1

    #The Lazy caterer's sequence is a recurrence relation of the form f(n) = n + f(n-1), where n = number of cuts, 
    # or in this case the diagonal number. Uses zero indexing.
    n = tmpY - 1
    startDigit = int(((n*n)+n+2)/2)
    ans = startDigit + (tmpY - y)

    return str(ans)

def main():
    print(solution(3, 2))


if __name__ == "__main__":
    main()