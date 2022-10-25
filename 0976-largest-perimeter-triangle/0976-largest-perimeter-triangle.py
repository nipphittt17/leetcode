class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # triange in-equality a+b > c
        # sum of 2 smallest > largest
        nums.sort(reverse=True)
        a,b,c = inf,inf,inf
        for n in nums:
            a, b, c = n, a, b
            if a + b > c:
                return a+b+c       
        return 0     