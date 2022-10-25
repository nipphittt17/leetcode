class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #a+b > c
        nums.sort(reverse=True)
        a,b,c = inf,inf,inf
        for num in nums:
            a, b, c = num , a, b
            if a + b > c:
                return a+b+c       
        return 0     