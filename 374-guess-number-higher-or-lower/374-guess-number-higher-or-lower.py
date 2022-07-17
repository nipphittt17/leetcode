# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
    
        left = 1
        right = n
        while left <= right:
            guessNum = (left+right)//2
            print(guessNum)
            check = guess(guessNum)
            if check == 0: return guessNum
            elif check == 1: left = guessNum+1
            else: right = guessNum-1 
        
        