class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        out = []
        dict = {}
        
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
            if num+1 not in dict:
                dict[num+1] = 0
            if num-1 not in dict:
                dict[num-1] = 0
        
        for num in nums:
            if dict[num] == 1:
                if dict[num+1] == 0 and dict[num-1] == 0:
                    out.append(num)
        return out
                    