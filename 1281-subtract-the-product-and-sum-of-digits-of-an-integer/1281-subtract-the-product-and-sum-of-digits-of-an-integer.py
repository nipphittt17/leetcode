class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        div = 10
        num = n
        pro = 1
        sum = 0
        
        while(num>0):
            mod = num%div
            num -= mod
            pro *= mod
            sum += mod
            num//=10
        return pro - sum
            
            
        