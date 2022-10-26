class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        neg = 0
        val = 1
        for num in nums:
            if(num < 0): neg+=1
            val*=abs(num)
        if neg%2 == 1: prod = -1*val
        else: prod = val

        if(prod < 0): return -1
        else: return 1